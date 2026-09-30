# ============================================================
# AGRISENSE - SMART FARM DECISION ASSISTANT
# Member 3: Farm Health Scanner & Farming Tips
# ============================================================


# ============================================================
# ASCII ART
# ============================================================

def agri_logo():
    print(r"""
    ██████╗  ██████╗ ██████╗ ██╗███████╗███████╗███╗   ██╗███████╗███████╗
   ██╔═══██╗██╔════╝ ██╔══██╗██║██╔════╝██╔════╝████╗  ██║██╔════╝██╔════╝
   ███████║██║  ███╗██████╔╝██║███████╗█████╗  ██╔██╗ ██║███████╗█████╗
   ██╔══██║██║   ██║██╔══██╗██║╚════██║██╔══╝  ██║╚██╗██║╚════██║██╔══╝
   ██║  ██║╚██████╔╝██║  ██║██║███████║███████╗██║ ╚████║███████║███████╗
   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝

                    🌾 SMART FARM DECISION ASSISTANT 🌾
    """)


def farm_picture():
    print(r"""
                         ☀️
                    \    |    /
                     \   |   /
                      \  |  /
                   🌳   🌾🌾🌾   🌳
                 🌾🌾🌾🌾🌾🌾🌾🌾🌾
              ─────────────────────────
                 🌱  🌱  🌱  🌱  🌱
                 🌱  🌱  🌱  🌱  🌱
              ─────────────────────────
                   🚜  SMART FARM
    """)


def scanner_picture():
    print(r"""
              ___________________________
             |                           |
             |     🔍 FARM SCANNER       |
             |___________________________|
                     /\
                    /  \
                   / 🌱 \
                  /______\
                     ||
                     ||
                   __||__
                  |______|
    """)


def healthy_farm_picture():
    print(r"""
                  ☀️
             \    |    /
              \   |   /
               \  |  /
                \ | /

          🌳      🌾      🌳
        🌾🌾🌾   🌱🌱🌱   🌾🌾🌾
       🌱🌱🌱🌱 🌱🌱🌱🌱 🌱🌱🌱🌱
       ───────────────────────────
             🚜   🌱   💧
    """)


# ============================================================
# TITLE
# ============================================================

def title():
    print("\n" + "=" * 70)
    print("                 🌾 AGRISENSE FARM ASSISTANT 🌾")
    print("=" * 70)


# ============================================================
# FARM HEALTH SCANNER
# ============================================================

