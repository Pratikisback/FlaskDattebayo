from newone import client


def find_user(username):
    print(username)
    result = client.Employees.Users.find_one({"username": username})
    return result


def reg_user(new_user):
    result = client.Employees.Users.insert_one(new_user)
    return result

def rm_user(username):
    result = client.Employees.Users.delete_one({"username":username})
    print(result)
    print(result.deleted_count)
    return result

def update_user(username):
    result = client.Employees.Users.update_one({"username": username})
    return result