from sqlalchemy import Column, Integer, DateTime, Date, String, func, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    expense_date = Column(Date, nullable=False)
    expense_description = Column(String(255), nullable=False)
    expense_category = Column(String(50), nullable=False)
    expense_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, expense_date, expense_description, expense_category, expense_amount):
        self.expense_date = expense_date
        self.expense_description = expense_description
        self.expense_category = expense_category
        self.expense_amount = expense_amount
    
    @classmethod
    def get_transaction_by_id(cls, session, transaction_id):
        return session.query(cls).filter(cls.id == transaction_id).first()


class Income(Base):
    __tablename__ = 'income'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    income_date = Column(Date, nullable=False)
    income_description = Column(String(255), nullable=False)
    income_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, income_date, income_description, income_amount):
        self.income_date = income_date
        self.income_description = income_description
        self.income_amount = income_amount

    @classmethod
    def get_transaction_by_id(cls, session, transaction_id):
        return session.query(cls).filter(cls.id == transaction_id).first()