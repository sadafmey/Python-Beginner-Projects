class Guestbook:
    def __init__(self):
        self.entries = []

    def add_entry(self, name, message):
        """Add a new entry to the guestbook."""
        entry = {'name': name, 'message': message}
        self.entries.append(entry)

    def view_entries(self):
        """View all entries in the guestbook."""
        if not self.entries:
            print("The guestbook is empty.")
        else:
            print("Guestbook Entries:")
            for i, entry in enumerate(self.entries, 1):
                print(f"{i}. Name: {entry['name']}, Message: {entry['message']}")


def main():
    guestbook = Guestbook()

    while True:
        print("\nMenu:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name = input("Enter your name: ")
            message = input("Enter your message: ")
            guestbook.add_entry(name, message)
            print("Entry added successfully!")
        elif choice == '2':
            guestbook.view_entries()
        elif choice == '3':
            print("Thank you for using the guestbook. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
