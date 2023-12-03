print("Welcome to Quiz Game! ")

initial_answer = input("Do You want to play the Quiz Game? ")
if initial_answer.lower() != "yes":
    quit()

print("Alright, let's play! ")
points = 0

answer = input("What does CPU mean in computers? ")
if answer.lower() == "central processing unit":
    print("You guessed it right!")
    points += 1
    print(f"You have gained 1 point! Your total points are: {points} points")
else:
    print("You are wrong")
    print(f"Your total points are: {points} points")


answer = input("What does GPU mean in computers? ")
if answer.lower() == "graphics processing unit":
    print("You guessed it right!")
    points += 1
    print(f"You have gained 1 point! Your total points are: {points} points")
else:
    print("You are wrong")
    print(f"Your total points are: {points} points")


answer = input("What does RAM mean in computers? ")
if answer.lower() == "random access memory":
    print("You guessed it right!")
    points += 1
    print(f"You have gained 1 point! Your total points are: {points} points")
else:
    print("You are wrong")
    print(f"Your total points are: {points} points")


answer = input("What does PSU mean in computers? ")
if answer.lower() == "power supply":
    print("You guessed it right!")
    points += 1
    print(f"You have gained 1 point! Your total points are: {points} points")
else:
    print("You are wrong")
    print(f"Your total points are: {points} points")

final_score = points / 4 * 100
print(f"You have correctly answered {final_score}% of questions")
if points >= 3:
    print("Congratulations, You passed the Quiz!")
else:
    print("You lost...")
    
