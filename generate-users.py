import mysql.connector
from faker import Faker
from config import ConfigFake

fake = Faker()
mydb = mysql.connector.connect(
    host='192.168.88.100',
    user = "monty",
    password = "debian1",
    database = "socapp"
)

mycursor = mydb.cursor()

for _ in range(1000):
    username = fake.user_name()
    password = fake.password()
    email = fake.email()
    name = fake.first_name()
    lastname = fake.last_name()
    city = fake.city()
    birth_date = fake.date()
    mycursor.execute(
        'INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s, NULL, %s, NULL, %s, NULL)',
        (
            username,
            password,
            email,
            name,
            lastname,
            city,
            birth_date
        )
    )
    mydb.commit()

