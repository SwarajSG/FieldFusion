# migrate_fields.py

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Adjust the URL if necessary
db = client['FFlogin']  # Replace with your database name
collection = db['FFlogin1']  # Replace with your collection name

# Add a new field to all documents
collection.update_many({}, { "$set": { "newField": "defaultValue" } })

# Rename an existing field
collection.update_many({}, { "$rename": { "oldFieldName": "newFieldName" } })

# Remove a field from all documents
collection.update_many({}, { "$unset": { "oldFieldToRemove": "" } })

# Perform any other migration logic...
print("Migration completed successfully!")