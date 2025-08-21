# Start with users that need to be verified,
# and an mepty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users= []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users: # Meaning while this list has itmes.
    current_user = unconfirmed_users.pop() # Pop rmeoves the last itme in a list

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user) # Populating the new list.

# Display all confirmed users.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(f"- {confirmed_user.title()}")
