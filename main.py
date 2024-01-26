import random

def roll():
    dice_number = random.randint(1, 6)
    return dice_number

def main():
    while True:
        input_phrase = input("Enter 'Roll' for random DICE number:")
        if input_phrase.lower() == "roll":
            dice_number = roll()
            if dice_number == 1:
                print("One. LOL")
            elif dice_number == 2:
                print("Two. Welp...")
            elif dice_number == 3:
                print("Three. Middle of nowhere")
            elif dice_number == 4:
                print("Four. Eeeek")
            elif dice_number == 5:
                print("Five. Close Call")
            elif dice_number == 6:
                print("SIX. LUCKYY?")
        elif input_phrase.lower() == "quit":
            break
        else:
            print("Invalid input. Please enter 'Roll Dice' to generate a random dice number or 'Quit' to exit.")

if __name__ == "__main__":
    main()