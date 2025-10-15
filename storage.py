#Operations to ADD, Read,  

users = []  # in-memory list to store user data
next_id = 1

def create_user(name, email):
    global next_id
    user = {"id": next_id, "name": name, "email": email}
    users.append(user)
    next_id += 1
    return user

def read_users():
    return users

def read_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            return user
    return None

def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return True
