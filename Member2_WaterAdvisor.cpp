#include <iostream>
#include <iomanip>
#include <limits>
#include <string>
using namespace std;

// ============================================================
//                    AGRISENSE
//            SMART FARM DECISION ASSISTANT
//             WATER MANAGEMENT ADVISOR
// ============================================================

// -------------------- ASCII ART -----------------------------

void showLogo()
{
    cout << R"(

     ___       ____  ____  ___ ____  _____ _   _ ____  _____
    / _ \     / ___||  _ \|_ _/ ___|| ____| \ | / ___|| ____|
   | | | |    \___ \| |_) || |\___ \|  _| |  \| \___ \|  _|
   | |_| |     ___) |  _ < | | ___) | |___| |\  |___) | |___|
    \___/     |____/|_| \_\___|____/|_____|_| \_|____/|_____|

              S M A R T   F A R M
             D E C I S I O N   A S S I S T A N T

)";
}

void showFarm()
{
    cout << R"(

                         \  |  /
                       `.  *  .'
                    ---   SUN   ---
                       .'  *  `.
                         / | \

                 ___________________
                |                   |
                |    AGRISENSE      |
                |    SMART FARM      |
                |___________________|
                    ||       ||
                    ||       ||
            ________||_______||________
           /                         \
          /   /\      /\      /\      \
         /___/  \____/  \____/  \______\
             ||      ||      ||
             ||      ||      ||
            /  \    /  \    /  \
           /____\  /____\  /____\

)";
}

