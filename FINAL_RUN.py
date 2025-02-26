import cv2
import os

# Load the image
img = cv2.imread("hide.jpg")  # Ensure "hide.jpg" is in the correct path

# Get user input for message and passcode
message = input("Enter secret message: ")
passcode = input("Enter a passcode: ")  # Store passcode entered during encryption

# Create ASCII mappings
char_to_ascii = {chr(i): i for i in range(255)}
ascii_to_char = {i: chr(i) for i in range(255)}

# Encoding the message into the image
n, m, z = 0, 0, 0  # Pixel position counters
for char in message:
    img[n, m, z] = char_to_ascii[char]
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycles through RGB channels

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Opens the image on Windows

# Decryption process
decrypt_passcode = input("Enter passcode for decryption: ")
decrypted_message = ""

if decrypt_passcode == passcode:  # Ensure entered passcode matches original
    n, m, z = 0, 0, 0  # Reset counters for decryption
    for _ in range(len(message)):
        decrypted_message += ascii_to_char[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycles through RGB channels

    print("Decrypted message:", decrypted_message)
else:
    print("ERROR: Incorrect passcode! Access denied.")
