--echo 'SELECT * FROM unique_id;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256)
