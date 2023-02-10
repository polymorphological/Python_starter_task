username = "admin"
password = "password"
attempts = 0
while attempts < 3:
    user_username = input("введіть username: ")
    user_password = input("введіть password: ")
    if user_username == username and user_password == password:
        print(f"Authentication успішна, passed on {attempts + 1} attempt.")
        break
    else:
        attempts += 1
        if attempts < 3:
            print("Incorrect login or password, please try again.")
        else:
            print("Maximum number of attempts reached.")

