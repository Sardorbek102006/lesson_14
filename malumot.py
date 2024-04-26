import psycopg2

date_base = psycopg2.connect(
    host='cornelius.db.elephantsql.com',
    user='hngkeojs',
    database='hngkeojs',
    password='yOSfdHUqN8bnqWIY4ukzMWoDWS-BnxiV'
)

cursor = date_base.cursor()

def infor(laptop_name, laptop_image, laptop_price, credit_price):
    cursor.execute(f"""
            INSERT INTO new_project(laptop_name, laptop_image, laptop_price, credit_price)
            VALUES
            ('{laptop_name}', '{laptop_image}', '{laptop_price}', '{credit_price}')
    """)
    date_base.commit()


cursor.execute("""
    SELECT * FROM new_project
""")

rows = cursor.fetchall()

for row in rows:
    print(row)