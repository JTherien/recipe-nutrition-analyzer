import sqlite3

from libs.config import get_config
from libs.database import create_connection
from libs.database import create_table

config = get_config()

food_db = config['food-db-path']

conn = create_connection(food_db)

sql_create_ingredients_table = """CREATE TABLE IF NOT EXISTS ingredients (
    id integer PRIMARY KEY,
    usda_ingredient text NOT NULL,
    local_ingredient_terms text NOT NULL
);"""

sql_create_conversions_table = """CREATE TABLE IF NOT EXISTS conversions (
    id integer PRIMARY KEY,
    ingredient_name text NOT NULL,
    unit_of_measurement text NOT NULL,
    grams real NOT NULL
);"""

if conn is not None:

    create_table(conn, sql_create_ingredients_table)

    create_table(conn, sql_create_conversions_table)

    conn.close()

else:

    print('Error! Cannot create the database connection.')
