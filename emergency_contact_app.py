#!/usr/bin/env python3
"""
===========================================
Emergency Contact Application
===========================================
A beginner-friendly Python program to manage 
emergency contacts and simulate emergency alerts.

Author: Beginner Python Developer
Level: Beginner
===========================================
"""

# ===========================================
# DATA STORAGE
# ===========================================
# We use a LIST to store all emergency contacts
# Each contact is a DICTIONARY with 'name' and 'phone' keys
# Example: [{"name": "John", "phone": "1234567890"}, ...]

contacts_list = []  # Empty list to start - will hold our contacts


# ===========================================
# INDIAN GOVERNMENT EMERGENCY CONTACTS
# ===========================================
# These are official emergency contact numbers provided by Government of India

indian_emergency_contacts = [
    {"name": "Police (All India)", "phone": "100"},
    {"name": "Fire Service", "phone": "101"},
    {"name": "Ambulance", "phone": "102"},
    {"name": "Women Helpline", "phone": "1091"},
    {"name": "Child Helpline", "phone": "1098"},
    {"name": "Disaster Management", "phone": "1070"},
    {"name": "National Emergency (Police/Fire/Ambulance)", "phone": "112"},
    {"name": "Railway Police", "phone": "1512"},
    {"name": "Road Safety", "phone": "1033"},
    {"name": "Anti Terrorist Helpline", "phone": "1930"},
]


# ===========================================
# FUNCTION: Load Indian Government Emergency Contacts
# ===========================================
def load_indian_emergency_contacts():
    """
    This function loads the Indian government emergency contact numbers.
    These are preset contacts that users can add with one click.
    """
    global contacts_list  # Allow modifying the global contacts list
    
    print("\n" + "="*50)
    print("   INDIAN GOVERNMENT EMERGENCY CONTACTS")
    print("="*50)
    print("\nAdding the following emergency contacts:\n")
    
    # Add all Indian emergency contacts to the list
    for contact in indian_emergency_contacts:
        print(f"  ✓ {contact['name']} - {contact['phone']}")
        contacts_list.append(contact)
    
    print("\n" + "="*50)
    print(f"✓ Successfully added {len(indian_emergency_contacts)} Indian emergency contacts!")
    print("="*50)


# ===========================================
# FUNCTION: Add a new emergency contact
# ===========================================
def add_contact():
    """
    This function allows user to add a new emergency contact.
    It asks for name and phone number, then saves them.
    """
    print("\n" + "="*40)
    print("       ADD NEW EMERGENCY CONTACT")
    print("="*40)
    
    # Get name from user
    name = input("Enter contact name: ").strip()
    
    # Check if name is empty
    if name == "":
        print("ERROR: Name cannot be empty!")
        return
    
    # Get phone number from user
    phone = input("Enter phone number: ").strip()
    
    # Check if phone is empty
    if phone == "":
        print("ERROR: Phone number cannot be empty!")
        return
    
    # Create a dictionary for this contact
    # We use a dictionary because we have two pieces of info: name and phone
    contact = {
        "name": name,
        "phone": phone
    }
    
    # Add the contact to our list
    contacts_list.append(contact)
    
    # Confirm to user
    print(f"\n✓ SUCCESS: Contact '{name}' added successfully!")
    print(f"  Phone: {phone}")


# ===========================================
# FUNCTION: View all saved contacts
# ===========================================
def view_contacts():
    """
    This function displays all saved emergency contacts.
    It handles the case when no contacts exist.
    """
    print("\n" + "="*40)
    print("       VIEW EMERGENCY CONTACTS")
    print("="*40)
    
    # Check if we have any contacts
    if len(contacts_list) == 0:
        print("\n⚠ No emergency contacts saved yet!")
        print("  Use option 1 to add a contact.")
        return
    
    # We have contacts, so display them
    print(f"\nTotal contacts: {len(contacts_list)}\n")
    
    # Loop through each contact in the list
    # enumerate() gives us both index and the contact
    for index, contact in enumerate(contacts_list, start=1):
        # Access dictionary values using keys
        name = contact["name"]
        phone = contact["phone"]
        
        # Display contact information
        print(f"  Contact #{index}")
        print(f"  ─────────────")
        print(f"  Name : {name}")
        print(f"  Phone: {phone}")
        print()


# ===========================================
# FUNCTION: Trigger emergency alert
# ===========================================
def emergency_alert():
    """
    This function simulates sending an emergency alert.
    It prints a message to indicate the alert was sent.
    """
    print("\n" + "!"*40)
    print("       🚨 EMERGENCY ALERT 🚨")
    print("!"*40)
    
    # Check if there are contacts to notify
    if len(contacts_list) == 0:
        print("\n⚠ WARNING: No contacts to notify!")
        print("  Please add emergency contacts first.")
        return
    
    # Show how many people will be notified
    print(f"\nNotifying {len(contacts_list)} emergency contact(s)...")
    
    # List all contacts that will be notified
    print("\nContacts being notified:")
    for contact in contacts_list:
        print(f"  - {contact['name']} ({contact['phone']})")
    
    # THE MAIN OUTPUT - This is the required output!
    print("\n" + "*"*40)
    print("   Emergency message sent")
    print("*"*40)
    print("\n✓ All contacts have been notified successfully!")


# ===========================================
# FUNCTION: Display the main menu
# ===========================================
def display_menu():
    """
    This function displays the main menu options.
    """
    print("\n" + "="*50)
    print("      EMERGENCY CONTACT APPLICATION")
    print("="*50)
    print("  1. Add Emergency Contact")
    print("  2. View All Contacts")
    print("  3. Trigger Emergency Alert")
    print("  4. Load Indian Government Emergency Contacts")
    print("  5. Exit Application")
    print("="*50)


# ===========================================
# FUNCTION: Main program loop
# ===========================================
def main():
    """
    This is the main function that runs the program.
    It contains the main loop that keeps the program running.
    """
    # Welcome message
    print("\n" + "="*50)
    print("  Welcome to Emergency Contact Application!")
    print("="*50)
    print("  This program helps you manage emergency contacts")
    print("  and send emergency alerts when needed.")
    print("="*50)
    
    # Main loop - keeps running until user chooses to exit
    while True:
        # Show the menu
        display_menu()
        
        # Ask user for their choice
        choice = input("Enter your choice (1-5): ").strip()
        
        # Process the user's choice
        # We use if-elif-else to handle different options
        if choice == "1":
            # Option 1: Add a new contact
            add_contact()
            
        elif choice == "2":
            # Option 2: View all contacts
            view_contacts()
            
        elif choice == "3":
            # Option 3: Trigger emergency alert
            emergency_alert()
            
        elif choice == "4":
            # Option 4: Load Indian Government Emergency Contacts
            load_indian_emergency_contacts()
            
        elif choice == "5":
            # Option 5: Exit the program
            print("\n" + "="*50)
            print("  Thank you for using the application!")
            print("  Stay safe! 👋")
            print("="*50)
            break  # Break exits the while loop
            
        else:
            # Invalid choice - user entered something other than 1-5
            print("\n⚠ Invalid choice! Please enter a number from 1 to 5.")


# ===========================================
# PROGRAM ENTRY POINT
# ===========================================
# This special line checks if the program is being run directly
# (not imported as a module), and calls the main() function
if __name__ == "__main__":
    # Call the main function to start the program
    main()
