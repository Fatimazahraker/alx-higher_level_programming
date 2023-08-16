--echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
CREATE TABLE
    IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256))
