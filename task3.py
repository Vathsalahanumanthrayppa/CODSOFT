# Contact Management System

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added successfully.\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    print("Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")
    print()

def search_contacts(contacts):
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [
        c for c in contacts
        if search_term in c['name'].lower() or search_term in c['phone']
    ]
    if not found_contacts:
        print("No matching contacts found.\n")
        return
    print("Search Results:")
    for contact in found_contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}\n")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Enter new details (leave blank to keep current):")
            new_name = input(f"New name [{contact['name']}]: ") or contact['name']
            new_phone = input(f"New phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"New email [{contact['email']}]: ") or contact['email']
            new_address = input(f"New address [{contact['address']}]: ") or contact['address']
            contact.update({
                'name': new_name,
                'phone': new_phone,
                'email': new_email,
                'address': new_address
            })
            print("Contact updated successfully.\n")
            return
    print("Contact not found.\n")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            del contacts[i]
            print("Contact deleted successfully.\n")
            return
    print("Contact not found.\n")

def main():
    contacts = []
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

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
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()