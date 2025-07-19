import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} | Phone: {contact['phone']}")

def search_contacts(contacts):
    print("\n--- Search Contact ---")
    query = input("Search by name or phone number: ").strip().lower()
    found = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    if not found:
        print("No contact found.")
    else:
        for contact in found:
            print(
                f"\nName: {contact['name']}\n"
                f"Phone: {contact['phone']}\n"
                f"Email: {contact['email']}\n"
                f"Address: {contact['address']}\n"
            )

def update_contact(contacts):
    print("\n--- Update Contact ---")
    name_to_update = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == name_to_update:
            print("Leave field blank to keep the current value.")
            new_phone = input(f"New phone number [{contact['phone']}]: ").strip()
            new_email = input(f"New email [{contact['email']}]: ").strip()
            new_address = input(f"New address [{contact['address']}]: ").strip()
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address
            save_contacts(contacts)
            print(f"Contact '{contact['name']}' updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter the name of the contact to delete: ").strip().lower()
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name_to_delete:
            deleted = contacts.pop(i)
            save_contacts(contacts)
            print(f"Contact '{deleted['name']}' deleted successfully!")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    print("Welcome to Contact Book!")
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Select an option: ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Thank you for using Contact Book! Goodbye.")
            break
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main() 
    