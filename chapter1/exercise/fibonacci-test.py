from time import perf_counter

import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_performance_recursive_solution(self):
        """
        Test to retrieve the nth element from fibonacci sequence
        """

        time_start = perf_counter()
        

        result = fibonacci.fib1(40)

        time_duration = perf_counter() - time_start

        print(f'Recursive Solution={time_duration}')

        self.assertEqual(result, 102334155)

    def test_performance_binet_solution(self):
        """
        Test to retrieve the nth element from fibonacci sequence
        """

        time_start = perf_counter()
        

        result = fibonacci.fib_binet(40)

        time_duration = perf_counter() - time_start

        print(f'Binet Solution={time_duration}')

        self.assertEqual(result, 102334155)        




if __name__ == '__main__':
    unittest.main()