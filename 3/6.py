day = input("Enter the day of the week: ").lower()

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    print("Today is a work day.")
elif day == "saturday" or day == "sunday":
    print("Today is a weekend.")
else:
    print("This day does not exist.")
