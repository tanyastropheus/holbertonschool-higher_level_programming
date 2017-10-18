-- create a user 'user_0d_1' and grant all privileges
CREATE USER user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
CREATE ALL PRIVILEGES on * . * TO user_0d_1@localhost;
