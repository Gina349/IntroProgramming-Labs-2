# guessing-game.py

def main():
    print("PYTHON GUESSING GAME. ")
    
    print()
    animal = ("dog")
    x=0
    q = "quit"
    while x==0:
        print("This program is thinking of an animal; he/she is mans best friend\nWhat is the animal this program is thinking? ")
        print()
        answer = input("Enter choice here\n")
        answer = answer.lower()
        if answer == animal:
            print("Congratulations you have won!")
            x=1
            
        elif answer[0] == "q":
            x=1
        else:
            print("Sorry your answer is inncorrect would you like to try again?")
            print()
    
main()
