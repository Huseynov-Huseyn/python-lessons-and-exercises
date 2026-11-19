from dataclasses import dataclass


# auto generate __init__, __repr__, __eq__ functions
@dataclass
class Book:
    title: str
    author: str
    num_pages: int
