# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Gina Roma 
# Created: 2020-02-24

import sys

def name():
    # get user's first and last names

    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last


def password():
    passwd = input("Create a new password: ")
    if checkStrength(passwd):
        print("Fool of a Took! That password is feeble!")
        print("This password is weak. You need at least one uppercase letter, one lowercase letter,\nand your password has to be 8 characters long.")
        return password() 
    else:
       print("The force is strong in this one…") 
    return passwd

# This checks the strength of the password
def checkStrength(passwd):
    return len(passwd) < 8 or passwd.islower() or passwd.isupper() or passwd.isnumeric()
    
                   
def username():
    first, last = name()
    uname = str(first + "." + last)
    return uname
                 
def main():
    uname = username().lower()

    passwd = password()
    
    print("Account configured. Your new email address is",uname, "@marist.edu")
    print("Your username is", uname, ".")
    print("Your password is", passwd, ".")
    sys.exit
    
main()








