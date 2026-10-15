#!/usr/bin/env python3
"""Read-only, SHA-pinned proposal audit. Never writes a production ledger.
Usage: python verify_csv_proposal.py --source-dir ../source/data --output-dir ./results
All output redacts ticket IDs, values and cash facts. Source archives stay private.
"""
import argparse,csv,hashlib,io,json,pathlib,unittest
SOURCE = {
 'decision_ledger.csv': ('82f1a4297ee7e7c64dc1f2d37f78ec19729ef416',60,26),
 'bet_history.csv': ('9035f654eff5fb3a0be188542593c62c3ba00b05',26,5),
 'pass_ledger.csv': ('e1644b9ee70ba6b39aa1579eae1e03b22151265c',25,17)}
# Zero-based token positions. Conditional candidate edits, NOT approved repairs.
OPS = {'decision_ledger.csv': {6:('merge',58),7:('delete_empty',24),12:('delete_empty',29),13:('delete_empty',24),26:('insert_empty',25),27:('insert_empty',25)},
       'bet_history.csv':{n:('delete_empty',24) for n in range(2,7)},
       'pass_ledger.csv':{n:('delete_empty',23) for n in range(15,18)}}
def blob_sha(data):
 return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def parse(data):
 return list(csv.reader(io.StringIO(data.decode('utf-8'),newline=''),strict=True))
def propose(row,op):
 kind,i=op;r=list(row)
 if kind=='delete_empty':
  if r[i]!='': raise ValueError('Refuse to delete nonempty source token')
  del r[i]
 elif kind=='insert_empty':r.insert(i,'')
 elif kind=='merge':r[i:i+2]=[r[i]+','+r[i+1]]
 else: raise ValueError('Unknown operation')
 return r
def mapping(n,op):
 a=[str(i) for i in range(n)];kind,i=op
 if kind=='delete_empty':del a[i]
 elif kind=='insert_empty':a.insert(i,'NEW_EMPTY_UNKNOWN')
 else:a[i:i+2]=[f'{i} + literal comma + {i+1}']
 return a
def reverse(candidate,op,original):
 r=list(candidate);kind,i=op
 if kind=='delete_empty':r.insert(i,'')
 elif kind=='insert_empty':
  assert r[i]=='';del r[i]
 else:r[i:i+1]=original[i:i+2]
 return r
class Tests(unittest.TestCase):
 def test_quote_comma(self):self.assertEqual(parse(b'a,b\n"x,y",z\n')[1],['x,y','z'])
 def test_embedded_newline(self):self.assertEqual(parse(b'a,b\n"x\ny",z\n')[1],['x\ny','z'])
 def test_doubled_quotes(self):self.assertEqual(parse(b'a,b\n"x""y",z\n')[1],['x"y','z'])
 def test_unclosed_quote(self):
  with self.assertRaises(csv.Error):parse(b'a,b\n"x,y')
 def test_refuse_data_loss(self):
  with self.assertRaises(ValueError):propose(['id','nonempty'],('delete_empty',1))
 def test_unknown_preserved(self):self.assertEqual(propose(['id',''],('insert_empty',1)),['id','',''])
 def test_hash_newline_sensitive(self):self.assertNotEqual(blob_sha(b'a\n'),blob_sha(b'a'))
 def test_empty_position_not_identifiable(self):
  # Multiple deletions in a blank run yield the same candidate. Width is not semantics.
  r=['id','','','42'];self.assertEqual(propose(r,('delete_empty',1)),propose(r,('delete_empty',2)))
 def test_insert_ambiguous(self):
  self.assertNotEqual(propose(['id','47','53'],('insert_empty',1)),propose(['id','47','53'],('insert_empty',2)))
 def test_wrong_width_detected(self):self.assertNotEqual(len(parse(b'a,b\nx,y,z')[1]),2)
 def test_roundtrip(self):
  for row,op in [(['id','','x'],('delete_empty',1)),(['id','x'],('insert_empty',1)),(['id','a',' b'],('merge',1))]:
   self.assertEqual(reverse(propose(row,op),op,row),row)
 def test_writer_roundtrip(self):
  a=['id','with, comma','quote"','line\nbreak',''];f=io.StringIO(newline='');csv.writer(f).writerow(a);self.assertEqual(parse(f.getvalue().encode()),[a])
def audit(source):
 result={'source_commit':'46526c2f2758be375609eff8c15fd60e7caeaa50','classification':'EMPIRICAL EVIDENCE: bounded read-only structural audit','production_edits':False,'all_candidates_require_review':True,'files':[],'candidate_diffs':[]}
 for name,(sha,width,count) in SOURCE.items():
  data=(source/name).read_bytes()
  if blob_sha(data)!=sha:raise ValueError(f'Source hash mismatch: {name}. Stop; do not fuzzy-apply.')
  rows=parse(data);header=rows[0]
  assert len(header)==width and len(rows)-1==count
  bad={n for n,r in enumerate(rows[1:],2) if len(r)!=width};assert bad==set(OPS[name])
  ids=[r[0] for r in rows[1:]];assert len(ids)==len(set(ids))
  result['files'].append({'path':'data/'+name,'git_blob_sha':sha,'bytes':len(data),'records':count,'header_width':width,'malformed':len(bad),'sha256':hashlib.sha256(data).hexdigest()})
  for n,op in OPS[name].items():
   r=rows[n-1];p=propose(r,op);assert len(p)==width;assert reverse(p,op,r)==r
   if op[0]!='merge':assert [x for x in r if x]!=[ ] and [x for x in r if x]==[x for x in p if x]
   # No new nonempty value, token order unchanged, only delimiter/empty proposal.
   if name=='decision_ledger.csv':assert p[33] in ['BET','PASS','WATCH','LEAN','AVOID']
   if name=='bet_history.csv':assert p[20] in ['WIN','LOSS','PUSH','VOID']
   if name=='pass_ledger.csv':assert p[12] in ['PASS','AVOID']
   digest=hashlib.sha256(json.dumps(r,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
   result['candidate_diffs'].append({'path':'data/'+name,'csv_record_number_including_header':n,'immutable_locator':f'{sha}:record:{n}','row_token_sha256':digest,'id_sha256':hashlib.sha256(r[0].encode()).hexdigest(),'original_field_count':len(r),'proposed_field_count':len(p),'operation':op[0],'original_zero_based_index':op[1],'before_token_indexes':list(range(len(r))),'after_token_mapping':mapping(len(r),op),'approval':'MANUAL_REVIEW_REQUIRED','values_redacted':True})
 return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--source-dir',type=pathlib.Path);ap.add_argument('--output-dir',type=pathlib.Path);args=ap.parse_args()
 t=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
 if not t.wasSuccessful():raise SystemExit(1)
 if args.source_dir:
  report=audit(args.source_dir)
  report['synthetic_unittests_passed']=t.testsRun
  if args.output_dir:
   args.output_dir.mkdir(parents=True,exist_ok=True)
   # Guard against output inside source tree; never overwrite sources.
   if args.output_dir.resolve()==args.source_dir.resolve() or args.source_dir.resolve() in args.output_dir.resolve().parents:raise ValueError('Output must be separate from sources')
   (args.output_dir/'audit-results.json').write_text(json.dumps(report,indent=2)+'\n')
  print(json.dumps({'source_blobs_verified':3,'malformed_records':14,'candidate_widths_validated':14,'synthetic_tests':t.testsRun,'production_edits':False}))
