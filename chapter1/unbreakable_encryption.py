from secrets import token_bytes
from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> Tuple[int, int]:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original:str) -> int:
    original_bytes :bytes = original.encode()
    dummy: int = random_key(len(original))
    original_key = int.from_bytes(original_bytes, "big") # big -> endianness

    encrypted :int = original_key ^ dummy # XOR

    return dummy, encrypted

def decrypt(key1 :int, key2 :int) -> str:
    decrypted: int = key1 ^ key2 # XOR

    # we need to sum 7 to rounding and make possible divide by 8
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":
    
    name = "Marcelo Serpa"

    key, encrypted = encrypt(name)

    print(f'key={key} encrypted={encrypted}')

    decoded = decrypt(key, encrypted)
    print(f'decrypted = {decoded}')

