import time
import random
import sys
import os
import pygame
import platform
#These are the basic module needs.
#Manual installation of pygame is needed.


audio_file = "Darkness.mp3"
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play(-1)
#This allows the audio to play. Change the directory to your needs (recommend audio file to be in your HOME file)


print("\033[91mNO ERRORS RETURNED\033[0m")
#If users see this, it means there are no errors.

os_type = platform.system()
if os_type == "Windows":
    print("\033[1;31mOperating System owner: Microsoft | WINDOWS-OS\033[0m")
elif os_type == "Darwin":
    print("\033[1;31mOperating System owner: Apple Computer, Inc. | MacOS\033[0m")
elif os_type == "Linux":
    print("\033[1;31mOperating System owner: OPEN SOURCE OS | Linux Kernel\033[0m")
elif os_type in ["FreeBSD", "OpenBSD", "NetBSD"]:
    print("\033[1;31mOperating System owner: OPEN SOURCE OS | BSD\033[0m")
elif os_type == "iOS":
    print("\033[1;31mOperating System owner: Apple Computer, Inc. | iOS\033[0m")
else:
   print("\n\033[91mUNKNOWN OPERATING SYSTEM DETECTED... PROGRAM MAY NOT RUN AS EFFIECIENTLY\033[m")
#This gives recogntion of OS. This is more or so a test of my own capabilities. Feel free to remove!


cylinder_size = 6
odds = 4 / cylinder_size #Change this when developing the game.
days = 0
count = 0
#these all make the game functional. Too many to go in-depth with.


time.sleep(0.5); print("\nLife of Sorrows")
time.sleep(0.5); print("Predecessor: Nokoribi")
time.sleep(1); print("\nThe first game of Nathan T.S [Tiktok: void_developers]")
time.sleep(1.5); print("Date of Production: February 12th, 2026 [3:53PM]")
time.sleep(1.5); print(" GitHub Account: NathanSlone2010")
time.sleep(1.5); print("  VERS. 5.10.4")
time.sleep(1.5); print("   RATING: 14+")
time.sleep(1.5); print("    This game is the first ever game of production... Enjoy \n")
print("TO ACCESS GAME HISTORY LOGS: LOG")
print("\nThe REVOLVERS lay in front of you...")
#standard introduction.



try:
    while True:
        con = input("Press E to continue: ")
        if con in ["E", "e"]:
            break
        print("PRESS E")
    while True:
        print("\nThe CYLINDER SPINS...\n")
        time.sleep(1); print("1. Shoot yourself...")
        time.sleep(1.5); print("2. Shoot the woman....")
        time.sleep(2); print("3. REVENGE.....")
        choice = input(">>> ")

        bullet = random.randint(1, cylinder_size)
        position = random.randint(1, cylinder_size)
        # Randomize the bullet each turn.

        if choice == "1":
            print("You shoot yourself...")
            if random.random() < odds:
                time.sleep(2); print("The gun goes off.......")
                time.sleep(1.5); print("...They will be missed..")
                break
            else:
                count += 1
                time.sleep(0.3); print("Click... You survive. \n")
                print("Collect your survival prize...")
                print(f"DAYS: {days}")

        if choice == "2":
            time.sleep(0.5); print("You point it at the woman...\n")
            days += 1
            if random.random() < odds:
                time.sleep(1); print("She survives, tears wells in her eyes...\n")
                time.sleep(0.5); print(f"DAYS: {days}")
            else:
                time.sleep(1); print("PLease... no.. I have a child..!\n")
                print("The gun fires... The woman slumps in her chair...")
                time.sleep(1.2); print("You survived, but at what costs...? HOW WILL YOU LIVE WITH YOURSLEF???")
                time.sleep(2.4); print("\n\nCome and collect your prize...")
                time.sleep(3); break

        if choice == "3":
            time.sleep(1); print("You face the guard, looking at him with hatred...\n")
            if random.random() < odds:
                print("The gun clicks, clicks, clicks, but doesn't go off... The guard gets angry.....")
                time.sleep(2); print("...They will be missed...")
                time.sleep(1.8); break
            else:
                print("You point the gun at the guard... Click, the gun fires, the guard's body slumps to the ground...")
                time.sleep(1.5); print("You saved yourself and the woman... But for how long..?")
                time.sleep(1); print("DAYS: 216, but then they found you and the woman...")
                time.sleep(1); break

        if choice == "LOG":
            print("WARNING: RUNNING THIS COMMAND WILL STOP THE PROGRAM.")
            time.sleep(2); print(" 3.9.3: Added the LOGS [everything before is lost from LOGS] | 3.10.3: Created iOS-based version if LoS | 4.10.3: Created a way to prevent user-issues | 5.10.3: Added a 'press E to continue' function, meant to make the game more modernised, even if it looks retro | 5.10.4: Tweaked the time dor the choices to appear.")
            time.sleep(5); break

        if choice not in ["1", "2", "3", "LOG"]:
            print("You did not even make a choice... MAKE ONE OR LOSE YOUR PRIZE.")

finally:
    pygame.mixer.music.stop()
# stop music on exit.
