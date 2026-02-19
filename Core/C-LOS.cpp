#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>
#include <ctime>
#include <string>

#ifdef _WIN32
    #define OS "Windows"
#elif __APPLE__
    #define OS "MacOS"
#elif __linux__
    #define OS "Linux"
#else
    #define OS "Unknown"
#endif

using namespace std;

// Function to mimic Python's time.sleep()
void sleep_seconds(double seconds) {
    this_thread::sleep_for(chrono::milliseconds(int(seconds * 1000)));
}

// Function to generate random float between 0 and 1
double random_float() {
    return static_cast<double>(rand()) / RAND_MAX;
}

// Function to generate random integer in range [min, max]
int random_int(int min, int max) {
    return rand() % (max - min + 1) + min;
}

int main() {
    srand(static_cast<unsigned int>(time(nullptr)));

    // Placeholder for audio playback
    string audio_file = "Sic_Bo.mp3";
    // In C++ you would use a library like SDL_mixer, SFML, or irrKlang to play audio
    cout << "[Audio playback: " << audio_file << "]" << endl;

    // Detect OS
    if (OS == string("Windows"))
        cout << "\nOperating System owner: Microsoft | WINDOWS-OS" << endl;
    else if (OS == string("MacOS"))
        cout << "\nOperating System owner: Apple Computer, Inc. | MacOS" << endl;
    else if (OS == string("Linux"))
        cout << "\nOperating System owner: OPEN SOURCE OS | Linux Kernel" << endl;
    else
        cout << "\nUNKNOWN OPERATING SYSTEM DETECTED... PROGRAM MAY NOT RUN AS EFFICIENTLY" << endl;

    int cylinder_size = 6;
    double odds = 4.0 / cylinder_size;
    int days = 0;
    int count = 0;

    sleep_seconds(0.5); cout << "\nLife of Sorrows" << endl;
    sleep_seconds(0.5); cout << "Predecessor: Nokoribi" << endl;
    sleep_seconds(1); cout << "\nThe first game of Nathan T.S [Tiktok: void_developers]" << endl;
    sleep_seconds(1.5); cout << "Date of Production: February 12th, 2026 [3:53PM]" << endl;
    sleep_seconds(1.5); cout << " GitHub Account: NathanSlone2010" << endl;
    sleep_seconds(1.5); cout << "  VERS. 5.10.3" << endl;
    sleep_seconds(1.5); cout << "   RATING: 14+" << endl;
    sleep_seconds(1.5); cout << "    This game is the first ever game of production... Enjoy \n" << endl;
    cout << "TO ACCESS GAME HISTORY LOGS: LOG" << endl;
    cout << "\nThe REVOLVERS lay in front of you..." << endl;

    string con;
    while (true) {
        cout << "Press E to continue: ";
        getline(cin, con);
        if (con == "E" || con == "e") break;
        cout << "PRESS E" << endl;
    }

    try {
        while (true) {
            cout << "\nThe CYLINDER SPINS...\n" << endl;
            sleep_seconds(1); cout << "1. Shoot yourself..." << endl;
            sleep_seconds(1.5); cout << "2. Shoot the woman...." << endl;
            sleep_seconds(3); cout << "3. REVENGE....." << endl;
            cout << ">>> ";
            string choice;
            getline(cin, choice);

            int bullet = random_int(1, cylinder_size);
            int position = random_int(1, cylinder_size);

            if (choice == "1") {
                cout << "You shoot yourself..." << endl;
                if (random_float() < odds) {
                    sleep_seconds(2); cout << "The gun goes off......." << endl;
                    sleep_seconds(1.5); cout << "...They will be missed.." << endl;
                    break;
                } else {
                    count++;
                    sleep_seconds(0.3); cout << "Click... You survive. \n" << endl;
                    cout << "Collect your survival prize..." << endl;
                    cout << "DAYS: " << days << endl;
                }
            } else if (choice == "2") {
                sleep_seconds(0.5); cout << "You point it at the woman...\n" << endl;
                days++;
                if (random_float() < odds) {
                    sleep_seconds(1); cout << "She survives, tears wells in her eyes...\n" << endl;
                    sleep_seconds(0.5); cout << "DAYS: " << days << endl;
                } else {
                    sleep_seconds(1); cout << "Please... no.. I have a child..!\n";
                    cout << "The gun fires... The woman slumps in her chair..." << endl;
                    sleep_seconds(1.2); cout << "You survived, but at what costs...? HOW WILL YOU LIVE WITH YOURSELF???" << endl;
                    sleep_seconds(2.4); cout << "\n\nCome and collect your prize..." << endl;
                    sleep_seconds(3); break;
                }
            } else if (choice == "3") {
                sleep_seconds(1); cout << "You face the guard, looking at him with hatred...\n" << endl;
                if (random_float() < odds) {
                    cout << "The gun clicks, clicks, clicks, but doesn't go off... The guard gets angry....." << endl;
                    sleep_seconds(2); cout << "...They will be missed..." << endl;
                    sleep_seconds(1.8); break;
                } else {
                    cout << "You point the gun at the guard... Click, the gun fires, the guard's body slumps to the ground..." << endl;
                    sleep_seconds(1.5); cout << "You saved yourself and the woman... But for how long..?" << endl;
                    sleep_seconds(1); cout << "DAYS: 216, but then they found you and the woman..." << endl;
                    sleep_seconds(1); break;
                }
            } else if (choice == "LOG") {
                cout << "WARNING: RUNNING THIS COMMAND WILL STOP THE PROGRAM." << endl;
                sleep_seconds(2);
                cout << " 3.9.3: Added the LOGS [everything before is lost from LOGS] | 3.10.3: Created iOS-based version if LoS | 4.10.3: Created a way to prevent user-issues | 5.10.3: Added a 'press E to continue' function, meant to make the game more modernised, even if it looks retro." << endl;
                sleep_seconds(5);
                break;
            } else {
                cout << "You did not even make a choice... MAKE ONE OR LOSE YOUR PRIZE." << endl;
            }
        }
    } catch (...) {
        // In Python you stop the music in finally
        cout << "[Music stopped]" << endl;
    }

    return 0;
}