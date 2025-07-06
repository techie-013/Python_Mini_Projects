print("Welcome to An Interesting Quiz..")

playing = input("Are you ready to juggle your mind?")

if playing.lower() != "yes":
    quit()

print("Awesome Lets's Start!!")

score = 0
# Question 1
answer1 = input("1. Which key is used to refresh a webpage? ").lower()
if answer1 == "f5":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: F5\n")

# Question 2
answer2 = input("2. Which company developed Windows? ").lower()
if answer2 == "microsoft":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Microsoft\n")

# Question 3
answer3 = input("3. Which language uses indentation instead of braces? ").lower()
if answer3 == "python":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Python\n")

# Question 4
answer4 = input("4. Which company created the iPhone? ").lower()
if answer4 == "apple":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Apple\n")

# Question 5
answer5 = input("5. Which company owns GitHub? ").lower()
if answer5 == "microsoft":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Microsoft\n")

# Question 6
answer6 = input("6. What is the most popular programming language in 2024? ").lower()
if answer6 == "python":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Python\n")

# Question 7
answer7 = input("7. Which tool do developers use to track code versions? ").lower()
if answer7 == "git":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Git\n")

# Question 8
answer8 = input("8. What do we call a software error or flaw? ").lower()
if answer8 == "bug":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Bug\n")

# Question 9
answer9 = input("9. What programming language runs in the browser? ").lower()
if answer9 == "javascript":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: JavaScript\n")

# Question 10
answer10 = input("10. What’s the short name for malicious software? ").lower()
if answer10 == "malware":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Malware\n")

# Question 11
answer11 = input("11. What do we call unwanted email messages? ").lower()
if answer11 == "spam":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Spam\n")

# Question 12
answer12 = input("12. Which key opens the Start Menu on a Windows PC? ").lower()
if answer12 == "windows":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Windows\n")

# Question 13
answer13 = input("13. What is the brain of the computer? ").lower()
if answer13 == "processor":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is: Processor\n")

# Final Score Summary
print("Quiz Complete")
print("You scored", score, "out of 13.")

if score == 13:
    print("Excellent! Full marks.")
elif score >= 10:
    print("Great job!")
elif score >= 6:
    print("Good effort. Keep learning.")
else:
    print("Try again. Practice makes perfect.")

