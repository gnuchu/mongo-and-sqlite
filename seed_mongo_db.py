from faker import Faker 
from datetime import datetime

class Customer:
  def __init__(self, name, address, notes, created_at):
    self.name = name
    self.address = address
    self.notes = notes
    self.created_at = created_at
  
  def to_document(self):
    return {
      "name": f"{self.name}",
      "address": f"{self.address}",
      "notes": f"{self.notes}",
      "created_at": f"{self.created_at}"
    }

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

