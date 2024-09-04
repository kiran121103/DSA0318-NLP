import re
text = "Hello, my email is example@example.com and my phone number is 123-456-7890."
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email_match = re.search(email_pattern, text)
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phone_match = re.search(phone_pattern, text)
print("Email:", email_match.group())
print("Phone Number:", phone_match.group())
