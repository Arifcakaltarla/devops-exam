CREATE TABLE IF NOT EXISTS students (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  track TEXT NOT NULL
);

INSERT INTO students (name, track) VALUES
('Shuriik3n', 'DevOps'),
('Alice', 'Cloud'),
('Bob', 'Networking');