def farm_health_scanner():

    title()
    scanner_picture()

    print("\n🔍 Let's check the current condition of your farm!")
    print("Answer the questions below carefully.\n")

    score = 0
    problems = []

    # --------------------------------------------------------
    # 1. SOIL CONDITION
    # --------------------------------------------------------

    print("\n" + "-" * 70)
    print("🌱 1. SOIL CONDITION")
    print("-" * 70)

    print("1. Good and fertile")
    print("2. Dry")
    print("3. Poor / unhealthy")

    soil = input("\nSelect soil condition (1-3): ")

    if soil == "1":

        score += 2

        print("\n✅ Soil condition looks good!")
        print("🌱 Your soil appears suitable for healthy plant growth.")

    elif soil == "2":

        score += 1
        problems.append("Soil is dry")

        print("\n⚠️ Soil is dry.")
        print("💧 Your soil may need better moisture management.")

    elif soil == "3":

        problems.append("Poor soil quality")

        print("\n⚠️ Soil quality needs attention.")
        print("🌱 Consider improving soil nutrients with suitable organic matter.")

    else:

        print("\n❌ Invalid choice.")
        print("Soil condition was skipped.")


    # --------------------------------------------------------
    # 2. PLANT CONDITION
    # --------------------------------------------------------

    print("\n" + "-" * 70)
    print("🌿 2. PLANT CONDITION")
    print("-" * 70)

    print("1. Healthy and green")
    print("2. Yellow leaves")
    print("3. Brown / damaged leaves")

    plant = input("\nSelect plant condition (1-3): ")

    if plant == "1":

        score += 2

        print("\n✅ Plants appear healthy!")
        print("🌿 Continue monitoring them regularly.")

    elif plant == "2":

        score += 1
        problems.append("Yellow leaves")

        print("\n⚠️ Yellow leaves detected.")
        print("🌿 Check plant nutrition, watering and other possible causes.")

    elif plant == "3":

        problems.append("Damaged leaves")

        print("\n🚨 Damaged leaves detected.")
        print("🌿 Inspect plants for pests, disease or environmental stress.")

    else:

        print("\n❌ Invalid choice.")
        print("Plant condition was skipped.")


    # --------------------------------------------------------
    # 3. PEST CONDITION
    # --------------------------------------------------------

    print("\n" + "-" * 70)
    print("🐛 3. PEST ACTIVITY")
    print("-" * 70)

    print("1. No pests noticed")
    print("2. Few pests")
    print("3. Many pests")

    pest = input("\nSelect pest condition (1-3): ")

    if pest == "1":

        score += 2

        print("\n✅ No major pest activity reported.")
        print("🌱 Continue regular crop inspection.")

    elif pest == "2":

        score += 1
        problems.append("Some pest activity")

        print("\n⚠️ Some pest activity detected.")
        print("🐛 Monitor affected plants regularly.")

    elif pest == "3":

        problems.append("High pest activity")

        print("\n🚨 High pest activity detected!")
        print("🐛 Inspect affected plants and consider suitable pest management.")

    else:

        print("\n❌ Invalid choice.")
        print("Pest condition was skipped.")


    # --------------------------------------------------------
    # 4. WATER CONDITION
    # --------------------------------------------------------

    print("\n" + "-" * 70)
    print("💧 4. WATER CONDITION")
    print("-" * 70)

    print("1. Enough water")
    print("2. Water is limited")
    print("3. Too much water")

    water = input("\nSelect water condition (1-3): ")

    if water == "1":

        score += 2

        print("\n✅ Water availability appears sufficient.")
        print("💧 Continue monitoring soil moisture.")

    elif water == "2":

        score += 1
        problems.append("Limited water")

        print("\n⚠️ Water availability is limited.")
        print("💧 Consider efficient irrigation and reducing water loss.")

    elif water == "3":

        problems.append("Excess water")

        print("\n⚠️ Too much water detected.")
        print("💧 Check drainage and avoid unnecessary watering.")

    else:

        print("\n❌ Invalid choice.")
        print("Water condition was skipped.")


    # ========================================================
    # FARM HEALTH RESULT
    # ========================================================

    print("\n\n" + "=" * 70)
    print("                 📊 FARM HEALTH RESULT")
    print("=" * 70)

    print(f"\n🌾 Farm Health Score: {score}/8")

    if score >= 7:

        status = "EXCELLENT 🌟"
        message = "Your farm is currently showing healthy conditions."

    elif score >= 5:

        status = "GOOD 👍"
        message = "Your farm is generally in good condition, but monitor it regularly."

    elif score >= 3:

        status = "NEEDS ATTENTION ⚠️"
        message = "Some areas of your farm require attention."

    else:

        status = "HIGH ATTENTION REQUIRED 🚨"
        message = "Several areas require immediate monitoring."


    print(f"\n🌱 Status: {status}")
    print(f"💬 {message}")


    # ========================================================
    # AREAS TO WATCH
    # ========================================================

    print("\n" + "-" * 70)
    print("🔎 AREAS TO WATCH")
    print("-" * 70)

    if problems:

        for problem in problems:
            print(f"  ⚠️ {problem}")

    else:

        print("  🎉 No major problems were identified!")


    # ========================================================
    # RECOMMENDATIONS
    # ========================================================

    print("\n" + "-" * 70)
    print("💡 AGRISENSE RECOMMENDATION")
    print("-" * 70)

    if "Soil is dry" in problems:
        print("🌱 Check soil moisture before watering.")

    if "Poor soil quality" in problems:
        print("🌱 Consider compost or suitable soil-improvement practices.")

    if "Yellow leaves" in problems:
        print("🌿 Monitor plant nutrition, watering and possible stress factors.")

    if "Damaged leaves" in problems:
        print("🌿 Inspect leaves carefully for pests, disease or environmental damage.")

    if "Some pest activity" in problems:
        print("🐛 Monitor affected plants regularly.")

    if "High pest activity" in problems:
        print("🐛 Inspect affected areas and apply suitable pest-management practices.")

    if "Limited water" in problems:
        print("💧 Use efficient irrigation and reduce unnecessary water loss.")

    if "Excess water" in problems:
        print("💧 Check drainage and avoid overwatering.")

    if not problems:
        print("🌟 Continue regular monitoring and maintain your current farm practices.")

    print("\n" + "=" * 70)


