from typing import List
from math import exp

# calculate the dot product of two vectors
def dot_product(xs: List[float], ys: List[float]) -> float:
    return sum(x * y for x,y in zip(xs, ys))

def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))

def derivate_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)


# feature scaling: normalize the value to 0/1
def normalize_by_feature_scaling(dataset:List[List[float]]) -> None:
    for col_num in range(len(dataset[0])):
        column: List[float] = [row[col_num] for row in dataset]
        maximum = max(column)
        minimum = min(column)
        
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = (dataset[row_num][col_num] - minimum ) / (maximum - minimum)    