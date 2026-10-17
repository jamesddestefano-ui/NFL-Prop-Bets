"""Shared fake connection for offline PRIME ingestion tests."""
class Cursor:
    def __init__(self, count=0): self.count=count
    def fetchone(self): return (self.count,)
class FakeConnection:
    def __init__(self):
        self.fingerprints=set()
        self.pending=None
    def execute(self, sql, params=None):
        if sql=="BEGIN TRANSACTION": self.pending=None
        elif sql.startswith("SELECT COUNT(*)"): return Cursor(int(params[0] in self.fingerprints))
        elif "INSERT INTO my_db.prime_research.ingestion_batches" in sql: self.pending=params[0]
        elif sql=="COMMIT" and self.pending: self.fingerprints.add(self.pending)
        elif sql=="ROLLBACK": self.pending=None
        return Cursor()
