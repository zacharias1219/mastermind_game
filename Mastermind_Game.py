import random

COLORS = ["R","G","B","Y","W","O"]
TRIES = 10
CODE_LENGTH = 4

def generateCode():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    
    return code

def guessCode():
    while True:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try Again!!")
                break
        else:
            break
    return guess

def checkCode(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess,real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -=1

    for guess_color, real_color in zip(guess,real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code...")
    print(f"The valid colors are {COLORS}")
    code = generateCode()
    for attempts in range(1,TRIES+1):
        guess = guessCode()
        correct_pos, incorrect_pos = checkCode(guess, code)
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print(f"You ran out of tries, the code was: {code}")

if __name__ == "__main__":
    game()