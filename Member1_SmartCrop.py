# ============================================================
#             AGRISENSE - SMART FARM ASSISTANT
#                   MEMBER 1: SMART CROP CHECK
# ============================================================

import time


# ============================================================
#                    COLOUR SETTINGS
# ============================================================

GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"


# ============================================================
#                     CREATIVE FARM LOGO
# ============================================================

def show_logo():

    print(GREEN + r"""
                         .-========-.
                      .-'  AGRISENSE '-.
                    .'                  '.
                   /    \  |  /           \
                  |      \ | /             |
                  |    --- 🌱 ---           |
                  |       /|\              |
                   \     / | \            /
                    '.                  .'
                      '-.____________.-'

                         \   |   /
                          \  |  /
                       ____\ | /____
                    __/      |      \__
                 __/         |         \__
              __/____________|____________\__

                    SMART FARM ASSISTANT
    """ + RESET)

    print(YELLOW + "       Better Decisions | Healthier Crops" + RESET)
    print(GREEN + "              A Greener Future" + RESET)
    print()


# ============================================================
#                       HEADER
# ============================================================

def show_header():

    print(CYAN + "=" * 60 + RESET)
    print(GREEN + BOLD + "                 AGRISENSE" + RESET)
    print(WHITE + "          SMART FARM DECISION ASSISTANT" + RESET)
    print(CYAN + "=" * 60 + RESET)


# ============================================================
#                       MAIN MENU
# ============================================================

