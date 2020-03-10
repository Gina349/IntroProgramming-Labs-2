# listexamples.py
# Lab 6
# Gina Roma 

Listcolors = ["red","blue","green","yellow","orange","purple"]

def showTitle():
    print("Color Preference Evaluator")

def promptForColor():
    color = input("Enter a color: ")
    color.strip()
    return color.upper()

def confirmColor(color):
        # Print color as part of a confirmation message or something like that
        # If you 
        comfirm = input("Is this the color you want " + color + " yes or no? ")
        if(comfirm == "yes"):
            return True
        else:
            return False

def containsElement(color):
    for x in Listcolors:
        if color == x.upper():
            return True
        if x == Listcolors[-1].upper():
            return False
        
def praiseUser():
    print("good job")

def ridiculeUser():
    print("You goofed")

def main():

    showTitle()

    color = promptForColor()

    confirmColor(color)

    right = containsElement(color)

    if right == True:
        praiseUser()
    else:
        ridiculeUser()

    print("Thank you for playing")

main()

    

    

    

    

    
