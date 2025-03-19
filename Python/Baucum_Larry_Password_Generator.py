import random
import string
import time

#Larry Baucum
#3/11/2025
#Final Project

def pass_gen():
    length = 12

    # Create pools of characters to ensure each criteria is met
    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special_chars = string.punctuation

    # Ensure the password has at least one of each required character type
    rand_pass = [
        random.choice(digits),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(special_chars)
    ]

    # Fill the remaining length of the password with a mix of all character types
    all_chars = digits + lowercase + uppercase + special_chars
    rand_pass += [random.choice(all_chars) for _ in range(length - 4)]

    # Shuffle the generated password to ensure a random order
    random.shuffle(rand_pass)

    # Convert the list to a string
    rand_pass = ''.join(rand_pass)

    user_pass = input("Enter a password that meets the requirements if you like:")
 
    print("Your auto-generated password: ", rand_pass)
    print("Your user-generated password: ", user_pass)

    # Ensure user_pass is a string, even if it's empty
    if len(user_pass) < 1:
        user_pass = ""

    return rand_pass, user_pass


def pass_ver(rand_pass, user_pass):
    def evaluate_strength(password):
        criteria_met = 0
        missing_criteria = []

        if len(password) >= 12:
            criteria_met += 1
        else:
            missing_criteria.append("Length of at least 12 characters")

        if any(char.islower() for char in password):
            criteria_met += 1
        else:
            missing_criteria.append("Lowercase letter")

        if any(char.isupper() for char in password):
            criteria_met += 1
        else:
            missing_criteria.append("Uppercase letter")

        if any(char.isdigit() for char in password):
            criteria_met += 1
        else:
            missing_criteria.append("Number")

        if any(char in string.punctuation for char in password):
            criteria_met += 1
        else:
            missing_criteria.append("Special character")

        if criteria_met <= 2:
            strength = f"Weak: Password meets only {criteria_met} out of 5 criteria."
        elif criteria_met == 3 or criteria_met == 4:
            strength = f"Moderate: Password meets {criteria_met} out of 5 criteria."
        elif criteria_met == 5:
            strength = f"Strong: Password meets all {criteria_met} criteria."
        else:
            strength = "Undefined Strength"

        return strength, missing_criteria

    user_strength, user_missing_criteria = evaluate_strength(user_pass)
    rand_strength, rand_missing_criteria = evaluate_strength(rand_pass)

    print(f"User Password Strength: {user_strength}")
    if user_missing_criteria:
        print("Missing criteria for user password:", ", ".join(user_missing_criteria))

    print(f"Random Password Strength: {rand_strength}")
    if rand_missing_criteria:
        print("Missing criteria for random password:", ", ".join(rand_missing_criteria))

    return user_strength, user_missing_criteria, rand_strength, rand_missing_criteria




def mfa_otp(rand_pass, user_pass):
    def generate_otp():
        otp = ''.join(random.choices(string.digits, k=6))
        return otp

    def verify_otp(input_otp, actual_otp, expiration_time):
        current_time = time.time()
        if current_time > expiration_time:
            return False, "Failed: OTP has expired."
        if input_otp == actual_otp:
            return True, "Success: OTP verified."
        else:
            return False, "Failed: Incorrect OTP."

    while True:
        actual_otp = generate_otp()
        expiration_time = time.time() + 15  # OTP valid for 15 seconds

        print(f"Generated OTP (valid for 15 seconds): {actual_otp}")

        # Prompt for password and OTP
        input_password = input("Enter your password: ")
        input_otp = input("Enter OTP: ")
        is_verified, message = verify_otp(input_otp, actual_otp, expiration_time)

        # Verify password strength
        user_strength, user_missing_criteria, rand_strength, rand_missing_criteria = pass_ver(rand_pass, user_pass)

        # Check selected password strength
        if input_password == user_pass:
            pass_strength = user_strength
        elif input_password == rand_pass:
            pass_strength = rand_strength
        else:
            pass_strength = "Invalid password."

        print(message)
        if is_verified and pass_strength == "Strong: Password meets all 5 criteria.":
            print("Login successful!")
            break
        else:
            print("Login unsuccessful. Please try again.\n")



def main():
    
    print("Welcome to the password generator complete with MFA.\n Please accept an auto generated password or enter your own password.\n Your password must meet the following criteria:\n Uppercase Letter\n Lowercase Letter\n Number\n Special Character\n Length of 12\n")
    
    
    
    user_pass, rand_pass = pass_gen()

    user_pass = str(user_pass)
    rand_pass = str(rand_pass)

    pass_ver(user_pass, rand_pass)

    mfa_otp(rand_pass, user_pass)


if __name__ == "__main__":
    main()

