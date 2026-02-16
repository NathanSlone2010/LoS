import time
import random
import sys
import os
import platform
import pygame
#These are the basic module needs.


#MESSAGE TO iOS USERS! REMOVE PYGAME AND AUDIO-RELATED STUFF IF YOU WANT TO USE THE UPDATED VERSIONS!

audio_file = "You_or_Her?.mp3"
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play(-1)
#This allows the audio to play. Change the directory to your needs (recommend audio file to be in your HOME file)


os_type = platform.system()
if os_type == "Windows":
    print("\nOperating System owner: Microsoft | WINDOWS-OS")
elif os_type == "Darwin":
    print("\nOperating System owner: Apple Computer, Inc. | MacOS")
elif os_type == "Linux":
    print("\nOperating System owner: OPEN SOURCE OS | Linux Kernel")
elif os_type in ["FreeBSD", "OpenBSD", "NetBSD"]:
    print("\nOperating System owner: OPEN SOURCE OS | BSD")
else:
    print("\nUNKNOWN OPERATING SYSTEM DETECTED... PROGRAM MAY NOT RUN AS EFFIECIENTLY")
#This gives recognition of OS. This is more or less a test of my own capabilities. Feel free to remove!


cylinder_size = 6
odds = 2 / cylinder_size
#Must do prize + prize_count below for additive prize
prize = 100000
pcount = 2
#pcf means prize counter final, used as a final number if the combined prize and pcount.
#These all make the game functional. Too many to go in-depth with.


time.sleep(0.5); print("\nAmerican Roulette")
time.sleep(0.5); print("Parent Game: Life of Sorrows")
time.sleep(1); print("\nThe second game of Nathan T.S [Tiktok: void_developers]")
time.sleep(1.5); print("Date of Production: February 15th, 2026 [3:37PM]")
time.sleep(1.5); print(" GitHub Account: NathanSlone2010")
time.sleep(1.5); print("  VERS. 2.01.00")
time.sleep(1.5); print("   RATING: 14+")
print("\nTO ACCESS GAME HISTORY LOGS: LOG")
time.sleep(1.2); print("Don't forget... The winning prize is one-hundred thousand dollars per round survived...")
print("Shooting your opponent, even if they live or die, will not boost your prize count...")
print("\n\nThe REVOLVERS lay in front of you...")
#standard introduction.


while True:
    print("The CYLINDER SPINS...\n")
    time.sleep(1); print("1. Shoot yourself...")
    time.sleep(1.5); print("2. Shoot the Opponent....")
    choice = input(">>> ")


    bullet = random.randint(1, cylinder_size)
    position = random.randint(1, cylinder_size)
    #Randomize the bullet each turn.


    if choice == "1":
        print("You shoot yourself...")
        if random.random() < odds:
            time.sleep(2); print("The gun goes off.......")
            time.sleep(1.5); print("...Player 1 loses..")
            print("Player 1 prize goes to player 2")
            break
        else:
            pcf = prize * pcount
            time.sleep(0.3); print("Click... You survive. \n")
            print(f"PRIZE COUNT: {pcf}")
            prize += 100000

    if choice == "2":
        time.sleep(0.5); print("You point it at your opponent...\n")
        if random.random() < odds:
            time.sleep(1); print("Opponent survives...\n")
        else:
            print("The gun fires... The opponent slumps in their chair...")
            time.sleep(1.2); print("You survived.")

    if choice not in ["1", "2", "LOG"]:
            print("You did not even make a choice... MAKE ONE OR LOSE YOUR PRIZE.")

    if choice == "LOG":
        print("WARNING: RUNNING THIS COMMAND WILL STOP THE PROGRAM.")
        time.sleep(2); print(" 1.0.0: Added the core code | 2.0.0: Added pygame for audio support. For iOS users, the old version without it will be up still, although outdated [sorry] | 2.1.0: Fixed a bit of the logic fallacies.")
        time.sleep(5); break
