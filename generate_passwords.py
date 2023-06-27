import string
import keyboard
import time


time.sleep(5)

def send_message(message, num_times):
    for _ in range(num_times):
        keyboard.write(message)
        keyboard.press_and_release("enter")

def generate_passwords():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password_length = 1

    while password_length <= 15:
        count = 0
        for password in generate_combinations(all_characters, password_length):
            send_message(password, 1)
            print(password)
            count += 1

        print(f"Number of combinations for {password_length}-character password: {count}")
        password_length += 1

def generate_combinations(characters, length):
    if length == 1:
        for char in characters:
            yield char
    else:
        for char in characters:
            for suffix in generate_combinations(characters, length - 1):
                yield char + suffix

generate_passwords()
