from csp import Constraint, CSP
from typing import Dict, List, Optional

class MapColoringConstraint(Constraint[str, str]):

    def __init__(self, place1: str, place2: str) -> None:

        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        
        # if the place not in assignment is not possible to define yet
        if self.place1 not in assignment or self.place2 not in assignment:
            return True

        # verift if the color is different
        return assignment[self.place1] != assignment[self.place2]
        

if __name__ == "__main__":
    variables: List[str] = ["Western Australia", "Northern Territory", "South Australia", "Queensland", "New South Wales", "Victoria", "Tasmania"]
    domains: Dict[str, List[str]] = {}

    for variable in variables:
        domains[variable] = ["red", "green", "blue"]

    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(MapColoringConstraint("Western Australia", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Western Australia", "South Australia"))
    csp.add_constraint(MapColoringConstraint("South Australia", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Queensland", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("New South Wales", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))


solution: Optional[Dict[str, str]] = csp.backtracking_search()

if solution is None:
    print("Solution not found")

else:
    print(solution)