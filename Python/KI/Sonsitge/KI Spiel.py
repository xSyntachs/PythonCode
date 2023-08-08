import random

def play_game():
    print("Willkommen zum Zahlenraten-Spiel!")
    print("In diesem Spiel kannst du abwechselnd raten, welche Zahl die KI sich ausdenkt,")
    print("und die KI wird versuchen, zu erraten, welche Zahl du dir ausdenkst.")

    while True:
        # Part 1: Die KI wählt eine Zahl aus und der Spieler muss raten
        print("\n--- Part 1: Die KI denkt sich eine Zahl aus ---")
        target_number = random.randint(1, 100)
        attempts = 0

        while True:
            attempts += 1
            guess = int(input("Rate eine Zahl zwischen 1 und 100: "))

            if guess < target_number:
                print("Zu niedrig! Versuche es erneut.")
            elif guess > target_number:
                print("Zu hoch! Versuche es erneut.")
            else:
                print(f"Herzlichen Glückwunsch! Du hast die Zahl {target_number} erraten!")
                print(f"Du hast {attempts} Versuche gebraucht.")
                break

        # Part 2: Der Spieler wählt eine Zahl aus und die KI versucht zu raten
        print("\n--- Part 2: Du denkst dir eine Zahl aus ---")
        low = 1
        high = 100
        attempts = 0

        while True:
            attempts += 1
            guess = random.randint(low, high)
            print(f"Schätzung der KI: {guess}")

            user_input = input("Ist die Zahl höher (h), niedriger (n) oder korrekt (k)? ").lower()

            if user_input == 'k':
                print(f"Die KI hat deine Zahl {guess} nach {attempts} Versuchen erraten!")
                break
            elif user_input == 'h':
                low = guess + 1
            elif user_input == 'n':
                high = guess - 1
            else:
                print("Ungültige Eingabe! Bitte antworte mit 'h', 'n' oder 'k'.")

        play_again = input("Möchtest du nochmal spielen? (Antworte mit 'ja' oder 'nein'): ").lower()
        if play_again != 'ja':
            break

if __name__ == "__main__":
    play_game()
