# guessing-game.py

def main():
    print("PYTHON GUESSING GAME. ")
    
    print()
    animal = ("Dog")
    x=0
    while x==0:
        print("This program is thinking of an animal; he/she is mans best friend\nWhat is the animal this program is thinking? ")
        print()
        answer = input("Enter choice here\n")
        if answer == animal:
            print("Congratuations you have won!")
            x=1
        else:
            print("Sorry your answer is inncorrect would you like to try again? ")

        
main()
