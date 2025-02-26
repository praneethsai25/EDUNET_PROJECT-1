from cryptography.fernet import Fernet

# Generate and save a key (do this once and reuse the key)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt message
def encrypt_message(message, key):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Decrypt message
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

# Generate Key (Only Run Once)
generate_key()

# Load Key
key = load_key()

# Original message
message = "This is a secret message."

# Encrypt the message
encrypted_message = encrypt_message(message, key)

# Encode encrypted message in image
encode_image("hide.png", encrypted_message, "encoded.png")

# Extract the hidden data
retrieved_data = decode_image("encoded.png", len(encrypted_message))

# Decrypt the extracted data
decrypted_message = decrypt_message(retrieved_data, key)

print("Decrypted Message:", decrypted_message)


