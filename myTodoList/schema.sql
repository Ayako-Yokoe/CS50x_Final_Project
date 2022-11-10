DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    task TEXT NOT NULL,
    duedate TEXT,
    priority INTEGER,
    completed INTEGER NOT NULL
);
