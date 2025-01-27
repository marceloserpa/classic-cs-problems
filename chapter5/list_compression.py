from __future__ import annotations
from genericpath import getsize
from typing import Tuple, List, Any
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm
from random import shuffle, sample
from copy import deepcopy
from zlib import compress
from sys import getsizeof
from pickle import dumps


PEOPLE: List[str] = ["Michael", "Sarah", "Joshua", "Narine", "David",
"Sajid", "Melanie", "Daniel", "Wei", "Dean", "Brian", "Murat", "Lisa"]

# Order can affect how the compression works. In this Genetic Algorithm we try to 
# find the best order to make the result smaller as possible 

class ListCompression(Chromosome):

    def __init__(self, list: List[Any]) -> None:
        self.list: List[Any] = list

    @property
    def bytes_compressed(self) -> int:
        return getsizeof(compress(dumps(self.list)))

    def fitness(self) -> float:
        return 1 / self.bytes_compressed

    # rearrenge the array the test a new order
    @classmethod
    def random_instance(cls) -> ListCompression:
        myList: List[str] = deepcopy(PEOPLE)
        shuffle(myList)
        return ListCompression(myList)

    def crossover(self, other: ListCompression) -> Tuple[ListCompression, ListCompression]:
        child1: ListCompression = deepcopy(self)
        child2: ListCompression = deepcopy(other)
        idx1, idx2 = sample(range(len(self.list)), k=2)
        l1, l2 = child1.list[idx1], child2.list[idx2]
        child1.list[child1.list.index(l2)], child1.list[idx2] = child1.list[idx2], l2
        child2.list[child2.list.index(l1)], child2.list[idx1] = child2.list[idx1], l1
        return child1, child2

    def mutate(self) -> None:
        idx1, idx2 = sample(range(len(self.list)), k=2)
        self.list[idx1], self.list[idx2] = self.list[idx2], self.list[idx1]

    def __str__(self) -> str:
        return f"Order: {self.list} Bytes: {self.bytes_compressed}"

if __name__ == "__main__":
    initial_population: List[ListCompression] = [ListCompression.random_instance() for _ in range(1000)]
    ga: GeneticAlgorithm[ListCompression] = GeneticAlgorithm(
        initial_population=initial_population, 
        threshold=1.0, 
        max_generations = 1000,
        mutation_chance = 0.2, 
        crossover_chance = 0.7, 
        selection_type=GeneticAlgorithm.SelectionType.TOURNAMENT)

    result: ListCompression = ga.run()
    print(result)