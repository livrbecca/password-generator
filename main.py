import random
print("welcome to your password generator")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTVXYZ0123456789!_-"

no_of_passwords = int(input("Number of passwords required?: "))
password_len = int(input("Numbers of characters required?: "))

print("\nhere are your passwords:")

for password in range(no_of_passwords):
  passwords = ""
  for c in range(password_len):
    passwords += random.choice(chars)
  print(passwords)