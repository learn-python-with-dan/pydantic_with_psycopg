from uuid import uuid4

from pydantic import BaseModel, computed_field


__all__ = [
    'User',
    'UserInput',
    'Transaction',
    'TransactionInput',
]


class User(BaseModel):
    id: str
    name: str


class UserInput(BaseModel):
    name: str

    @computed_field
    def id(self) -> str:
        return uuid4().hex


class Transaction(BaseModel):
    id: str
    amount: float
    payer: User
    payee: User


class TransactionInput(BaseModel):
    amount: float
    payer_id: str
    payee_id: str

    @computed_field
    def id(self) -> str:
        return uuid4().hex
