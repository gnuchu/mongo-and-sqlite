from customer import Customer
import sqlite3

def get_database():
  from pymongo import MongoClient
  import pymongo

  CONNECTION_STRING = "mongodb://127.0.0.1:27017"

  from pymongo import MongoClient
  client = MongoClient(CONNECTION_STRING)

  return client['customer-database']

if __name__ == "__main__":
  mongo_dbname = get_database()
  
  mongo_collection = mongo_dbname['customer-data-items']
  
  sql_connection = sqlite3.connect("db/test.db")

  items = mongo_collection.find()
  for record_count, item in enumerate(items):
    customer_name = item['name']
    customer_address = item['address']
    customer_notes = item['notes']
    customer_created_at = item['created_at']

    sql_command = 'insert into customers (name, address, notes, created_at) values (?,?,?,?)'
    sql_connection.execute(sql_command, (customer_name, customer_address, customer_notes, customer_created_at))

    #Commit every 50 records. Not entriely necessary but some records you might have to manage your transactions.
    if (record_count % 50) == 0:
      sql_connection.commit()

