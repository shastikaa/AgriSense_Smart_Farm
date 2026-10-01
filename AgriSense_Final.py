import importlib.util
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_module(module_name, file_name):
    file_path = BASE_DIR / file_name
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


member1 = load_module("member1_smart_crop", "Member1_SmartCrop.py")
member2 = load_module("member2_water_advisor", "Member2_WaterAdvisor .py")
member3 = load_module("member3_farming_tips", "Member3_FarmingTips.py")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    while True:
        clear_screen()
        print("=" * 72)
        print("                AGRISENSE - SMART FARM DECISION ASSISTANT")
        print("=" * 72)
        print("\nChoose a module:\n")
        print("1. Smart Crop Check")
        print("2. Water Management Advisor")
        print("3. Farm Health Scanner & Farming Tips")
        print("4. Exit")
        print("=" * 72)

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            clear_screen()
            member1.show_logo()
            member1.main_menu()
        elif choice == "2":
            clear_screen()
            member2.water_management_advisor()
        elif choice == "3":
            clear_screen()
            member3.agri_logo()
            member3.farming_tips_menu()
        elif choice == "4":
            clear_screen()
            print("\nThank you for using AgriSense!")
            print("Smart farming starts with better information.\n")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")
            input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main_menu()