# ============================================================
# SMART FARMING TIPS
# ============================================================

def farming_tips():

    print("\n" + "=" * 70)
    print("                 🌾 SMART FARMING TIPS")
    print("=" * 70)

    farm_picture()

    print("\n🌱 SOIL CARE")
    print("-" * 50)
    print("• Add suitable organic matter to improve soil condition.")
    print("• Avoid excessive fertilizer use.")
    print("• Rotate crops where appropriate.")

    print("\n💧 WATER MANAGEMENT")
    print("-" * 50)
    print("• Check soil moisture before watering.")
    print("• Reduce unnecessary water loss.")
    print("• Maintain irrigation equipment.")

    print("\n🌿 PLANT HEALTH")
    print("-" * 50)
    print("• Check leaves and stems regularly.")
    print("• Monitor crops for unusual changes.")
    print("• Investigate damaged or unhealthy plants.")

    print("\n🐛 PEST MANAGEMENT")
    print("-" * 50)
    print("• Inspect plants regularly.")
    print("• Identify pest problems early.")
    print("• Use appropriate pest-management methods.")

    print("\n🌤️ WEATHER")
    print("-" * 50)
    print("• Check weather conditions before major farm activities.")
    print("• Protect vulnerable crops during extreme weather.")

    print("\n📋 FARM RECORDS")
    print("-" * 50)
    print("• Record planting dates.")
    print("• Record irrigation and fertilizer activities.")
    print("• Monitor crop growth and harvest information.")

    print("\n" + "=" * 70)


# ============================================================
# MAIN MEMBER 3 MENU
# ============================================================

def farming_tips_menu():

    while True:

        print("\n")
        print("=" * 70)
        print("             🌾 AGRISENSE FARM ASSISTANT 🌾")
        print("=" * 70)

        print(r"""
                 🌱       🌱       🌱
               🌱🌱🌱   🌱🌱🌱   🌱🌱🌱
              🌱🌱🌱🌱 🌱🌱🌱🌱 🌱🌱🌱🌱
                   🚜   SMART FARM   🚜
        """)

        print("1. 🔍 Farm Health Scanner")
        print("2. 🌱 Smart Farming Tips")
        print("3. 🚪 Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":

            farm_health_scanner()

            input("\n👉 Press ENTER to return to the menu...")

        elif choice == "2":

            farming_tips()

            input("\n👉 Press ENTER to return to the menu...")

        elif choice == "3":

            # =================================================
            # THANK YOU SCREEN
            # =================================================

            print("\n\n")
            print("=" * 70)

            print(r"""
                 🌾🌾🌾  AGRISENSE  🌾🌾🌾

                       THANK YOU!

              Thank you for using AgriSense
               Smart Farm Decision Assistant

                    🌱 Grow Smarter
                    💧 Save Resources
                    🌿 Protect Crops
                    🚜 Farm Better

                       🌾  🌾  🌾
            """)

            print("=" * 70)
            print("              🌱 SMART FARMING,")
            print("             SMARTER TOMORROW! 🌱")
            print("=" * 70)

            break

        else:

            print("\n" + "-" * 70)
            print("❌ INVALID CHOICE!")
            print("Please enter a number from 1 to 3.")
            print("-" * 70)


# ============================================================
# RUN MEMBER 3 MODULE
# ============================================================

if __name__ == "__main__":
    agri_logo()
    farming_tips_menu()