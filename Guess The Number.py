#Guess The Number
import random
input_a = int(input("Enter 1st number : "))
input_b = int(input("Enter 2nd number : "))
num_list = []    
for i in range(input_a,input_b + 1):
    num_list.append(i)
random_num = random.choice(num_list)
player_1 = None
player_2 = None
attempt_p1 = 1
attempt_p2 = 1
print("Player 1 :")
print("Your chance to guess the number ")                      
while True:
    guesser = int(input(""))
    if guesser<random_num:
        print("Your guessed number is smaller than the actual number")
        print("TRY AGAIN !!!!!!")
    elif guesser>random_num:
        print("Your guessed number is bigger than actual number  ")
        print("TRY AGAIN !!!!!!")
    else:
        print("CONGRATULATION !!!!!!")

        print(f"you guessed the actual number in {attempt_p1} attemps ")
        break
    attempt_p1 += 1
print("-"*100)
print("Player 2 :")
print("Your chance to guess the number ") 
random_num = random.choice(num_list)
while True: 
    guesser = int(input(""))
    if guesser<random_num:
        print("Your guessed number is smaller than the actual number")
        print("TRY AGAIN !!!!!!")
    elif guesser>random_num:
        print("Your guessed number is bigger than actual number  ")
        print("TRY AGAIN !!!!!!")
    else:
        print("CONGRATULATION !!!!!!")
        print(f"you guessed the actual number in {attempt_p2} attemps ")
        break
    attempt_p2 += 1

print("-"*100)
print(f"The total attempts needed by player 1 is {attempt_p1}  ")
print(f"The total attempts needed by player 2 is {attempt_p2}  ")
print("-"*100)
if attempt_p1>attempt_p2:
    print("Player 2 won the game ")
elif attempt_p2>attempt_p1:
    print("Player 1 won the game")
elif attempt_p1 == attempt_p2:

    print("Its a Draw")


