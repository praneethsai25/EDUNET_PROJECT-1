Secure Data Hiding in Image Using Steganography![image](https://github.com/user-attachments/assets/dc805758-5865-4826-a188-cd2a88e936ed)


### **Image-Based Text Encryption & Decryption 🔒**


## 📌 Overview

This project hides a **secret message** inside an image using **pixel manipulation** and retrieves it later using a **passcode-based decryption** system. It modifies the **RGB values of pixels** to store ASCII values of characters in the image.

## 📚 Project Structure

```
📁 Image-Encryption
📀 FINAL_RUN.py  # Main script for encoding & decoding
🎨 hide.jpg            # Image used for encoding message
📚 README.md           # Project documentation
```

## ⚙️ How It Works

1. **Encoding Phase**

   - User enters a **secret message**.
   - User sets a **passcode** to protect the message.
   - The message characters are **converted to ASCII** and stored inside the image pixels.

2. **Decoding Phase**

   - The user provides the correct passcode.
   - The script reads the **hidden ASCII values** and converts them back to text.
   - If the passcode is correct, the secret message is revealed.

---

## 🚀 Setup & Installation

### 1️⃣ **Prerequisites**

Ensure you have **Python 3+** installed. Install required dependencies:

```bash
pip install opencv-python
```

### 2️⃣ **Running the Encryption Script**

```bash
python FINAL_RUN.py
```

- Enter your **secret message** and a **passcode** when prompted.
- The image with the hidden message will be saved as **`hide.jpg`**.
- Enter the **correct passcode** to retrieve the hidden message.



---

## 📝 Code Explanation

### ✅ **Key Components**

- `cv2.imread("hide.jpg")` → Reads the image for encoding.
- `char_to_ascii` → Converts characters to ASCII.
- `ascii_to_char` → Converts ASCII back to characters.


### 🔑 **Passcode Mechanism**

- User sets a **passcode** during encryption.
- During decryption, the script asks for the passcode.
- If it matches, the message is displayed; otherwise, access is denied.

---

## 🛠️ Possible Improvements

🔹 Add a **GUI for easy use**.\
🔹 Use **LSB Steganography** for better security.\
🔹 Implement **support for larger messages**.

---

## 📝 Author

👨‍💻 **Sai Praneeth Yamagani**\
📧 [praneethsai520@gmail.com](mailto\:your.email@example.com)\
🔗 GitHub: [https://github.com/praneethsai25/EDUNET_PROJECT-1](https://github.com/YourGitHubProfile)

---

🚀 **Enjoy encrypting your secret messages!** 🔏

