import time
import random
#this is for certain things that are primarily for aesthetics


cylinder_size = 6
count = 0
odds = 4 / cylinder_size
#these all make the game functional. Too many to go in-depth with.


time.sleep(0.5); print("Life of Sorrows")
time.sleep(0.5); print("Predecessor: Nokoribi")
time.sleep(1); print("\nThe first game of Nathan T.S [Tiktok: void_developers]")
time.sleep(1.5); print("Date of Production: February 12th, 2025 [3:53PM]")
time.sleep(1.5); print(" GitHub Account: NathanSlone2010")
time.sleep(1.5); print("  VERS. 3.07.02")
time.sleep(1.5); print("   RATING: 14+")
time.sleep(1.5); print("    This game is the first ever game of production... Enjoy \n")
print("\nThe REVOLVERS lay in front of you...")
#standard introduction


while True:
    print("The CYLINDER SPINS...\n")
    time.sleep(1); print("1. Shoot yourself...")
    time.sleep(1); print("2. Shoot the woman....")
    time.sleep(3); print("3. REVENGE.....")
    choice = input(">>> ")

    # Randomize the bullet each turn
    bullet = random.randint(1, cylinder_size)
    position = random.randint(1, cylinder_size)

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

    if choice == "2":
        time.sleep(0.5); print("You point it at the woman...\n")
        if random.random() < odds:
            print("She survives, tears wells in her eyes...")
        else:
           print("The gun fires... The woman slumps in her chair...")
           time.sleep(1.2); print("You survived, but at what costs...? HOW WILL YOU LIVE WITH YOURSLEF???")
           time.sleep(2.4); print("Come and collect your prize...")
           time.sleep(3); break

    if choice == "3":
        time.sleep(1); print("You face the guard, looking at him with hatred...\n")
        if random.random() < odds:
            print("The gun clicks, clicks, clicks, but doesn't go off... The guard gets angry.....")
            time.sleep(2); print("...They will be missed...")
            time.sleep(1.8); break
        else:
            print("You point the gub at the guard... Click, the gun fires, the guard's body slumps to the ground...")
            time.sleep(1.5); print("YOu saved yourself and the woman... But for how long..?")
            time.sleep(1); break
