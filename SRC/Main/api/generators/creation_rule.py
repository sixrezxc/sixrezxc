from dataclasses import dataclass

@dataclass
class CreationRule:
    regex: str
    min_value: int | None = None
    max_value: int | None = None