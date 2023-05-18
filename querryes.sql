CREATE TABLE tasks(id INT PRIMARY KEY auto_increment,name VARCHAR(255),done BOOL default 0);

CREATE TABLE IF NOT EXISTS tasks(id INT PRIMARY KEY auto_increment,name VARCHAR(255),done BOOL default 0);

SELECT * FROM tasks;

INSERT INTO tasks (name) VALUES ('Learn Python');

INSERT INTO tasks (name) VALUES ('Do an Python app');
DROP TABLE tasks;

SELECT * FROM tasks WHERE ID=1;

UPDATE tasks SET name='Most important task' WHERE id=1

UPDATE tasks SET done='1' WHERE id=1

DELETE FROM tasks WHERE id=22

SELECT done FROM tasks where id=1