from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__="users1"
    sl_no=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, unique = True)
    user_name=Column(String,nullable=False)
    email_id=Column(String,unique=True)
    posts=relationship("Post", back_populates="user")

class Post(Base):
    __tablename__="posts1"
    post_no=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey("users1.user_id"))
    post_list=Column(String)
    desscription=Column(String)
    user= relationship("User", back_populates="posts")