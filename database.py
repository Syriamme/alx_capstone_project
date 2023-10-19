from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Expense

engine = create_engine('mysql+mysqlconnector://Daniel:new_password@localhost/expense_db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()