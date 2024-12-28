
from typing import Dict

class BitStringWrapper:

    def __init__(self) -> None:
        self._value: int = 1 # it avoid to print a extra character

        # map all the possibilities
        self._letter_to_binary: Dict[str, int] = {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}
        self._binary_to_letter: Dict[int, str] = {0b00: "A", 0b01:"C", 0b10: "G", 0b11: "T"}

        possible_elements: int = len(self._binary_to_letter)
        possible_elements_round: int = possible_elements - (possible_elements % 2)

        self._shift: int = int(possible_elements_round / 2)
        print(self._shift)

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

    def get_size(self) -> int:
        return getsizeof(self._value)


class CompressedGene:
    
    def __init__(self, gene: str) -> None:
        self._bit_string: BitStringWrapper = BitStringWrapper()
        self._compress(gene)

    
    def _compress(self, gene: str) -> None:
        for nucleotide in gene.upper():
            self._bit_string.append(nucleotide)

    def decompress(self) -> str:
        bit_string_interable = iter(self._bit_string)
        gene = ""
        for nucleotide in bit_string_interable:
            gene += nucleotide
        return gene

    def get_size(self) -> int:
        return self._bit_string.get_size()



if __name__ == "__main__":
    
    from sys import getsizeof
    original:str = "TAGGGATTAACCGTTATATATATATAGC" * 100

    print("original value = {}".format(original))
    print("original is {} bytes".format(getsizeof(original)))

    compressed : CompressedGene = CompressedGene(original)
    print("compressed value = {}".format(compressed.decompress()))
    print("compressed is {} bytes".format(compressed.get_size()))