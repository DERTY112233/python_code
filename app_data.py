from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# Replace the database URL with your database connection details
DATABASE_URL = 'sqlite:///client_database.db'

# Define the SQLAlchemy database models
Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    status = Column(Boolean)

# Create a SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    return 'Hello, Database Integration with Flask!'

# Define a route to fetch active clients
@app.route('/active_clients', methods=['GET'])
def get_active_clients():
    active_clients = session.query(Client).filter(Client.status == True).all()
    result = [{'id': client.id, 'name': client.name} for client in active_clients]
    return jsonify(result)

# Define a route to fetch inactive clients
@app.route('/inactive_clients', methods=['GET'])
def get_inactive_clients():
    inactive_clients = session.query(Client).filter(Client.status == False).all()
    result = [{'id': client.id, 'name': client.name} for client in inactive_clients]
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
