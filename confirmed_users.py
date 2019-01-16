# Start with users that need to be verified,
# and an empty list to hold confirmed users.


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users: # kj�rer s� lenge denne ikke er tom
    current_user = unconfirmed_users.pop() # pop tar verdien ut...

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())