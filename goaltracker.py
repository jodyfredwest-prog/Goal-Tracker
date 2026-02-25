import json
import os
import random

# Display welcome message
print("Welcome to your Goal tracker✨")
print()
print("Let's get intentional")

#Create affirmations list
affirmations = [
    "Everything not meant for me falls away on its own",
    "I attract opportunities that align with my goals",
    "I deserve success without burnout",
    "I radiate confidence and calm energy",
    "I am allowed to take up space",
    "I execute even when I don't feel motivated",
    "Success is a natural outcome of my persistence",
    "I outgrow old limits daily",
    "I choose long-term success over short-term comfort",
    "My goals are non-negotiable"
]

# Create empty list called goals
goals = []

# Load saved goals if file exists
if os.path.exists("goals.json"):
    with open("goals.json", "r") as file:
        goals = json.load(file)

#mainloop
while True:
    print("\nMenu")
    print("1. Add a new goal 📝")
    print("2. View your goals 📋")
    print("3. Mark goal complete ✅")
    print("4. Daily affirmation✨")
    print("5. Exit 🚪")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        goal_text = input("Enter you new goal: ").strip()
        target_date = input("Enter your target date (YYYY-MM-DD): ").strip()

        new_goal = {
            "goal": goal_text,
            "date": target_date,
            "status": "In Progress"
        }

        goals.append(new_goal)

    elif choice == "2":
        if not goals:
            print("You have no goals yet.")
        else:
            print("\nYour Goals:")
            for index, goal in enumerate(goals, start=1):
                print(f"{index}. {goal['goal']}")
                print(f"   Target Date: {goal['date']}")
                print(f"   Status: {goal['status']}")
                print("----------------------")

    elif choice == "3":


        if not goals:
            print("No goals to complete.")
        else:
            print("\nSelect a goal to mark complete:")

            for index, goal in enumerate(goals, start=1):
                print(f"{index}. {goal['goal']} ({goal['status']})")

            selection = input("Enter goal number: ").strip()

            if selection.isdigit():
                selection = int(selection)

                if 1 <= selection <= len(goals):
                    goals[selection - 1]["status"] = "Completed"

                    # Save changes
                    with open("goals.json", "w") as file:
                        json.dump(goals, file, indent=4)

                    print("Goal marked as completed!")
                else:
                    print("Invalid number.")
            else:
                print("Please enter a valid number.")

    elif choice == "4":
        affirmation = random.choice(affirmations)
        print(affirmation)
    elif choice == "5":
        print("Thank you for your time")
        break
    else:
        print("Invalid option, please choose 1-5")
        continue




