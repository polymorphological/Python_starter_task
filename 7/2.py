short_links = {}

def shorten_link(long_link, short_name):
    short_links[short_name] = long_link
    print(f"Link {long_link} has been shortened to {short_name}")

def get_long_link(short_name):
    if short_name in short_links:
        print(f"The long link for {short_name} is {short_links[short_name]}")
    else:
        print(f"{short_name} not found.")

long_link = input("Enter the long link: ")
short_name = input("Enter the short name: ")
shorten_link(long_link, short_name)

short_name = input("Enter the short name to get long link: ")
get_long_link(short_name)
