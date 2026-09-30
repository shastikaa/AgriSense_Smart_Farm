# ============================================================
#                    AGRISENSE
#            SMART FARM DECISION ASSISTANT
#             WATER MANAGEMENT ADVISOR
# ============================================================

import os


# -------------------- SCREEN CLEAR ---------------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# -------------------- ASCII ART ------------------------------

def show_logo():
    print(r"""

     _     ____ ____  ___ ____  _____ _   _ ____  _____
    / \   / ___|  _ \|_ _/ ___|| ____| \ | / ___|| ____|
   / _ \ | |  _| |_) || |\___ \|  _| |  \| \___ \|  _|
  / ___ \| |_| |  _ < | | ___) | |___| |\  |___) | |___|
 /_/   \_\____|_| \_\___|____/|_____|_| \_|____/ |_____|

              S M A R T   F A R M
             D E C I S I O N   A S S I S T A N T

""")


def show_farm():
    print(r"""

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

""")


def show_water_ascii():
    print(r"""

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

""")


def show_rain():
    print(r"""

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

""")


def show_sunny():
    print(r"""

                    \  |  /
                  --- SUN ---
                    /  |  \

""")


def show_cloudy():
    print(r"""

              .--.       .--.
           .-(    ).   .-(    )-.
          (___.__) (___.__)

                  CLOUDY

""")


# -------------------- INPUT VALIDATION -----------------------

def get_number(min_value, max_value):

    while True:
        try:
            choice = int(
                input(f"\nEnter your choice ({min_value}-{max_value}): ")
            )

            if choice < min_value or choice > max_value:
                print(
                    f"\n[!] Invalid choice. "
                    f"Please choose between {min_value} and {max_value}."
                )
            else:
                return choice

        except ValueError:
            print("\n[!] Invalid input. Please enter a NUMBER.")


def get_yes_no():

    while True:
        answer = input("\nEnter Y or N: ").strip()

        if answer.lower() in ["y", "n"]:
            return answer

        print("[!] Invalid input. Please enter Y or N.")


# -------------------- HEADER --------------------------------

def show_section_header(title):

    print("\n")
    print("=" * 60)
    print(f"                 {title}")
    print("=" * 60)


# -------------------- SOIL MOISTURE --------------------------

def check_soil_moisture():

    show_section_header("SOIL MOISTURE CHECK")

    print("\nSelect the current soil moisture level:")
    print("1. Very Dry")
    print("2. Dry")
    print("3. Moist")
    print("4. Wet")
    print("5. Very Wet")

    moisture = get_number(1, 5)

    print("\n" + "-" * 60)

    if moisture == 1:
        print("Soil Status : VERY DRY")
        print("Action      : Irrigation is strongly recommended.")
        print("Tip         : Water slowly to allow proper absorption.")

    elif moisture == 2:
        print("Soil Status : DRY")
        print("Action      : Moderate irrigation may be required.")
        print("Tip         : Check the crop before watering.")

    elif moisture == 3:
        print("Soil Status : MOIST")
        print("Action      : No immediate irrigation required.")
        print("Tip         : Continue monitoring soil moisture.")

    elif moisture == 4:
        print("Soil Status : WET")
        print("Action      : Avoid additional irrigation.")
        print("Tip         : Check drainage to prevent waterlogging.")

    elif moisture == 5:
        print("Soil Status : VERY WET")
        print("Action      : Stop irrigation immediately.")
        print("Tip         : Improve drainage and prevent root damage.")

    print("-" * 60)


# -------------------- IRRIGATION LEVEL -----------------------

def irrigation_level():

    show_section_header("IRRIGATION MANAGEMENT")

    print("\nSelect your current irrigation condition:")
    print("1. No irrigation system")
    print("2. Manual watering")
    print("3. Sprinkler system")
    print("4. Drip irrigation")
    print("5. Automated irrigation")

    level = get_number(1, 5)

    print("\n" + "-" * 60)

    if level == 1:
        print("System: No irrigation system")
        print("Advice: Monitor soil moisture manually.")
        print("Advice: Water crops only when required.")

    elif level == 2:
        print("System: Manual watering")
        print("Advice: Avoid overwatering individual plants.")
        print("Advice: Water near the root zone.")

    elif level == 3:
        print("System: Sprinkler irrigation")
        print("Advice: Check sprinkler coverage regularly.")
        print("Advice: Avoid watering during strong wind.")

    elif level == 4:
        print("System: Drip irrigation")
        print("Advice: Check pipes and emitters for blockage.")
        print("Advice: Maintain suitable water pressure.")

    elif level == 5:
        print("System: Automated irrigation")
        print("Advice: Check timer settings regularly.")
        print("Advice: Adjust watering according to weather.")

    print("-" * 60)


# -------------------- SUNNY WEATHER --------------------------

def sunny_advice():

    show_sunny()

    show_section_header("SUNNY WEATHER WATER ADVICE")

    print("\nWeather Condition : SUNNY\n")

    print("[+] Recommended Actions")
    print("    1. Check soil moisture before watering.")
    print("    2. Provide appropriate irrigation.")
    print("    3. Water during early morning or evening.")
    print("    4. Use mulch to reduce evaporation.")
    print("    5. Monitor plants for signs of water stress.")
    print("    6. Check irrigation pipes for leaks.")
    print("    7. Avoid wasting water.")

    print("\n[-] Avoid")
    print("    - Excessive watering.")
    print("    - Watering during the hottest part of the day.")
    print("    - Ignoring dry soil.")


