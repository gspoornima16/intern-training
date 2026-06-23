CREATE TABLE Users( 
 sl_no SERIAL PRIMARY KEY,
 User_name VARCHAR(35) NOT NULL , 
 Email_id VARCHAR(100) NOT NULL UNIQUE )

select*from Users

INSERT INTO Users (user_name,email_id) VALUES('Aiden','aiden99@gmail.com');
INSERT INTO Users (user_name,email_id) VALUES('Bella','Bella27@gmail.com');
INSERT INTO Users (user_name,email_id) VALUES('Cameron','Cameron01@gmail.com');
INSERT INTO Users (user_name,email_id) VALUES('Daniel','Daniel02@gmail.com');
INSERT INTO Users (user_name,email_id) VALUES('Eva','eva66@gmail.com');

select user_name from Users where sl_no=4
select user_name,email_id from Users where sl_no=4

select sl_no,user_name,email_id from Users where user_name='Eva'

select sl_no,user_name,email_id from Users ORDER BY sl_no DESC
select sl_no,user_name,email_id from Users ORDER BY user_name DESC