import random
import string
def check_user_password(user: str, password: str, dictionary: dict):
    for user1 in dictionary.keys():
        if user == user1:
            new_user = user + str(random.randint(0, 9))
            print(f"Username {user} is already taken. Suggested username: {new_user}.")
    for password1 in dictionary.values():
        if password == password1:
            letters = ''.join(random.choices(string.ascii_letters, k=2))
            number = str(random.randint(0, 9)) 
            new_password = password + letters + number
            print(f"Password {password} is already taken. Suggested password: {new_password}")


user_db = {
    "john_doe": "password123",
    "jane_smith": "securepass",
    "admin": "admin123",
    "guest": "guest123",
    "charlie_brown": "peanuts2023"
}
check_user_password("new_user", "securepass", user_db)
check_user_password("john_doe", "newpass", user_db)
