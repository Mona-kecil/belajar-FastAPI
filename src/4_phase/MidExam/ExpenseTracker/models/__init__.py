from .connection import get_connection
conn = get_connection()

create_user_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(30) NOT NULL UNIQUE,
    email VARCHAR(50) NOT NULL UNIQUE,
    hashed_password VARCHAR(100) NOT NULL
);
'''

create_transaction_table_query = '''
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    amount NUMERIC(10, 2) NOT NULL,
    date DATE NOT NULL,
    category VARCHAR(10) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CHECK (amount > 0),
    CHECK (category IN ('income', 'expense'))
);
'''

with conn.cursor() as cursor:
    cursor.execute(create_user_table_query)
    cursor.execute(create_transaction_table_query)
    conn.commit()

    print('Tables created successfully!')
    print('if it isn\'t initialized yet..')
