from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractclassmethod

V = TypeVar('V')
D = TypeVar('D')

class Constraint(Generic[V, D], ABC):

    def __init__(self, variables: List[V]) -> None:
        self.variables  = variables

    @abstractclassmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


class CSP(Generic[V, D]):

    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:

        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V,D]]] = {}

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False

        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:

        # base case: ensure that all variables are assigned
        if len(assignment) == len(self.variables):
            return assignment

        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # find the first variable that was not assigned to test against alll domains
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assigment = assignment.copy()
            local_assigment[first] = value

            if self.consistent(first, local_assigment):

                # if consistent it will continue to search for new assignment
                result : Optional[Dict[V,D]] = self.backtracking_search(local_assigment)

                if result is not None:
                    return result

        return None

    

        
