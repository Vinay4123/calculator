#Write a python program which will keep adding a stream of numbers inputted by the user. The adding stops as soon as user presses q key on the keyboard

sum =0
while(True):
    userInput = input("Enter the Price: \n")
    if(userInput!='q'):
        sum = sum + int(userInput)
    else:
        print("Thanks for using our calculator")
        print(f"Your total bill is {sum}")
        break

