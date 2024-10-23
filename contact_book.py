class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contact found with the name '{name}'.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter the name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()