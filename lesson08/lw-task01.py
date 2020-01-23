import os
users_file = "./users.txt"
userlst = []

login = input("Input username: ")
password = input("Input password: ")
print(os.path.isfile(users_file))
    
with open(users_file, 'r') as logins:
    userslst = logins.readlines()
    print(userlst)
if login in userlst:
    print(login, " is exist in userlist")
else:
    with open(users_file, 'a') as logins:
        logins.write(login)
        logins.write(password)

    

    
        
