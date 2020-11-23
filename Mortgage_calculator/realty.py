"""
Realty provides functionality to ...

use Realty.calculate_mortage_monthly_payment to ...
...
"""

class Realty:
    def __init__(self, name: str, area: float):
        """one-liner description

        @param :name: - 
        === Header level 3
        I want to say that:
        -a
        -b
        -c

        area - size of property in square meters
        :param area:
        """
        if not area:
            raise ValueError("area should be set amd it should be a positive float value")
        self.name = name
        self.area = area

    def greet(self):
        greeting = f"Hello, {self.name}"
        return greeting

    @staticmethod
    def calculate_monthly_payment(value: float, years: int, interest: float) -> float:
        monthly_interest = interest / 12
        complex_interest = (1.0 + monthly_interest) ** (years * 12)
        monthly_payment = value * monthly_interest * complex_interest / (overall_interest - 1.0)
        return monthly_payment

    @classmethod
    def load_from_file(cls, filepath: str):
        with open(filepath) as fin:
            name, area = fin.read().strip().split()
            area = float(area)
        realty = cls(name=name, area=area)
        return realty

    def __repr__(self):
        repr_ = f"{self.__class__.__name__}(name='{self.name}', area={self.area})"
        return repr_

    def __eq__(self, rhs):
        outcome = (
            (self.name == rhs.name)
            and (self.area == rhs.area)
        )
        return outcome
