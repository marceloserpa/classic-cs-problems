from PIL import Image
from secrets import token_bytes
from typing import Tuple
import base64

def random_key(length: int) -> Tuple[int, int]:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original_bytes: bytes) -> int:
    ##original_bytes :bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big") # big -> endianness

    encrypted :int = original_key ^ dummy # XOR

    return dummy, encrypted

def decrypt(key1 :int, key2 :int) -> str:
    decrypted: int = key1 ^ key2 # XOR

    # we need to sum 7 to rounding and make possible divide by 8
    return decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")

if __name__ == "__main__":
    
    filename = "kuriboh"
    image_bytes :bytes = ""

    with open(filename + ".png", "rb") as img_file:
        image_bytes = img_file.read() # it gets the image content and the file metadata

    key, encrypted = encrypt(image_bytes)
    print(encrypted)

    encrypted_b64 = base64.b64encode(encrypted.to_bytes((encrypted.bit_length() + 7) // 8, "big")).decode('utf-8')

    with open(filename + "-encrypted.txt", "w") as fp:
        fp.write(encrypted_b64)     

    #print(f'key={key} encrypted={encrypted}')

    with open(filename + "-encrypted.txt", "r") as fp:
        encrypted_b64 = fp.read()

    encrypted_bytes = base64.b64decode(encrypted_b64)
    encrypted_int = int.from_bytes(encrypted_bytes, "big")

    decoded = decrypt(key, encrypted_int)

    # Write the decrypted bytes back to a PNG file
    with open(filename + "-decrypted.png", "wb") as bin_file:
        bin_file.write(decoded)
