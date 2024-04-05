
CREATE TABLE IF NOT EXISTS users (
    id CHAR(32) PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS transactions (
    id CHAR(32) PRIMARY KEY,
    amount DECIMAL NOT NULL,
    payer_id CHAR(32) REFERENCES users(id) NOT NULL,
    payee_id CHAR(32) REFERENCES users(id) NOT NULL
);
