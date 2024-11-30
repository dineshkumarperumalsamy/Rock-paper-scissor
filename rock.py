import random
import os
def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For macOS/Linux
guess = ["ROCK", "PAPER", "SCISSOR"]
iw = input("Enter your Choice: ")
iw = iw.upper()
scorep =0
scoren=0
def checkinput(ip):
    gc = random.choice(guess)
    global scorep
    global scoren
    if ip in guess:
        print(f"The system's input is: {gc}")

        if gc == "ROCK":
            if ip == gc:
                print("It's a Draw....Wanna try again?")
                print(f"\nYOUR SCORE {scoren} \nPC SCORE {scorep}")
                print("TYPE 1 - EXIT")
                print("TYPE 2 - CONTINUE")
                try:
                    ri = int(input("Choice: "))
                    if ri == 1:
                        clear_screen()
                        print("Thanks for playing the game!")
                    elif ri == 2:
                        clear_screen()
                        print("That's the spirit! Come on, let's play again.")
                        ip = input("Enter your Choice: ").upper()
                        checkinput(ip)
                    else:
                        print("Please enter 1 or 2.")
                except ValueError:
                    clear_screen()
                    print("Invalid input. Please enter 1 or 2.")
                    checkinput(ip)
            elif ip == "PAPER":
                print("\nCongrats! You won the game")
                scoren=scoren+1
                print(f"\nYOUR SCORE {scoren} \nPC SCORE {scorep}")
                print("TYPE 1 - EXIT")
                print("TYPE 2 - CONTINUE")
                try:
                    ri = int(input("Choice: "))
                    if ri == 1:
                        clear_screen()
                        print("Thanks for playing the game!")
                    elif ri == 2:
                        clear_screen()
                        print("That's the spirit! Come on, let's play again.")
                        ip = input("Enter your Choice: ").upper()
                        checkinput(ip)
                    else:
                        print("Please enter 1 or 2.")
                except ValueError:
                    clear_screen()
                    print("Invalid input. Please enter 1 or 2.")
                    checkinput(ip)
            else:
                print("\nSorry, you lost the game.")
                scorep=scorep+1
                print(f"\nYOUR SCORE {scoren} \nPC SCORE {scorep}")
                print("TYPE 1 - EXIT")
                print("TYPE 2 - CONTINUE")
                try:
                    ri = int(input("Choice: "))
                    if ri == 1:
                        clear_screen()
                        print("Haha, Hi Coward! It's nice meeting you.")
                    elif ri == 2:
                        clear_screen()
                        print("Wanna see another loss? Come on, let's play again.")
                        ip = input("Enter your Choice: ").upper()
                        checkinput(ip)
                    else:
                        print("Please enter 1 or 2.")
                except ValueError:
                    clear_screen()
                    print("Invalid input. Please enter 1 or 2.")
                    checkinput(ip)

        elif gc == "PAPER":
            if ip == gc:
                print("It's a Draw....Wanna try again?")
                print(f"\nYOUR SCORE {scoren} \nPC SCORE {scorep}")
                print("TYPE 1 - EXIT")
                print("TYPE 2 - CONTINUE")
                try:
                    ri = int(input("Choice: "))
                    if ri == 1:
                        clear_screen()
                        print("Thanks for playing the game!")
                    elif ri == 2:
                        clear_screen()
                        print("That's the spirit! Come on, let's play again.")
                        ip = input("Enter your Choice: ").upper()
                        checkinput(ip)
                    else:
                        clear_screen()
                        print("Please enter 1 or 2.")
                except ValueError:
                    clear_screen()
                    print("Invalid input. Please enter 1 or 2.")
                    checkinput(ip)
            elif ip == "SCISSOR":
                print("\nCongrats! You won the game")
                scoren=scoren+1
                print(f"\nYOUR SCORE {scoren} \nPC SCORE {scorep}")
                print("TYPE 1 - EXIT")
                print("TYPE 2 - CONTINUE")
                try:
                    ri = int(input("Choice: "))
                    if ri == 1:
                        clear_screen()
                        print("Thanks for playing the game!")
                    elif ri == 2:
                        clear_screen()
                        print("That's the spirit! Come on, let's play again.")
                        ip = input("Enter your Choice: ").upper()
                        checkinput(ip)
                    else:
                        clear_screen()
                        print("Please enter 1 or 2.")
                except ValueError:
                    clear_screen()
                    print("Invalid input. Please enter 1 or 2.")
                    checkinput(ip)
            else:
                print("\nSorry, you lost the game.")
                scorep=scorep+1
                print(f"\nYOUR SCORE {scoren} \nPC SCORE {scorep}")
                print("TYPE 1 - EXIT")
                print("TYPE 2 - CONTINUE")
                try:
                    ri = int(input("Choice: "))
                    if ri == 1:
                        clear_screen()
                        print("Haha, Hi Coward! It's nice meeting you.")
                    elif ri == 2:
                        clear_screen()
                        print("Wanna see another loss? Come on, let's play again.")
                        ip = input("Enter your Choice: ").upper()
                        checkinput(ip)
                    else:
                        clear_screen()
                        print("Please enter 1 or 2.")
                except ValueError:
                    clear_screen()
                    print("Invalid input. Please enter 1 or 2.")
                    checkinput(ip)

        elif gc == "SCISSOR":
            if ip == gc:
                print("It's a Draw....Wanna try again?")
                print(f"\nYOUR SCORE {scoren} \nPC SCORE {scorep}")
                print("TYPE 1 - EXIT")
                print("TYPE 2 - CONTINUE")
                try:
                    ri = int(input("Choice: "))
                    if ri == 1:
                        clear_screen()
                        print("Thanks for playing the game!")
                    elif ri == 2:
                        clear_screen()
                        print("That's the spirit! Come on, let's play again.")
                        ip = input("Enter your Choice: ").upper()
                        checkinput(ip)
                    else:
                        clear_screen()
                        print("Please enter 1 or 2.")
                except ValueError:
                    clear_screen()
                    print("Invalid input. Please enter 1 or 2.")
                    checkinput(ip)
            elif ip == "ROCK":
                print("\nCongrats! You won the game")
                scoren=scoren+1
                print(f"\nYOUR SCORE {scoren} \nPC SCORE {scorep}")
                print("TYPE 1 - EXIT")
                print("TYPE 2 - CONTINUE")
                try:
                    ri = int(input("Choice: "))
                    if ri == 1:
                        clear_screen()
                        print("Thanks for playing the game!")
                    elif ri == 2:
                        clear_screen()
                        print("That's the spirit! Come on, let's play again.")
                        ip = input("Enter your Choice: ").upper()
                        checkinput(ip)
                    else:
                        clear_screen()
                        print("Please enter 1 or 2.")
                except ValueError:
                    clear_screen()
                    print("Invalid input. Please enter 1 or 2.")
                    checkinput(ip)
            else:
                print("\nSorry, you lost the game.")
                scorep=scorep+1
                print(f"\nYOUR SCORE {scoren} \nPC SCORE {scorep}")
                print("TYPE 1 - EXIT")
                print("TYPE 2 - CONTINUE")
                try:
                    ri = int(input("Choice: "))
                    if ri == 1:
                        clear_screen()
                        print("Haha, Hi Coward! It's nice meeting you.")
                    elif ri == 2:
                        clear_screen()
                        print("Wanna see another loss? Come on, let's play again.")
                        ip = input("Enter your Choice: ").upper()
                        checkinput(ip)
                    else:
                        clear_screen()
                        print("Please enter 1 or 2.")
                except ValueError:
                    clear_screen()
                    print("Invalid input. Please enter 1 or 2.")
                    checkinput(ip)

    else:
        print("Please enter ROCK, PAPER, or SCISSOR.")
        ip = input("Try again: ").upper()
        checkinput(ip)
checkinput(iw)