# mini_project1
# vista shahbazi
# 404130873

import random

#نمایش اطلاعات برنامه نویس در صفحه ی اصلی 
def programmer_info():
    print("programer : vista shahbazi")
    print("student iD : 404130873")


#تولید رمز تصادفی چهار رقمی بدون تکرار توسط برنامه 
def generate_secret_code():
    secret_code = ""

    while len(secret_code) < 4:
        digit = str(random.randrange(1, 7))

        if digit not in secret_code:
            secret_code += digit

    return secret_code


# بررسی معتبر بودن حدس بازیکن
def is_valid_guess(guess):

    if len(guess) != 4:
        return False

    for digit in guess:
        if digit not in "123456":
            return False

    for i in range(4):
        for j in range(i + 1, 4):
            if guess[i] == guess[j]:
                return False

    return True


# مقایسه حدس بازیکن با رمز مخفی
def check_guess(secret_code, guess):
    correct_place = 0
    wrong_place = 0

    for i in range(4):

        if guess[i] == secret_code[i]:
            correct_place += 1

        elif guess[i] in secret_code:
            wrong_place += 1

    return correct_place, wrong_place


# اجرای بازی
def play_game():
    secret_code = generate_secret_code()
    attempts = 0
    max_attempts = 10

    print("the secret code has 4 different numbers from 1 to 6 ")
    print("you have 10 chances to guess the code ")

    while attempts < max_attempts:

        guess = input("enter your guess :")

        # بررسی اعتبار ورودی
        if not is_valid_guess(guess):
            print("invalid input!")
            print("please enter 4 diffirent number from 1 to 6")
            continue

        attempts += 1

        # مقایسه حدس با رمز مخفی
        correct_place, wrong_place = check_guess(
            secret_code, guess
        )

        print("number of correct digits in the correct position : ", correct_place)
        print("number of correct digits in the wrong position : ", wrong_place)
        print("number of remaining guesses : ", max_attempts - attempts)

        # بررسی برنده شدن بازیکن
        if correct_place == 4:
            print("you win!")
            print("number of your trys :", attempts)
            return

    # پایان بازی در صورت تمام شدن فرصت ها
    print("your chances have run out!")
    print("you lost!")
    print("the secret code was this :", secret_code)


# شروع برنامه
programmer_info()
play_game()