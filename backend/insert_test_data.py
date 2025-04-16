from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from flask_cors import CORS

# MongoDB connection with authentication
client = MongoClient('mongodb://root:pass@localhost:27017/')
db = client['ai_chat_db']
collection = db['documents']

# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example data
documents = [
    {"text": "What is AI?", "vector": None},
    {"text": "How does machine learning work?", "vector": None},
    {"text": "Explain deep learning.", "vector": None},
    {"text": "What is natural language processing?", "vector": None},
    {"text": "How do neural networks function?", "vector": None}
]

# Vectorize and store the documents
for doc in documents:
    doc['vector'] = model.encode(doc['text']).tolist()
    collection.insert_one(doc)

print("Test data inserted successfully.") 