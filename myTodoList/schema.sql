DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "day" TIMESTAMP NOT NULL,
    "task" TEXT NOT NULL,
    "datetime" TIMESTAMP,
    "priority" INTEGER,
    "completed" TEXT NOT NULL
);