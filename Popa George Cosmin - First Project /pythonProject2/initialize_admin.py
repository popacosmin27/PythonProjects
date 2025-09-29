import json
import os
import hashlib


def initialize_admin():
    # Admin credentials
    admin_username = "admin"
    admin_password = "admin123"

    # Create hashed password
    hashed_password = hashlib.sha256(admin_password.encode()).hexdigest()

    # Create users dictionary
    users = {
        admin_username: hashed_password
    }

    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Save users to JSON file
    try:
        with open('data/users.json', 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2)
        print(f"""
Admin user has been successfully created!

Username: {admin_username}
Password: {admin_password}

Please save these credentials and delete this file after use.
        """)
    except IOError as e:
        print(f"Error saving user data: {str(e)}")


if __name__ == "__main__":
    initialize_admin()