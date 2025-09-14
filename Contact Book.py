# 📒 Contact Book in Python

# Each contact will be stored as:
# contacts = {
#     "Alice": {"phone": "1234567890", "email": "alice@example.com"},
#     "Bob": {"phone": "9876543210", "email": "bob@example.com"}
# }

contacts = {}

def add_contact(name, phone, email):
    """Add a new contact or update if already exists."""
    contacts[name] = {"phone": phone, "email": email}
    print(f"✅ Contact '{name}' added/updated successfully!\n")

def view_contacts():
    """View all contacts."""
    if not contacts:
        print("📭 No contacts found.\n")
        return
    print("📒 Contact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    print()

def search_contact(name):
    """Search for a contact by name."""
    if name in contacts:
        info = contacts[name]
        print(f"🔍 Found Contact - Name: {name}, Phone: {info['phone']}, Email: {info['email']}\n")
    else:
        print(f"❌ Contact '{name}' not found.\n")

def update_contact(name, phone=None, email=None):
    """Update an existing contact's phone or email."""
    if name in contacts:
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print(f"✏️ Contact '{name}' updated successfully!\n")
    else:
        print(f"❌ Contact '{name}' not found.\n")

def delete_contact(name):
    """Delete a contact by name."""
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted successfully!\n")
    else:
        print(f"❌ Contact '{name}' not found.\n")

# --- Menu-driven program ---
def menu():
    while True:
        print("====== Contact Book ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        
        elif choice == "2":
            view_contacts()
        
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        
        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone (leave blank to keep old): ")
            email = input("Enter new email (leave blank to keep old): ")
            update_contact(name, phone if phone else None, email if email else None)
        
        elif choice == "5":
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("⚠️ Invalid choice! Please try again.\n")

# Run the contact book
if __name__ == "__main__":
    menu()
