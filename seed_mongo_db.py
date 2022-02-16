from faker import Faker 
from datetime import datetime
from customer import Customer
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://127.0.0.1:27017"

def get_database():
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

