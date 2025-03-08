import random


def load_words(filename):
    try:
        with open(filename, "r") as file:
            words = [line.strip() for line in file if line.strip()]  # Remove empty lines
        if not words:
            raise ValueError("Word list is empty!")
        return words
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []


word_list = load_words("wordlist.txt")

def generate_password():
    if not word_list:
        return "WordListEmpty"  

    word = random.choice(word_list)  
    number = random.randint(1, 999999999)


    choice = random.choice(["word+num", "num+word", "word", "num"])

    if choice == "word+num":
        return f"{word}{number}"
    elif choice == "num+word":
        return f"{number}{word}"
    elif choice == "word":
        return word
    else:  
        return str(number)


with open("passwords.txt", "w") as file:
    for _ in range(100000):
        file.write(generate_password() + "\n")

print("Passwords saved to passwords.txt!")
