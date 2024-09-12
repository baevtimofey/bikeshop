import dataclasses


@dataclasses.dataclass
class User:
    id: int
    name: str
    email: str
    password: str
