from newone import client


def find_user(username):
    print(username)
    result = client.Employees.Users.find_one({"username": username})
    if result:
        return result
    else:
        return False


def reg_user(new_user):
    result = client.Employees.Users.insert_one(new_user)
    print(result)
    return result

def rm_user(username):
    result = client.Employees.Users.delete_one({"username":username})
    print(result)
    print(result.deleted_count)
    return result


def update_user_pwd(username, password):
    result = client.Employees.Users.update_one({"username": username}, {"$set": {"password": password}})
    return result
