# Art Showcase RSVP System
# Developed by Ranganathan

import os

FILENAME = "guest_list.txt"

# ----------------------------
# Helper Functions
# ----------------------------

def load_guests():
    """Load guest data from file."""
    guests = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    guests.append({"name": parts[0], "style": parts[1]})
    return guests


def save_guests(guests):
    """Save all guests to file."""
    with open(FILENAME, "w") as file:
        for guest in guests:
            file.write(f"{guest['name']},{guest['style']}\n")


def add_guest():
    """Add a new guest to the list."""
    name = input("Enter guest name: ").strip()
    style = input("Enter art style (e.g., Abstract, Portrait, Sculpture): ").strip()

    if name and style:
        guests = load_guests()
        guests.append({"name": name, "style": style})
        save_guests(guests)
        print(f"✅ Guest '{name}' added successfully!\n")
    else:
        print("⚠️ Both name and style are required.\n")


def view_guests():
    """Display all guests."""
    guests = load_guests()
    if not guests:
        print("No guests have RSVP'd yet.\n")
        return

    print("\n🖼️ Guest List:")
    for i, guest in enumerate(guests, start=1):
        print(f"{i}. {guest['name']} - {guest['style']}")
    print()


def search_guest():
    """Search for a guest by name."""
    name = input("Enter guest name to search: ").strip()
    guests = load_guests()
    found = [g for g in guests if g['name'].lower() == name.lower()]

    if found:
        print(f"\n🎯 Found Guest: {found[0]['name']} ({found[0]['style']})\n")
    else:
        print("❌ Guest not found.\n")


def filter_by_style():
    """Filter guests by art style."""
    style = input("Enter art style to filter: ").strip()
    guests = load_guests()
    filtered = [g for g in guests if g['style'].lower() == style.lower()]

    if filtered:
        print(f"\n🎨 Guests with style '{style}':")
        for g in filtered:
            print(f"- {g['name']}")
        print()
    else:
        print("⚠️ No guests found for that art style.\n")


def count_by_style():
    """Count guests by each art style."""
    guests = load_guests()
    if not guests:
        print("No guests available to count.\n")
        return

    style_count = {}
    for g in guests:
        style_count[g['style']] = style_count.get(g['style'], 0) + 1

    print("\n📊 RSVP Count by Art Style:")
    for style, count in style_count.items():
        print(f"{style}: {count}")
    print()


def send_invitations():
    """Send a personalized invitation message to all guests."""
    guests = load_guests()
    if not guests:
        print("No guests available to send invitations.\n")
        return

    print("\n📩 Sending Invitations...")
    for guest in guests:
        print(f"Dear {guest['name']}, you're invited to the Art Showcase! "
              f"We look forward to seeing your {guest['style']} masterpiece.")
    print("\n✅ All invitations sent!\n")


# ----------------------------
# Main Menu
# ----------------------------

def main():
    while True:
        print("====== ART SHOWCASE RSVP SYSTEM ======")
        print("1. View Guest List")
        print("2. Add Guest")
        print("3. Search Guest by Name")
        print("4. Filter Guests by Art Style")
        print("5. Count Guests by Style")
        print("6. Send Invitations")
        print("7. Exit")
        print("======================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            view_guests()
        elif choice == "2":
            add_guest()
        elif choice == "3":
            search_guest()
        elif choice == "4":
            filter_by_style()
        elif choice == "5":
            count_by_style()
        elif choice == "6":
            send_invitations()
        elif choice == "7":
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    main()
