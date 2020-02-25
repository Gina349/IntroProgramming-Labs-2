# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Gina Roma 
# Created: 2020-02-24


def name():
    # get user's first and last names

    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last


def password():
    passwd = str(input("Create a new password: "))
    
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!\nThis password is weak")
        passwd = input("Create a new password with 8 characters: ")
        print(passwd, "\nThis password is strong")
    
    return passwd
    
    
    
def username():
    first, last = name()
    uname = str(first + "." + last)
    return uname
    
               
def main():
    uname = username()

    passwd = password()
    
    print("Account configured. Your new email address is",uname, "@marist.edu")
    print("Your username is", uname, ".")
    print("Your password is", passwd, ".")

    
main()
