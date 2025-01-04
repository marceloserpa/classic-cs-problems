from enum import IntEnum
from typing import Tuple, List
from bisect import bisect_left

Nucleotide: IntEnum = IntEnum("Nucleotide", ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGTTTATATATATCCCTAGGATCTCCCTTT"

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if(i + 2) >=len(s):
            return gene
        
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)

    return gene

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1

    while low <= high: # verify the searchable area
        mid: int = (low + high) // 2 # low + high calculate the searchable area

        if gene[mid] < key_codon:
            low = mid + 1 # resize the searchableare and use +1 is to skip the current element since it is not equal the searched element
        elif gene[mid] > key_codon:
            high = mid - 1 # the same 
        else:
            return True
    return False

def bisect_contains(gene: Gene, key_codon: Codon) -> bool:
    index: int = bisect_left(gene, key_codon)
    if index != len(gene) and gene[index]  == key_codon:
        return index
    return -1


            
my_gene: Gene = string_to_gene(gene_str)
print(my_gene)

print("Linear search")

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

print(linear_contains(my_gene, acg))

print(linear_contains(my_gene, gat))

print("Binary search")

sorted_gene: Gene = sorted(string_to_gene(gene_str))
print(sorted_gene)

print(binary_contains(sorted_gene, acg))

print(binary_contains(sorted_gene, gat))


print("Binary search using Bisect")

sorted_gene: Gene = sorted(string_to_gene(gene_str))
print(sorted_gene)

print(bisect_contains(sorted_gene, acg))

print(bisect_contains(sorted_gene, gat))