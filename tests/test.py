from dataclasses import dataclass, asdict
from typing import TypedDict

# Define the TypedDict for type hints
class PersonDict(TypedDict):
    name: str
    age: int

# Define the dataclass
@dataclass
class Person:
    name: str
    age: int

    # Method to convert dataclass to dictionary
    def to_dict(self) -> PersonDict:
        return asdict(self)  # Returns a dictionary representation

# Example usage
person_instance = Person(name="Alice", age=30)
person_dict: PersonDict = person_instance.to_dict()

print(person_dict)  # Output: {'name': 'Alice', 'age': 30}
