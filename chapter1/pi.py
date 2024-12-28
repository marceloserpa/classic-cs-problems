
# Leibniz formula to calculate PI

def calculate_pi(n_terms :int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi:float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0 # force to alternate between sum and subtract

    return pi

if __name__ == "__main__":
    result :float = calculate_pi(1000000000)
    print(f'{result}')