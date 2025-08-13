import phonenumbers
from phonenumbers import geocoder, carrier

# Input phone number (with country code)
number = input("Enter phone number with country code (e.g. +14155552671): ")

try:
    phone_number = phonenumbers.parse(number)
    location = geocoder.description_for_number(phone_number, "en")
    network = carrier.name_for_number(phone_number, "en")
    print(f"The phone number {number} is located in: {location}")
    print(f"Carrier/Network: {network}")
except phonenumbers.NumberParseException:
    print("Invalid phone number!")
