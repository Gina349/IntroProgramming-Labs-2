# guessing-game.py
# [0] means first letter of any variable placed before it. 

def main():
    print("PYTHON GUESSING GAME. ")
    
    print()
    animal = ("dog")
    x=0
    q = "quit"
    yes = "y"
    no = "n"
    while x==0:
        print("This program is thinking of an animal; he/she is mans best friend.\nWhat is the animal this program is thinking? ")
        print()
        answer = input("Enter choice here\n")
        answer = answer.lower()
        if answer == animal:
            print("Congratulations you have won!")
            x=1
    
            like = input("Do you like Dogs?\nAnswer y for yes and n for no.\n")

            if like == "y" or like == "Y":
                print("Aren't dogs so fluffy?")
            elif like == "n" or like == "N":
                print("I guess your not a dog person.")
            
        elif answer[0] == "q":
            x=1
        else:
            print("Sorry your answer is inncorrect would you like to try again?")
            print()
    
main()
