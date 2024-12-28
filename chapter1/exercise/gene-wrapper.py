
from typing import Dict

class BitStringWrapper:

    def __init__(self) -> None:
        self._value: int = 1 # it avoid to print a extra character
        self._shift: int = 2 # in this moment is FIXED but it should be dynamic

        # map all the possibilities
        self._letter_to_binary: Dict[str, int] = {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}
        self._binary_to_letter: Dict[int, str] = {0b00: "A", 0b01:"C", 0b10: "G", 0b11: "T"}

    def append(self, letter: str) -> None:
        self._value <<= self._shift
        self._value |= self._letter_to_binary[letter]

    def get_binary(self) -> int:
        return self._value

    def __iter__(self):
        # it force to start in the highest position
        self.current = (self._value.bit_length() // self._shift - 1) * self._shift
        
        return self

    def __next__(self):

        if self.current < 0:
            raise StopIteration

        bits: int = (self._value >> self.current ) & 0b11
        result: str = self._binary_to_letter[bits]
        self.current -= self._shift

        return result  


if __name__ == "__main__":
    
    from sys import getsizeof
    gene:str = "TAGGGATTAACCGTTATATATATATAGC" * 100

    bit = BitStringWrapper()
    for nucleotide in gene.upper():
        bit.append(nucleotide)

    print("*****")

    print(bit.get_binary())



    myiter = iter(bit)
    decompressed = ""
    for x in myiter:
        decompressed += x

    print(gene)
    print("---")
    print(decompressed)