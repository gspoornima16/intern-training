users = db.query(User).all()

for user in users:
    print(f"SL No: {user.sl_no}")
    print(f"User ID: {user.user_id}")
    print(f"User Name: {user.user_name}")
    print(f"Email: {user.email_id}")
    print("----------------------")