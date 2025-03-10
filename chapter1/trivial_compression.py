
class CompressedGene:
    
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1

        for nucleotide in gene.upper():
            self.bit_string <<= 2 # move 2 bits to left

            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))

    def decompress(self) -> str:

        gene: str = ""

        for i in range(0, self.bit_string.bit_length() -1, 2):
            bits: int = self.bit_string >> i & 0b11

            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"       
            else:
                raise ValueError("Invalid bits: {}".format(bits))       

        return gene[::-1]  

if __name__ == "__main__":
    
    from sys import getsizeof
    original:str = "TAGGGATTAACCGTTATATATATATAGC" * 100

    print("original value = {}".format(original))
    print("original is {} bytes".format(getsizeof(original)))

    compressed : CompressedGene = CompressedGene(original)
    print("compressed value = {}".format(compressed.decompress()))
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    
