# 5-10 Checkining Usernames
current_users = ['john', 'Em', 'mamaDEE', 'SallyTims', 'ubuntu', 'admin', 'Justice']

# To convert all existing usernames to lowercase
users = []

for current_user in current_users:
    users.append(current_user.lower())

# To compare all new usernames in lowercase with users 
new_users = ['trust', 'david', 'ola', 'ADMIN', 'Ubuntu', 'me']

for new_user in new_users:
    if new_user.lower() in users:
        print(f"{new_user.title()}, please choose a new username.")
    else:
        print(f"{new_user.title()}, you can proceed with the registration.")
