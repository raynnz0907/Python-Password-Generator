import random
import string

def genarate_password(min_length, numbers = True, special_characters = True):
        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation

        characters = letters
        if numbers:
            characters += digits
        if special_characters:
            characters += special

        pwd = ""
        has_number = False
        has_special = False
        meets_criteria = False

        while not meets_criteria or len(pwd) < min_length:
            newchar = random.choice(characters)
            pwd += newchar

            if newchar in digits:
                has_number = True
            elif newchar in special:
                has_special = True

            meets_criteria = True
            if numbers:
                meets_criteria = has_number
            if special_characters:
                meets_criteria = meets_criteria and has_special

        return pwd


min_length = int(input("Enter the minimum length you want for your password: "))
numbers = input("Do you want to add numbers to your password?(y/n): ").lower() == "y"
special_characters = input("Do you want to add special characters?(y/n): ").lower() == "y"
password = genarate_password(min_length, numbers, special_characters)
print(password)
