

secret_Word = "Word"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_Word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter Your Guess: ")
        guess_count += 1

    else:
        out_of_guess = True

if out_of_guess:
    print("Out of Guesses! You Loss!")

else:
    print("Yooo...You win!")