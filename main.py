from psycopg import Connection
from psycopg.conninfo import make_conninfo

from src.crud import CRUD
from src.models import *


conn_info = make_conninfo(host='localhost', port=5432, dbname='postgres')

with Connection.connect(conninfo=conn_info, options='-c search_path=demo') as conn:

    crud = CRUD(conn)

    user_input_1 = UserInput(name='Dan')
    user_input_2 = UserInput(name='Ann')

    user_id_1 = crud.insert_user(user_input_1)
    user_id_2 = crud.insert_user(user_input_2)

    user_1 = crud.get_user(user_id_1)
    user_2 = crud.get_user(user_id_2)

    print(user_1.model_dump())
    print(user_2.model_dump())

    transaction_input = TransactionInput(amount=10, payer_id=user_1.id, payee_id=user_2.id)
    transaction_id = crud.insert_transaction(transaction_input)

    transaction = crud.get_transaction(transaction_id)

    print(transaction.model_dump())
