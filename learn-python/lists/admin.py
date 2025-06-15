usernames = []
# usernames = ['admin', 'tims', 'ubuntu', 'ec2', 'john']
if usernames == []:
    print("We need to find some users")
else:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()}, would you like to see a status report?")
        else:
            print(f"Welcome {username.title()}")

