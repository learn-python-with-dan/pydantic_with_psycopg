
__all__ = [
    'insert_user_stmt',
    'get_user_stmt',
    'insert_transaction_stmt',
    'get_transaction_stmt',
]


insert_user_stmt = """
    INSERT INTO users (id, name) VALUES (%(id)s, %(name)s)
    RETURNING id
"""

get_user_stmt = """
    SELECT * FROM users WHERE id = %(id)s
"""

insert_transaction_stmt = """
    INSERT INTO transactions (id, amount, payer_id, payee_id) VALUES (%(id)s, %(amount)s, %(payer_id)s, %(payee_id)s)
    RETURNING id
"""

get_transaction_stmt = """
    SELECT 
        t.*,
        row_to_json(u1.*) payer,
        row_to_json(u2.*) payee
    FROM transactions t
    JOIN users u1 ON t.payer_id = u1.id
    JOIN users u2 ON t.payee_id = u2.id
"""
