def get_user_details():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    return name, email

def main():
    print("Club Members Registration Form")
    members = []

    while True:
        choice = input("Do you want to register a new member? (yes/no): ").lower()

        if choice != 'yes':
            break

        name, email = get_user_details()
        members.append({"Name": name, "Email": email})
        print("Member registered successfully!\n")

    # Save members' details to a file
    with open("members.txt", "a") as file:
        for member in members:
            file.write(f"Name: {member['Name']}, Email: {member['Email']}\n")

if __name__ == "__main__":
    main()