# -------------------- RAINY WEATHER --------------------------

def rainy_advice():

    show_rain()

    show_section_header("RAINY WEATHER WATER ADVICE")

    print("\nWeather Condition : RAINY\n")

    print("[+] Recommended Actions")
    print("    1. Reduce or stop irrigation if rainfall is sufficient.")
    print("    2. Check soil moisture before watering.")
    print("    3. Check drainage channels.")
    print("    4. Remove blocked drainage paths.")
    print("    5. Monitor plants for waterlogging.")
    print("    6. Watch for fungal diseases.")
    print("    7. Protect young plants from heavy rain.")

    print("\n[-] Avoid")
    print("    - Additional watering when soil is saturated.")
    print("    - Blocked drainage systems.")
    print("    - Allowing water to remain around plant roots.")


# -------------------- CLOUDY WEATHER -------------------------

def cloudy_advice():

    show_cloudy()

    show_section_header("CLOUDY WEATHER WATER ADVICE")

    print("\nWeather Condition : CLOUDY\n")

    print("[+] Recommended Actions")
    print("    1. Check soil moisture regularly.")
    print("    2. Provide moderate irrigation when necessary.")
    print("    3. Monitor plants for water stress.")
    print("    4. Check drainage conditions.")
    print("    5. Adjust watering based on soil moisture.")
    print("    6. Avoid unnecessary irrigation.")

    print("\n[-] Avoid")
    print("    - Following a fixed watering schedule blindly.")
    print("    - Excessive watering.")


# -------------------- WEATHER MENU ---------------------------

def weather_advisor():

    while True:

        show_section_header("WEATHER CONDITION")

        print("""
   +-----------------------------+
   |       WEATHER MENU          |
   +-----------------------------+
   | 1. Sunny                   |
   | 2. Rainy                   |
   | 3. Cloudy                  |
   | 4. Back                    |
   +-----------------------------+
        """)

        weather = get_number(1, 4)

        if weather == 1:
            sunny_advice()

        elif weather == 2:
            rainy_advice()

        elif weather == 3:
            cloudy_advice()

        elif weather == 4:
            break

        input("\nPress ENTER to continue...")


# -------------------- WATER SAVING TIPS ----------------------

def water_saving_tips():

    show_section_header("SMART WATER-SAVING TIPS")

    print(r"""

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

""")


# -------------------- DRAINAGE CHECK -------------------------

def drainage_check():

    show_section_header("DRAINAGE CHECK")

    print("\nSelect drainage condition:")
    print("1. Good drainage")
    print("2. Slow drainage")
    print("3. Poor drainage")
    print("4. Waterlogged")

    drainage = get_number(1, 4)

    print("\n" + "-" * 60)

    if drainage == 1:
        print("Drainage Status: GOOD")
        print("Recommendation: Continue regular monitoring.")

    elif drainage == 2:
        print("Drainage Status: SLOW")
        print("Recommendation: Check soil and drainage channels.")
        print("Recommendation: Avoid excessive irrigation.")

    elif drainage == 3:
        print("Drainage Status: POOR")
        print("Recommendation: Improve drainage before heavy irrigation.")
        print("Recommendation: Clear blocked drainage channels.")

    elif drainage == 4:
        print("Drainage Status: WATERLOGGED")
        print("Recommendation: Stop irrigation temporarily.")
        print("Recommendation: Remove excess water.")
        print("Recommendation: Improve drainage immediately.")

    print("-" * 60)


# -------------------- FULL WATER ADVISOR ---------------------

def water_management_advisor():

    show_logo()
    show_farm()
    show_water_ascii()

    while True:

        show_section_header("WATER MANAGEMENT ADVISOR")

        print("""
       +--------------------------------+
       |       WATER MANAGEMENT         |
       +--------------------------------+
       | 1. Weather Advisor             |
       | 2. Soil Moisture Check         |
       | 3. Irrigation Management       |
       | 4. Drainage Check              |
       | 5. Water-Saving Tips           |
       | 6. Exit Water Advisor          |
       +--------------------------------+
        """)

        choice = get_number(1, 6)

        if choice == 1:
            weather_advisor()

        elif choice == 2:
            check_soil_moisture()

        elif choice == 3:
            irrigation_level()

        elif choice == 4:
            drainage_check()

        elif choice == 5:
            water_saving_tips()

        elif choice == 6:

            print("\n")
            print("=" * 60)
            print("       Returning to AgriSense Main Menu...")
            print("       Thank you for using Water Management Advisor!")
            print("=" * 60)

            return

        input("\nPress ENTER to return to the Water Management menu...")


# -------------------- MAIN FUNCTION --------------------------

def main():

    water_management_advisor()


# -------------------- PROGRAM START --------------------------
                                                                                                                                                                                                                                                            
if __name__ == "__main__":
    main()