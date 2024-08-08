from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI()
fake = Faker()

file_name = 'backend/fakeapi/products_clean.csv'
df = pd.read_csv(file_name)
df['index'] = range(1, len(df) + 1)
df.set_index('index', inplace=True)

@app.get("/gerar_compra/{register_number}")
async def gerar_compra(register_number: int):

    if register_number < 1:
        return {"error": "The number must be greater than one"}

    requests = []
    for _ in range(register_number):
        index = random.randint(1, len(df) - 1)
        tuple = df.loc[index]
        print(type(tuple["EAN"]))
        transaction = {
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": tuple["Product"],
            "ean": str(tuple["EAN"]),
            "price": round(float(tuple["Price"]*1.2), 2),
            "store": 11,
            "dateTime": fake.iso8601(),
            "clientPosition": fake.location_on_land()
            }
        requests.append(transaction)

    return requests