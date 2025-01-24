from demo.helper import generate_password, validate_password

def run_main():
    print("=== Password Generator and Validator ===")
    try:
        while True:
            choice = input("Do you want to generate a new password? (yes/no): ").strip().lower()
            if choice == "yes":
                try:
                    length = int(input("Enter the desired password length (minimum 6): ").strip())
                    password = generate_password(length)
                    if password:
                        print(f"Generated Password: {password}")
                        errors = validate_password(password)
                        if not errors:
                            print("Password is valid.")
                        else:
                            print("Password is invalid:")
                            for error in errors:
                                print(f"- {error}")
                except ValueError:
                    print("Input Error: Password length must be a valid number.")
        
            elif choice == "no":
                user_password = input("Enter your password to validate: ").strip()
                errors = validate_password(user_password)
                if not errors:
                    print("Password is valid.")
                if not user_password:
                    print("Validation Error: Password cannot be empty.")
                else:
                    for error in errors:
                        print(f"Validation Error: {error}")
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    except KeyboardInterrupt:
        print("Program interrupted.")

if __name__ == "__main__":
    run_main()