import random as rd

def Guess_number():
    print("Welcome to the number Guessing Game!")
    print("Caution, Before Starting Game you should guess numbers from 1 to 100.")
    
    n=rd.randint(1,101)
    attempts=0
    
    while True:
        try:
            guess_num=int(input("Enter the Guess Number: "))
            attempts+=1
            
            if guess_num < n:
                print("Too low! Try again.")
            elif guess_num > n:
                print("Too high! Try again.")
            else:
                print(f"Congratulation! You guess the number in {attempts} attempts.")
                break
        
        except ValueError:
            print("Invalid Input, Please Enter a number.")
            
    
Guess_number()
    
