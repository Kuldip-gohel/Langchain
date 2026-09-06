from typing import TypedDict

# Kind of create defination of our dict
class person(TypedDict):
    name : str
    age: int


# new_Person is type of person
new_Person: person = {"name":"Kuldip", "age":20}

print(new_Person)