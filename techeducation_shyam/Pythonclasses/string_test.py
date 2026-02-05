import re
email = "test@gmail.com"
pattern = r"\w+@\w+\.\w"
if re.search(pattern, email):
 print("Valid email")
else:
 print("Invalid email")