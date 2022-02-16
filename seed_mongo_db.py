from faker import Faker 
from datetime import datetime
from customer import Customer

def get_database():
  from pymongo import MongoClient
  import pymongo

  CONNECTION_STRING = "mongodb://127.0.0.1:27017"

  from pymongo import MongoClient
  client = MongoClient(CONNECTION_STRING)

  return client['customer-database']
    

if __name__ == "__main__":    
  dbname = get_database()
  fake = Faker()

  customers = []

  for _ in range(5001):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    customer = Customer(fake.name(), fake.address(), fake.text(), now)
    customers.append(customer.to_document())
  
  collection = dbname['customer-data-items']
  collection.insert_many(customers)

