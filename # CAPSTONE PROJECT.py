# CAPSTONE PROJECT

import math

players = []

# 1. Function to display ideal height and weight table for basketball positions
def display_table():
    print("\n--- Ideal Height and Weight for Basketball Positions ---")
    print("{:<20} {:<20} {:<20}".format("Position", "Height (cm)", "Weight (kg)"))
    print("-" * 60)
    print("{:<20} {:<20} {:<20}".format("Point Guard", "170 - 195", "70 - 90"))
    print("{:<20} {:<20} {:<20}".format("Forward", "196 - 205", "80 - 110"))
    print("{:<20} {:<20} {:<20}".format("Center", "> 205", "100 - 130"))
    print("-" * 60)

# 2. Function to add a new player
def add_player():
    print("\n-- Add New Player --")
    name = input("Enter player name: ")
    height = float(input("Enter player height (in cm): "))
    weight = float(input("Enter player weight (in kg): "))
    email = input("Enter player email: ")

    if height < 170:
        print("Sorry, you don't meet the minimum height of the standards.")
        return
    elif weight > 130:
        print("Sorry, but we need each athlete to be fit regarding safety precautions. Please rejoin when your weight meets the standards.")
        return
    else:
        if 170 <= height <= 195 and 70 <= weight <= 90:
            position = "Point Guard"
        elif 196 <= height <= 209 and 80 <= weight <= 110:
            position = "Forward"
        elif height > 209 and 100 <= weight <= 130:
            position = "Center"
        else:
            position = "Will be personally given at health institution"

        players.append({"name": name, "height": height, "weight": weight, "email": email, "position": position})
        print(f"Thank you for filling out the form, Welcome to the second step of the interview.")
        print(f"You will be informed as soon as possible through your email which is: {email}\n")

# 3. Function to display all players
def display_players():
    if not players:
        print("\nNo player records found.\n")
        return
    print("\n--- Player Records ---")
    print("{:<20} {:<10} {:<10} {:<25} {:<15}".format("Name", "Height", "Weight", "Email", "Position"))
    print("-" * 80)
    for player in players:
        print("{:<20} {:<10} {:<10} {:<25} {:<15}".format(
            player["name"], player["height"], player["weight"], player["email"], player["position"]))
    print()

# 4. Function to search for a player by name
def search_player():
    search_name = input("\nEnter the player's name to search: ")
    for player in players:
        if player["name"].lower() == search_name.lower():
            print(f"\nPlayer found: {player['name']}, Height: {player['height']} cm, Weight: {player['weight']} kg, Email: {player['email']}, Position: {player['position']}")
            return
    print("\nPlayer not found.\n")

# 5. Function to update a player's details
def update_player():
    update_name = input("\nEnter the player's name to update: ")
    for player in players:
        if player["name"].lower() == update_name.lower():
            print(f"Updating details for {player['name']}...")
            player["height"] = float(input("Enter new height (cm): "))
            player["weight"] = float(input("Enter new weight (kg): "))
            player["email"] = input("Enter new email: ")
            print("Player details updated successfully.\n")
            return
    print("\nPlayer not found.\n")

# 6. Function to delete a player
def delete_player():
    delete_name = input("\nEnter the player's name to delete: ")
    for i, player in enumerate(players):
        if player["name"].lower() == delete_name.lower():
            players.pop(i)
            print(f"Player {delete_name} deleted successfully.\n")
            return
    print("\nPlayer not found.\n")

# Main function to run the recruitment program
def main():
    while True:
        print("\n--- Basketball Recruitment Program ---")
        print("1. Show Ideal Height and Weight Table")
        print("2. Add Player")
        print("3. Display All Players")
        print("4. Search Player by Name")
        print("5. Update Player Details")
        print("6. Delete Player")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            display_table()
        elif choice == "2":
            add_player()
        elif choice == "3":
            display_players()
        elif choice == "4":
            search_player()
        elif choice == "5":
            update_player()
        elif choice == "6":
            delete_player()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option.\n")

# Run the main program
if __name__ == "__main__":
    main()