def main_menu():

    while True:

        show_header()

        print(YELLOW + "\n================== MAIN MENU ==================" + RESET)
        print("  [1] Smart Crop Check")
        print("  [2] About AgriSense")
        print("  [3] Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            smart_crop_check()

        elif choice == "2":
            about_agrisense()

        elif choice == "3":
            print()
            print(GREEN + "Thank you for using AgriSense!" + RESET)
            print("Smarter farming starts with better information.")
            print(GREEN + "\n                 Happy Farming! 🌱" + RESET)
            break

        else:
            print(RED + "\nInvalid choice! Please enter 1, 2 or 3." + RESET)


# ============================================================
#                    SMART CROP CHECK
# ============================================================

def smart_crop_check():

    show_header()

    print(CYAN + "\n                SMART CROP CHECK" + RESET)
    print("-" * 60)

    print("Answer four questions about your farm.")
    print("AgriSense will analyse your selections and")
    print("provide suitable farming recommendations.")

    crop = select_crop()
    soil = select_soil()
    weather = select_weather()
    condition = select_plant_condition()

    print()
    print(MAGENTA + "=" * 60 + RESET)
    print(BOLD + "             ANALYSING YOUR FARM..." + RESET)
    print(MAGENTA + "=" * 60 + RESET)

    loading_animation()

    score = calculate_score(crop, soil, weather, condition)

    show_analysis(crop, soil, weather, condition, score)

    input(CYAN + "\nPress ENTER to return to the main menu..." + RESET)


# ============================================================
#                       CROP SELECTION
# ============================================================

def select_crop():

    crops = {
        "1": "Rice",
        "2": "Corn",
        "3": "Tomato",
        "4": "Chili"
    }

    print(GREEN + "\n========== STEP 1: SELECT YOUR CROP ==========" + RESET)

    print("  [1] Rice")
    print("  [2] Corn")
    print("  [3] Tomato")
    print("  [4] Chili")

    while True:

        choice = input("\nChoose your crop (1-4): ").strip()

        if choice in crops:
            print(GREEN + "Crop selected: " + crops[choice] + RESET)
            return crops[choice]

        print(RED + "Invalid choice. Please enter 1-4." + RESET)


# ============================================================
#                       SOIL SELECTION
# ============================================================

def select_soil():

    soils = {
        "1": "Loamy",
        "2": "Clay",
        "3": "Sandy"
    }

    print(YELLOW + "\n========== STEP 2: SELECT SOIL TYPE ==========" + RESET)

    print("  [1] Loamy")
    print("  [2] Clay")
    print("  [3] Sandy")

    while True:

        choice = input("\nChoose your soil (1-3): ").strip()

        if choice in soils:
            print(GREEN + "Soil selected: " + soils[choice] + RESET)
            return soils[choice]

        print(RED + "Invalid choice. Please enter 1-3." + RESET)


# ============================================================
#                      WEATHER SELECTION
# ============================================================

def select_weather():

    weather_types = {
        "1": "Sunny",
        "2": "Rainy",
        "3": "Cloudy"
    }

    print(BLUE + "\n========== STEP 3: SELECT WEATHER ==========" + RESET)

    print("  [1] Sunny")
    print("  [2] Rainy")
    print("  [3] Cloudy")

    while True:

        choice = input("\nChoose the weather (1-3): ").strip()

        if choice in weather_types:
            print(GREEN + "Weather selected: " + weather_types[choice] + RESET)
            return weather_types[choice]

        print(RED + "Invalid choice. Please enter 1-3." + RESET)


# ============================================================
#                  PLANT CONDITION SELECTION
# ============================================================

def select_plant_condition():

    conditions = {
        "1": "Healthy",
        "2": "Leaves turning yellow",
        "3": "Leaves wilting"
    }

    print(MAGENTA + "\n====== STEP 4: PLANT CONDITION ======" + RESET)

    print("  [1] Healthy")
    print("  [2] Leaves turning yellow")
    print("  [3] Leaves wilting")

    while True:

        choice = input("\nChoose plant condition (1-3): ").strip()

        if choice in conditions:
            print(GREEN + "Condition selected: " + conditions[choice] + RESET)
            return conditions[choice]

        print(RED + "Invalid choice. Please enter 1-3." + RESET)


# ============================================================
#                     LOADING ANIMATION
# ============================================================

def loading_animation():

    tasks = [
        "Checking crop condition",
        "Analysing soil type",
        "Evaluating weather",
        "Preparing recommendations"
    ]

    for task in tasks:
        print(CYAN + "  > " + task + "..." + RESET)
        time.sleep(0.4)

    print(GREEN + "\n  Analysis completed successfully!" + RESET)


# ============================================================
#                    FARM HEALTH SCORE
# ============================================================

def calculate_score(crop, soil, weather, condition):

    score = 50

    # Plant condition
    if condition == "Healthy":
        score += 30

    elif condition == "Leaves turning yellow":
        score += 5

    elif condition == "Leaves wilting":
        score -= 10

    # Soil suitability
    soil_scores = {
        "Rice": {
            "Loamy": 10,
            "Clay": 5,
            "Sandy": -5
        },
        "Corn": {
            "Loamy": 10,
            "Clay": -5,
            "Sandy": 5
        },
        "Tomato": {
            "Loamy": 10,
            "Clay": -5,
            "Sandy": 5
        },
        "Chili": {
            "Loamy": 10,
            "Clay": -5,
            "Sandy": 5
        }
    }

    score += soil_scores[crop][soil]

    # Weather suitability
    if weather == "Sunny":

        if crop in ["Corn", "Tomato", "Chili"]:
            score += 5
        else:
            score += 2

    elif weather == "Rainy":

        if crop == "Rice":
            score += 8
        else:
            score -= 3

    elif weather == "Cloudy":
        score += 1

    # Keep score within 0-100
    score = max(0, min(score, 100))

    return score


# ============================================================
#                     DISPLAY ANALYSIS
# ============================================================

def show_analysis(crop, soil, weather, condition, score):

    show_header()

    print(GREEN + "\n                 FARM ANALYSIS RESULT" + RESET)
    print("=" * 60)

    print(f"\n  Crop             : {crop}")
    print(f"  Soil Type        : {soil}")
    print(f"  Weather          : {weather}")
    print(f"  Plant Condition  : {condition}")

    print("\n" + CYAN + "-" * 60 + RESET)

    show_health_score(score)

    show_recommendations(crop, soil, weather, condition)

    show_crop_fact(crop)


# ============================================================
#                      HEALTH SCORE DISPLAY
# ============================================================

def show_health_score(score):

    print(YELLOW + "\n               FARM HEALTH SCORE" + RESET)

    # Visual progress bar
    bar_length = 30
    filled = int(score / 100 * bar_length)

    bar = "█" * filled + "░" * (bar_length - filled)

    print(f"\n  [{GREEN}{bar}{RESET}] {score}/100")

    if score >= 80:

        print(GREEN + "\n  STATUS: EXCELLENT 🌱" + RESET)
        print("  Your selected conditions look favourable.")

    elif score >= 60:

        print(YELLOW + "\n  STATUS: GOOD 🌿" + RESET)
        print("  Your farm may benefit from some improvements.")

    elif score >= 40:

        print(YELLOW + "\n  STATUS: NEEDS ATTENTION ⚠" + RESET)
        print("  Review the recommendations below.")

    else:

        print(RED + "\n  STATUS: HIGH PRIORITY 🚨" + RESET)
        print("  Check your plants and growing conditions promptly.")


# ============================================================
#                   FARMING RECOMMENDATIONS
# ============================================================

def show_recommendations(crop, soil, weather, condition):

    print(CYAN + "\n" + "=" * 60 + RESET)
    print(BOLD + "                RECOMMENDED ACTIONS" + RESET)
    print(CYAN + "=" * 60 + RESET)

    # Plant condition recommendations
    print(YELLOW + "\n1. PLANT CARE" + RESET)

    if condition == "Healthy":

        print(GREEN + "  Your plants appear healthy!" + RESET)
        print("  - Continue regular plant monitoring.")
        print("  - Maintain suitable watering.")
        print("  - Check for pests and diseases.")
        print("  - Apply fertiliser when needed.")

    elif condition == "Leaves turning yellow":

        print(YELLOW + "  Yellow leaves detected." + RESET)
        print("  - Check whether the soil is too wet or dry.")
        print("  - Inspect for possible nutrient deficiencies.")
        print("  - Check leaves for pests or disease.")
        print("  - Avoid adding fertiliser without identifying the cause.")

    elif condition == "Leaves wilting":

        print(RED + "  Wilting plants need attention." + RESET)
        print("  - Check soil moisture immediately.")
        print("  - Inspect roots and stems for damage.")
        print("  - Check for waterlogging or poor drainage.")
        print("  - Provide shade if plants are heat-stressed.")

    # Soil recommendations
    print(YELLOW + "\n2. SOIL MANAGEMENT" + RESET)

    if soil == "Loamy":

        print("  - Maintain soil quality with organic compost.")
        print("  - Monitor moisture and drainage.")

    elif soil == "Clay":

        print("  - Check drainage, especially after rainfall.")
        print("  - Add suitable organic matter to improve soil structure.")
        print("  - Avoid working with waterlogged soil.")

    elif soil == "Sandy":

        print("  - Monitor soil moisture frequently.")
        print("  - Add compost to improve water retention.")
        print("  - Consider smaller, more frequent watering.")

    # Weather recommendations
    print(YELLOW + "\n3. WEATHER MANAGEMENT" + RESET)

    if weather == "Sunny":

        print("  - Check soil moisture during hot periods.")
        print("  - Water when needed, preferably in the morning.")
        print("  - Watch for signs of heat stress.")

    elif weather == "Rainy":

        print("  - Reduce irrigation when rainfall is sufficient.")
        print("  - Check drainage to prevent waterlogging.")
        print("  - Monitor for fungal diseases.")

    elif weather == "Cloudy":

        print("  - Check soil moisture before watering.")
        print("  - Continue monitoring plant growth.")
        print("  - Avoid unnecessary irrigation.")

    # Crop-specific recommendations
    print(YELLOW + "\n4. CROP-SPECIFIC TIPS" + RESET)

    if crop == "Rice":

        print("  - Maintain suitable water levels for the growth stage.")
        print("  - Monitor weeds, pests and drainage.")

    elif crop == "Corn":

        print("  - Provide sufficient sunlight and nutrients.")
        print("  - Monitor moisture during flowering and grain formation.")

    elif crop == "Tomato":

        print("  - Maintain good drainage and consistent soil moisture.")
        print("  - Support plants and inspect leaves regularly.")

    elif crop == "Chili":

        print("  - Avoid waterlogged soil.")
        print("  - Monitor leaves and stems for pests.")

    # Final alert
    print(CYAN + "\n" + "-" * 60 + RESET)

    if condition == "Healthy":

        print(GREEN + "🌱 AGRISENSE: Keep up the good farm care!" + RESET)

    elif condition == "Leaves turning yellow":

        print(YELLOW + "🍂 AGRISENSE: Investigate the cause of yellow leaves." + RESET)

    else:

        print(RED + "🚨 AGRISENSE: Check the plant's growing conditions promptly." + RESET)


# ============================================================
#                       CROP FACTS
# ============================================================

def show_crop_fact(crop):

    facts = {
        "Rice": (
            "Rice needs careful water management. "
            "Water requirements vary by growth stage."
        ),
        "Corn": (
            "Corn benefits from sunlight, suitable soil moisture "
            "and sufficient nutrients."
        ),
        "Tomato": (
            "Tomatoes generally grow well in well-drained soil "
            "with consistent moisture."
        ),
        "Chili": (
            "Chili plants benefit from sunlight, suitable watering "
            "and regular pest inspection."
        )
    }

    print(CYAN + "\n" + "=" * 60 + RESET)
    print(GREEN + "                    DID YOU KNOW?" + RESET)
    print("=" * 60)

    print(f"\n  {crop}: {facts[crop]}")


# ============================================================
#                      ABOUT AGRISENSE
# ============================================================

def about_agrisense():

    show_header()

    print(CYAN + "\n                 ABOUT AGRISENSE" + RESET)
    print("-" * 60)

    print("""
AgriSense is a Smart Farm Decision Assistant designed
to help users make informed farming decisions.

The Smart Crop Check analyses four important factors:

  1. Crop type
  2. Soil type
  3. Weather condition
  4. Plant condition

The program provides:

  - A farm health score
  - Plant care recommendations
  - Soil management advice
  - Weather management tips
  - Crop-specific recommendations

Our goal:
Better Decisions | Healthier Crops | A Greener Future
""")

    input("Press ENTER to return to the main menu...")


# ============================================================
#                     START THE PROGRAM
# ============================================================

if __name__ == "__main__":

    show_logo()

    print(GREEN + BOLD + "Welcome to AgriSense!" + RESET)
    print("Your smart assistant for better farming decisions.\n")

    time.sleep(1)

    main_menu()