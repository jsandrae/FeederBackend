-- sqlite3 feedingLog.sqlt < schema.sql
drop table if exists feedingLog;
create table feedingLog (
  'id' integer primary key autoincrement,
  'username' text not null,
  'timestamp' DATETIME DEFAULT (datetime('now','localtime'))
);
