# Task 1 Input Length Validator:

'''
Write a script that asks for and checks the lenght of the user's first name and last name.
Both should be at least 2 characters long. if not, print an error message.

'''

def full_name_user(first_name, last_name):
    first_name_lenght = len(first_name)
    last_name_lenght = len(last_name)

    if first_name_lenght > 2:
        print(f"The lenght of first name {first_name} is {first_name_lenght}: ")
    if last_name_lenght > 2:
        print(f"The lenght of the last name {last_name} is {last_name_lenght}: ")

    if first_name_lenght <= 2 or last_name_lenght <= 2:
        return "Either first or last name are too short, please enter a longer name."
    else:
        return f"So in total; The First name lenght is: {first_name_lenght} and Last name lenght is: {last_name_lenght}."



while True:
    first_name_input = input("Enter your first name: ")
    last_name_input = input("Enter your last name: ")

    measured_name = full_name_user(first_name_input, last_name_input)
    print(measured_name)


    continue_input = input("do you want to check the lenght of another last name or first name? (yes/no)").lower()
    if continue_input != 'yes':
        break