void showWaterASCII()
{
    cout << R"(

                         .-.
                        (   )
                         `-'
                          |
                          |
                         \|/
                    .-----------.
                   /             \
                  /    WATER      \
                 |   MANAGEMENT    |
                  \    ADVISOR     /
                   \             /
                    '-----------'

)";
}

void showRain()
{
    cout << R"(

              .-""""""""-.
            .'   CLOUD    '.
           /               \
          |                 |
           \               /
            '.___________.'
              |  |  |  |
              |  |  |  |
              |  |  |  |
             /   /   /   /

)";
}

void showSunny()
{
    cout << R"(

                    \  |  /
                  --- SUN ---
                    /  |  \

)";
}

void showCloudy()
{
    cout << R"(

              .--.       .--.
           .-(    ).   .-(    )-.
          (___.__) (___.__)

                  CLOUDY

)";
}

// -------------------- INPUT VALIDATION ----------------------

int getNumber(int minValue, int maxValue)
{
    int choice;

    while (true)
    {
        cout << "\nEnter your choice (" << minValue
             << "-" << maxValue << "): ";

        cin >> choice;

        if (cin.fail())
        {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');

            cout << "\n[!] Invalid input.";
            cout << " Please enter a NUMBER.\n";
        }
        else if (choice < minValue || choice > maxValue)
        {
            cout << "\n[!] Invalid choice.";
            cout << " Please choose between "
                 << minValue << " and " << maxValue << ".\n";
        }
        else
        {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return choice;
        }
    }
}

char getYesNo()
{
    char answer;

    while (true)
    {
        cout << "\nEnter Y or N: ";
        cin >> answer;

        if (answer == 'Y' || answer == 'y' ||
            answer == 'N' || answer == 'n')
        {
            return answer;
        }

        cout << "[!] Invalid input. Please enter Y or N.\n";
    }
}

// -------------------- HEADER -------------------------------

void showSectionHeader(string title)
{
    cout << "\n";
    cout << "============================================================\n";
    cout << "                 " << title << "\n";
    cout << "============================================================\n";
}

// -------------------- SOIL MOISTURE -------------------------

void checkSoilMoisture()
{
    int moisture;

    showSectionHeader("SOIL MOISTURE CHECK");

    cout << "\nSelect the current soil moisture level:\n";
    cout << "1. Very Dry\n";
    cout << "2. Dry\n";
    cout << "3. Moist\n";
    cout << "4. Wet\n";
    cout << "5. Very Wet\n";

    moisture = getNumber(1, 5);

    cout << "\n------------------------------------------------------------\n";

    switch (moisture)
    {
        case 1:
            cout << "Soil Status : VERY DRY\n";
            cout << "Action      : Irrigation is strongly recommended.\n";
            cout << "Tip         : Water slowly to allow proper absorption.\n";
            break;

        case 2:
            cout << "Soil Status : DRY\n";
            cout << "Action      : Moderate irrigation may be required.\n";
            cout << "Tip         : Check the crop before watering.\n";
            break;

        case 3:
            cout << "Soil Status : MOIST\n";
            cout << "Action      : No immediate irrigation required.\n";
            cout << "Tip         : Continue monitoring soil moisture.\n";
            break;

        case 4:
            cout << "Soil Status : WET\n";
            cout << "Action      : Avoid additional irrigation.\n";
            cout << "Tip         : Check drainage to prevent waterlogging.\n";
            break;

        case 5:
            cout << "Soil Status : VERY WET\n";
            cout << "Action      : Stop irrigation immediately.\n";
            cout << "Tip         : Improve drainage and prevent root damage.\n";
            break;
    }

    cout << "------------------------------------------------------------\n";
}

// -------------------- IRRIGATION LEVEL ---------------------

void irrigationLevel()
{
    int level;

    showSectionHeader("IRRIGATION MANAGEMENT");

    cout << "\nSelect your current irrigation condition:\n";
    cout << "1. No irrigation system\n";
    cout << "2. Manual watering\n";
    cout << "3. Sprinkler system\n";
    cout << "4. Drip irrigation\n";
    cout << "5. Automated irrigation\n";

    level = getNumber(1, 5);

    cout << "\n------------------------------------------------------------\n";

    switch (level)
    {
        case 1:
            cout << "System: No irrigation system\n";
            cout << "Advice: Monitor soil moisture manually.\n";
            cout << "Advice: Water crops only when required.\n";
            break;

        case 2:
            cout << "System: Manual watering\n";
            cout << "Advice: Avoid overwatering individual plants.\n";
            cout << "Advice: Water near the root zone.\n";
            break;

        case 3:
            cout << "System: Sprinkler irrigation\n";
            cout << "Advice: Check sprinkler coverage regularly.\n";
            cout << "Advice: Avoid watering during strong wind.\n";
            break;

        case 4:
            cout << "System: Drip irrigation\n";
            cout << "Advice: Check pipes and emitters for blockage.\n";
            cout << "Advice: Maintain suitable water pressure.\n";
            break;

        case 5:
            cout << "System: Automated irrigation\n";
            cout << "Advice: Check timer settings regularly.\n";
            cout << "Advice: Adjust watering according to weather.\n";
            break;
    }

    cout << "------------------------------------------------------------\n";
}

// -------------------- WEATHER RECOMMENDATIONS ---------------

void sunnyAdvice()
{
    showSunny();

    showSectionHeader("SUNNY WEATHER WATER ADVICE");

    cout << "\nWeather Condition : SUNNY\n\n";

    cout << "[+] Recommended Actions\n";
    cout << "    1. Check soil moisture before watering.\n";
    cout << "    2. Provide appropriate irrigation.\n";
    cout << "    3. Water during early morning or evening.\n";
    cout << "    4. Use mulch to reduce evaporation.\n";
    cout << "    5. Monitor plants for signs of water stress.\n";
    cout << "    6. Check irrigation pipes for leaks.\n";
    cout << "    7. Avoid wasting water.\n";

    cout << "\n[-] Avoid\n";
    cout << "    - Excessive watering.\n";
    cout << "    - Watering during the hottest part of the day.\n";
    cout << "    - Ignoring dry soil.\n";
}

void rainyAdvice()
{
    showRain();

    showSectionHeader("RAINY WEATHER WATER ADVICE");

    cout << "\nWeather Condition : RAINY\n\n";

    cout << "[+] Recommended Actions\n";
    cout << "    1. Reduce or stop irrigation if rainfall is sufficient.\n";
    cout << "    2. Check soil moisture before watering.\n";
    cout << "    3. Check drainage channels.\n";
    cout << "    4. Remove blocked drainage paths.\n";
    cout << "    5. Monitor plants for waterlogging.\n";
    cout << "    6. Watch for fungal diseases.\n";
    cout << "    7. Protect young plants from heavy rain.\n";

    cout << "\n[-] Avoid\n";
    cout << "    - Additional watering when soil is saturated.\n";
    cout << "    - Blocked drainage systems.\n";
    cout << "    - Allowing water to remain around plant roots.\n";
}

void cloudyAdvice()
{
    showCloudy();

    showSectionHeader("CLOUDY WEATHER WATER ADVICE");

    cout << "\nWeather Condition : CLOUDY\n\n";

    cout << "[+] Recommended Actions\n";
    cout << "    1. Check soil moisture regularly.\n";
    cout << "    2. Provide moderate irrigation when necessary.\n";
    cout << "    3. Monitor plants for water stress.\n";
    cout << "    4. Check drainage conditions.\n";
    cout << "    5. Adjust watering based on soil moisture.\n";
    cout << "    6. Avoid unnecessary irrigation.\n";

    cout << "\n[-] Avoid\n";
    cout << "    - Following a fixed watering schedule blindly.\n";
    cout << "    - Excessive watering.\n";
}

// -------------------- WEATHER MENU --------------------------

void weatherAdvisor()
{
    int weather;

    while (true)
    {
        showSectionHeader("WEATHER CONDITION");

        cout << "\n";
        cout << "   +-----------------------------+\n";
        cout << "   |       WEATHER MENU          |\n";
        cout << "   +-----------------------------+\n";
        cout << "   | 1. Sunny                   |\n";
        cout << "   | 2. Rainy                   |\n";
        cout << "   | 3. Cloudy                  |\n";
        cout << "   | 4. Back                    |\n";
        cout << "   +-----------------------------+\n";

        weather = getNumber(1, 4);

        if (weather == 1)
        {
            sunnyAdvice();
        }
        else if (weather == 2)
        {
            rainyAdvice();
        }
        else if (weather == 3)
        {
            cloudyAdvice();
        }
        else
        {
            break;
        }

        cout << "\nPress ENTER to continue...";
        cin.get();
    }
}

// -------------------- WATER SAVING TIPS ---------------------

void waterSavingTips()
{
    showSectionHeader("SMART WATER-SAVING TIPS");

    cout << R"(

     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  SAVE WATER - SAVE CROPS
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

       [1] Check soil moisture before watering.

       [2] Water early in the morning or evening.

       [3] Avoid excessive irrigation.

       [4] Check pipes for leaks.

       [5] Keep drainage channels clear.

       [6] Use drip irrigation when possible.

       [7] Collect and reuse rainwater where suitable.

       [8] Use mulch to reduce evaporation.

       [9] Adjust irrigation after rainfall.

       [10] Monitor plants regularly.

     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

)";
}

// -------------------- DRAINAGE CHECK ------------------------

void drainageCheck()
{
    int drainage;

    showSectionHeader("DRAINAGE CHECK");

    cout << "\nSelect drainage condition:\n";
    cout << "1. Good drainage\n";
    cout << "2. Slow drainage\n";
    cout << "3. Poor drainage\n";
    cout << "4. Waterlogged\n";

    drainage = getNumber(1, 4);

    cout << "\n------------------------------------------------------------\n";

    switch (drainage)
    {
        case 1:
            cout << "Drainage Status: GOOD\n";
            cout << "Recommendation: Continue regular monitoring.\n";
            break;

        case 2:
            cout << "Drainage Status: SLOW\n";
            cout << "Recommendation: Check soil and drainage channels.\n";
            cout << "Recommendation: Avoid excessive irrigation.\n";
            break;

        case 3:
            cout << "Drainage Status: POOR\n";
            cout << "Recommendation: Improve drainage before heavy irrigation.\n";
            cout << "Recommendation: Clear blocked drainage channels.\n";
            break;

        case 4:
            cout << "Drainage Status: WATERLOGGED\n";
            cout << "Recommendation: Stop irrigation temporarily.\n";
            cout << "Recommendation: Remove excess water.\n";
            cout << "Recommendation: Improve drainage immediately.\n";
            break;
    }

    cout << "------------------------------------------------------------\n";
}

// -------------------- FULL WATER ADVISOR --------------------

void waterManagementAdvisor()
{
    int choice;

    showLogo();
    showFarm();
    showWaterASCII();

    while (true)
    {
        showSectionHeader("WATER MANAGEMENT ADVISOR");

        cout << "\n";
        cout << "       +--------------------------------+\n";
        cout << "       |       WATER MANAGEMENT         |\n";
        cout << "       +--------------------------------+\n";
        cout << "       | 1. Weather Advisor             |\n";
        cout << "       | 2. Soil Moisture Check         |\n";
        cout << "       | 3. Irrigation Management       |\n";
        cout << "       | 4. Drainage Check              |\n";
        cout << "       | 5. Water-Saving Tips           |\n";
        cout << "       | 6. Exit Water Advisor          |\n";
        cout << "       +--------------------------------+\n";

        choice = getNumber(1, 6);

        switch (choice)
        {
            case 1:
                weatherAdvisor();
                break;

            case 2:
                checkSoilMoisture();
                break;

            case 3:
                irrigationLevel();
                break;

            case 4:
                drainageCheck();
                break;

            case 5:
                waterSavingTips();
                break;

            case 6:
                cout << "\n";
                cout << "============================================================\n";
                cout << "       Returning to AgriSense Main Menu...\n";
                cout << "       Thank you for using Water Management Advisor!\n";
                cout << "============================================================\n";
                return;
        }

        cout << "\nPress ENTER to return to the Water Management menu...";
        cin.get();
    }
}

// -------------------- MAIN FUNCTION -------------------------

int main()
{
    waterManagementAdvisor();

    return 0;
}