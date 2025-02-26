from PIL import Image
import numpy as np


# Hide data in image
def encode_image(img_path, data, output_path):
    img = Image.open(img_path)
    img_array = np.array(img)

    # Convert data to binary
    binary_data = ''.join(format(byte, '08b') for byte in data)
    data_len = len(binary_data)

    # Modify pixel LSBs
    idx = 0
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  # RGB channels
                if idx < data_len:
                    img_array[i, j, k] = (img_array[i, j, k] & 0xFE) | int(binary_data[idx])
                    idx += 1

    # Save encoded image
    encoded_img = Image.fromarray(img_array)
    encoded_img.save(output_path)
    print("Data hidden successfully!")


# Extract data from image
def decode_image(img_path, data_length):
    img = Image.open(img_path)
    img_array = np.array(img)

    binary_data = ""
    idx = 0
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):
                if idx < data_length * 8:
                    binary_data += str(img_array[i, j, k] & 1)
                    idx += 1

    # Convert binary to bytes
    byte_data = int(binary_data, 2).to_bytes(len(binary_data) // 8, byteorder="big")
    return byte_data


# Example Usage
img_path = r"C:\Users\saipr\PycharmProjects\pythonProject\hide.jpg"  # Use raw string or double backslashes
output_path = r"C:\Users\saipr\PycharmProjects\pythonProject\encoded.jpg"
data = b"hi praneethuu"

encode_image(img_path, data, output_path)

# Extract and print the hidden message
retrieved_data = decode_image(output_path, len(data))
print("Decoded Message:", retrieved_data.decode())


def decode_image(img_path, data_length):
    img = Image.open(img_path)
    img_array = np.array(img)

    binary_data = ""
    idx = 0
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  # RGB channels
                if idx < data_length * 8:
                    binary_data += str(img_array[i, j, k] & 1)
                    idx += 1

    # Convert binary to bytes
    byte_data = int(binary_data, 2).to_bytes(len(binary_data) // 8, byteorder="big")
    return byte_data

# Example Usage
retrieved_data = decode_image(output_path, len(data))
print("🔓 Decoded Message:", retrieved_data.decode())
