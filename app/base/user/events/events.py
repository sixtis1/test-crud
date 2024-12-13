from dataclasses import dataclass


@dataclass
class UserCreatedEvent:
    user_id: int
    full_name: str