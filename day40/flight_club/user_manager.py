from data_manager import DataManager

def register_user():
    print("Welcome to Flight Club!\nWe find the best flight deals and email you.")
    first = input("What's your first name? ")
    last = input("What's your last name? ")
    email = input("What's your email? ")
    confirm = input("Type your email again: ")
    if email == confirm:
        DataManager().add_user(first, last, email)
        print("You're in the club! 🎉")
    else:
        print("Emails don't match. Please try again.")