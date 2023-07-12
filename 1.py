import random
import string

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length=10):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    def add_password(self, website, username, password):
        self.passwords[website] = {'username': username, 'password': password}
        print(f"Password added for {website}")

    def get_password(self, website):
        if website in self.passwords:
            return self.passwords[website]['password']
        else:
            return None

    def remove_password(self, website):
        if website in self.passwords:
            del self.passwords[website]
            print(f"Password removed for {website}")
        else:
            print("Password not found for the given website.")

    def list_passwords(self):
        print("Website\t\tUsername\t\tPassword")
        print("----------------------------------------------")
        for website, data in self.passwords.items():
            username = data['username']
            password = data['password']
            print(f"{website}\t\t{username}\t\t{password}")

# Example usage
manager = PasswordManager()

print("Welcome to the Password Manager!")
while True:
    print("\nAvailable commands:")
    print("1. Generate Password")
    print("2. Add Password")
    print("3. Get Password")
    print("4. Remove Password")
    print("5. List Passwords")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        length = int(input("Enter password length: "))
        password = manager.generate_password(length)
        print(f"Generated password: {password}")
    elif choice == "2":
        website = input("Enter website: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        manager.add_password(website, username, password)
    elif choice == "3":
        website = input("Enter website: ")
        password = manager.get_password(website)
        if password:
            print(f"Password for {website}: {password}")
        else:
            print(f"No password found for {website}.")
    elif choice == "4":
        website = input("Enter website: ")
        manager.remove_password(website)
    elif choice == "5":
        manager.list_passwords()
    elif choice == "6":
        print("Exiting Password Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
