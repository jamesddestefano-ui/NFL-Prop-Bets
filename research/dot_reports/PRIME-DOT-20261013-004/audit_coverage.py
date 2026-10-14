"""Read-only reproduction on caller-supplied local CSV directory; no row content output."""
import csv,json,sys
from pathlib import Path
wanted={'decision_ledger.csv':['odds','estimated_over_probability','estimated_under_probability','no_vig_probability','actual_result','closing_odds'],'bet_history.csv':[],'pass_ledger.csv':['odds','actual_result','closing_odds'],'missed_bets.csv':['recommended_odds','outcome','closing_odds'],'line_history.csv':['odds','opposite_side_odds','source_url'],'ev_source_signals.csv':[],'weekly_attribution.csv':[]}
summary={}
for name,fields in wanted.items():
    with (Path(sys.argv[1])/name).open(newline='') as f:
        rows=[r for r in csv.reader(f) if r]
    header=rows[0];good=[dict(zip(header,r)) for r in rows[1:] if len(r)==len(header)]
    summary[name]={'nonblank_data_rows':len(rows)-1,'header_width':len(header),'width_valid_rows':len(good),'width_mismatches':len(rows)-1-len(good),'nonempty_fields_among_width_valid_rows':{k:sum(bool(r[k].strip()) for r in good) for k in fields}}
print(json.dumps(summary,indent=2))
