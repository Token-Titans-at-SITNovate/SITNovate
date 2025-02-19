from cryptography.fernet import Fernet

# Step 1: Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()

# Step 2: Initialize Fernet with the key
cipher = Fernet(key)

# Step 3: Read the encrypted message from file
with open("ciphertext.txt", "rb") as encrypted_file:
    encrypted_message = encrypted_file.read()

# Step 4: Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)

# Step 5: Print or save the decrypted message
print("Decrypted Message:", decrypted_message.decode())
