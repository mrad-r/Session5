name = input("What is your name? ")
#let's write this in a simpler way
age2 = input(f"How old are you {name}? ")

try:
    age2 = int(age2)
    print(f"{name}, you were born in {2024-age2}")
#When there is a problem, the follow lines are printed
except ValueError: #Here we indicate what type of error will produce the following lines
    print("please enter a valid value for age")
    print("I can also print this in case of error that I prevented")

except ZeroDivisionError:
    print("You cannot divide by 0!")

else: # This is for no exception
    print("Thank you for playing as expected")
finally: # This will be executed no matter what, at the very end
    print("Thanks for playing the game")





