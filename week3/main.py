from database import engine, SessionLocal, Base
from models import User,Post


Base.metadata.create_all(bind=engine)

db = SessionLocal()

# posts1=Post(post_no=2,user_id=1002,post_list='fastapi',desscription='learning')
# posts2=Post(post_no=3,user_id=1003,post_list='exercise',desscription='walking')
# posts3=Post(post_no=4,user_id=1004,post_list='mysql',desscription='sqlalchemy')
# posts4=Post(post_no=5,user_id=1004,post_list='fun',desscription='arcade')
# posts5=Post(post_no=6,user_id=1005,post_list='evening',desscription='coffee')
# posts6=Post(post_no=7,user_id=1005,post_list='art',desscription='painting')
# # posts=Post(post_no=8,user_id=1005,post_list='song',desscription='singing')



# db.add_all([posts1,posts2,posts3,posts4,posts5,posts6])
# db.commit()
# db.close()

# find_all
users = db.query(User).all()

for user in users:
    print(f"SL No: {user.sl_no}")
    print(f"User ID: {user.user_id}")
    print(f"User Name: {user.user_name}")
    print(f"Email: {user.email_id}")
    print("----------------------")


user = db.query(User).filter(User.user_id ==1005).first()
if user:
    user.user_name = "Zoho"
    db.commit()
    db.refresh(user)
    print(user.email_id)
else:
    print("User not found")


user = db.query(User).filter(User.email_id == "Rana@gmail.com").first()

if user:
    db.delete(user)
    db.commit()
    print("User deleted successfully.")
else:
    print("User not found.")
print("-"*30)

user = db.query(User).filter(User.user_id == 1005).first()

if user:
    print(user.user_name)

    for i in user.posts:
        print(f"{i.post_no}, {i.desscription}, {i.user_id}")
else:
    print("User not found")
