import time
import random
#this is for certain things that are primarily for aesthetics, though random is fully needed.


cylinder_size = 6
odds = 4 / cylinder_size
days = 0
#these all make the game functional. Too many to go in-depth with.


time.sleep(0.5); print("Life of Sorrows")
time.sleep(0.5); print("Predecessor: Nokoribi")
time.sleep(1); print("\nThe first game of Nathan T.S [Tiktok: void_developers]")
time.sleep(1.5); print("Date of Production: February 12th, 2025 [3:53PM]")
time.sleep(1.5); print(" GitHub Account: NathanSlone2010")
time.sleep(1.5); print("  VERS. 3.08.03")
time.sleep(1.5); print("   RATING: 14+")
time.sleep(1.5); print("    This game is the first ever game of production... Enjoy \n")
print("TO ACCESS GAME HISTORY LOGS: LOG")
print("\nThe REVOLVERS lay in front of you...")
#standard introduction.


while True:
    print("The CYLINDER SPINS...\n")
    time.sleep(1); print("1. Shoot yourself...")
    time.sleep(1.5); print("2. Shoot the woman....")
    time.sleep(3); print("3. REVENGE.....")
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
            print("You point the gub at the guard... Click, the gun fires, the guard's body slumps to the ground...")
            time.sleep(1.5); print("You saved yourself and the woman... But for how long..?")
            time.sleep(1); print("DAYS: 216, but then they found you and the woman...")
            time.sleep(1); break
        
    if choice == "LOG":
        print("WARNING: RUNNING THIS COMMAND WILL STOP THE PROGRAM.")
        time.sleep(2); print(" 3.9.03: Added the LOGS [evething before is lost from LOGS]")
        time.sleep(5); break
#this is the actual game itself
