CREATE TABLE Users( 
 sl_no SERIAL PRIMARY KEY,
 user_id INT,
 User_name VARCHAR(35) NOT NULL , 
 Email_id VARCHAR(100) NOT NULL UNIQUE )

select*from Users

INSERT INTO Users (user_id,user_name,email_id) VALUES(1003,'Aiden','aiden99@gmail.com');
INSERT INTO Users (user_id,user_name,email_id) VALUES(1005,'Bella','Bella27@gmail.com');
INSERT INTO Users (user_id,user_name,email_id) VALUES(1007,'Cameron','Cameron01@gmail.com');
INSERT INTO Users (user_id,user_name,email_id) VALUES(1009,'Daniel','Daniel02@gmail.com');
INSERT INTO Users (user_id,user_name,email_id) VALUES(1011,'Eva','eva66@gmail.com');

select user_name from Users where sl_no=4
select user_name,email_id from Users where sl_no=4

select sl_no,user_name,email_id from Users where user_name='Eva'

select sl_no,user_name,email_id from Users ORDER BY sl_no DESC
select sl_no,user_name,email_id from Users ORDER BY user_name DESC

CREATE TABLE posts(
post_no SERIAL ,
user_id int,
posts VARCHAR(200) NOT NULL,
description VARCHAR(200) NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(user_id)
)

INSERT INTO posts(user_id,posts,description) VALUES(1003,'photo','evening')
INSERT INTO posts(user_id,posts,description) VALUES(1005,'statement','defining the statement')
INSERT INTO posts(user_id,posts,description) VALUES(1005,'song','singing')
INSERT INTO posts(user_id,posts,description) VALUES(1007,'art','painting')
INSERT INTO posts(user_id,posts,description) VALUES(1007,'art','painting')
INSERT INTO posts(user_id,posts,description) VALUES(1009,'fun','arcade')
INSERT INTO posts(user_id,posts,description) VALUES(1011,'evening','coffee')
INSERT INTO posts(user_id,posts,description) VALUES(1007,'morning','sunrise')
INSERT INTO posts(user_id,posts,description) VALUES(1007,'data','base')
INSERT INTO posts(user_id,posts,description) VALUES(1007,'dbms','sql')
INSERT INTO posts(user_id,posts,description) VALUES(1009,'sql_language','mysql')
INSERT INTO posts(user_id,posts,description) VALUES(1009,'sql_lan1','Postgresql')
INSERT INTO posts(user_id,posts,description) VALUES(1003,'restapi','restfulapi')
INSERT INTO posts(user_id,posts,description) VALUES(1003,'sql commands','sql clauses')
INSERT INTO posts(user_id,posts,description) VALUES(1003,'sql commands','select')
INSERT INTO posts(user_id,posts,description) VALUES(1003,'DQL','clauses')
INSERT INTO posts(user_id,posts,description) VALUES(1005,'DDL','Defining')
INSERT INTO posts(user_id,posts,description) VALUES(1005,'DML','manipulation')
INSERT INTO posts(user_id,posts,description) VALUES(1011,'git','github')
INSERT INTO posts(user_id,posts,description) VALUES(1011,'repository','remote')

update posts
SET posts= 'sql command 1'
where description = 'select'

delete from posts 
where posts = 'sql command 1'

select users.user_name,posts.posts,posts.description
from users inner join posts
on users.user_id=posts.user_id

select count(description),user_id 
from posts
group by user_id

ALTER TABLE posts
RENAME COLUMN posts TO post_list;