#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#ifdef _WIN32
#include <windows.h>
#define SLEEP(sec) Sleep(sec * 1000)
#else
#include <unistd.h>
#define SLEEP(sec) sleep(sec)
#endif

int main() {
    srand(time(NULL));  // seed random number generator

    int cylinder_size = 6;
    double odds = 4.0 / cylinder_size;
    int days = 0;
    int count = 0;
    char choice[10];

    // OS detection
#ifdef _WIN32
    printf("\nOperating System owner: Microsoft | WINDOWS-OS\n");
#elif __APPLE__
    printf("\nOperating System owner: Apple Computer, Inc. | MacOS\n");
#elif __linux__
    printf("\nOperating System owner: OPEN SOURCE OS | Linux Kernel\n");
#elif __FreeBSD__ || __OpenBSD__ || __NetBSD__
    printf("\nOperating System owner: OPEN SOURCE OS | BSD\n");
#else
    printf("\nUNKNOWN OPERATING SYSTEM DETECTED... PROGRAM MAY NOT RUN AS EFFICIENTLY\n");
#endif

    // Intro
    SLEEP(1);
    printf("\nLife of Sorrows\n");
    SLEEP(1);
    printf("Predecessor: Nokoribi\n");
    SLEEP(1);
    printf("\nThe first game of Nathan T.S [Tiktok: void_developers]\n");
    SLEEP(1);
    printf("Date of Production: February 12th, 2026 [3:53PM]\n");
    SLEEP(1);
    printf("GitHub Account: NathanSlone2010\n");
    SLEEP(1);
    printf("VERS. 5.10.3\n");
    SLEEP(1);
    printf("RATING: 14+\n");
    SLEEP(1);
    printf("This game is the first ever game of production... Enjoy\n");
    printf("TO ACCESS GAME HISTORY LOGS: LOG\n");
    printf("\nThe REVOLVERS lay in front of you...\n");

    // Press E to continue
    while (1) {
        printf("Press E to continue: ");
        scanf("%s", choice);
        if (strcmp(choice, "E") == 0 || strcmp(choice, "e") == 0)
            break;
        printf("PRESS E\n");
    }

    // Main game loop
    while (1) {
        printf("\nThe CYLINDER SPINS...\n");
        SLEEP(1);
        printf("1. Shoot yourself...\n");
        SLEEP(1);
        printf("2. Shoot the woman....\n");
        SLEEP(1);
        printf("3. REVENGE.....\n");
        printf(">>> ");
        scanf("%s", choice);

        int bullet = rand() % cylinder_size + 1;
        int position = rand() % cylinder_size + 1;
        double rand_prob = (double)rand() / RAND_MAX;

        if (strcmp(choice, "1") == 0) {
            printf("You shoot yourself...\n");
            if (rand_prob < odds) {
                SLEEP(2);
                printf("The gun goes off.......\n");
                SLEEP(1);
                printf("...They will be missed..\n");
                break;
            } else {
                count++;
                SLEEP(0.3);
                printf("Click... You survive. \n");
                printf("Collect your survival prize...\n");
                printf("DAYS: %d\n", days);
            }
        } else if (strcmp(choice, "2") == 0) {
            SLEEP(1);
            printf("You point it at the woman...\n");
            days++;
            if (rand_prob < odds) {
                SLEEP(1);
                printf("She survives, tears wells in her eyes...\n");
                printf("DAYS: %d\n", days);
            } else {
                SLEEP(1);
                printf("Please... no.. I have a child..!\n");
                printf("The gun fires... The woman slumps in her chair...\n");
                SLEEP(1);
                printf("You survived, but at what costs...? HOW WILL YOU LIVE WITH YOURSELF???\n");
                break;
            }
        } else if (strcmp(choice, "3") == 0) {
            SLEEP(1);
            printf("You face the guard, looking at him with hatred...\n");
            if (rand_prob < odds) {
                printf("The gun clicks, clicks, clicks, but doesn't go off... The guard gets angry.....\n");
                SLEEP(2);
                printf("...They will be missed...\n");
                break;
            } else {
                printf("You point the gun at the guard... Click, the gun fires, the guard's body slumps to the ground...\n");
                SLEEP(1);
                printf("You saved yourself and the woman... But for how long..?\n");
                SLEEP(1);
                printf("DAYS: 216, but then they found you and the woman...\n");
                break;
            }
        } else if (strcmp(choice, "LOG") == 0) {
            printf("WARNING: RUNNING THIS COMMAND WILL STOP THE PROGRAM.\n");
            SLEEP(2);
            printf("3.9.3: Added the LOGS [everything before is lost from LOGS]\n3.10.3: Created iOS-based version of LoS\n4.10.3: Created a way to prevent user-issues\n5.10.3: Added a 'press E to continue' function\n");
            SLEEP(5);
            break;
        } else {
            printf("You did not even make a choice... MAKE ONE OR LOSE YOUR PRIZE.\n");
        }
    }

    return 0;
}