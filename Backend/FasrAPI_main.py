from fastapi import FastAPI
import csv

app = FastAPI()

# Load CSV data
csv_file = '/Users/aman_bitian/PycharmProjects/basicStrockScreener/data/tickers_name_mapping.csv'
data = []

with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file);
    data = list(reader)

@app.get("/get_value/{item_id}")
def read_item(item_id: int):
    if item_id < 1 or item_id > len(data):
        return {"error": "Item not found"}
    return data[item_id - 1]
