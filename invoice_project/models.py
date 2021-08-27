from invoice_project.db import db

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text, Date, Numeric

class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    date = Column(Date,nullable=False)

    @classmethod
    def add(cls,date):
        handler = cls()
        handler.date = date
        db.session.add(handler)
        db.session.commit()
        return handler

class InvoiceItem(db.Model):
    __tablename__ = 'invoice_item'
    id = Column(Integer, primary_key=True)
    units = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    amount = Column(Numeric)
    invoice_id = Column(Integer, ForeignKey("invoice.id"))

    @classmethod
    def add(cls,units,description,amount,invoice_id):
        handler = cls()
        handler.units = units
        handler.description = description
        handler.amount = amount
        handler.invoice_id = invoice_id
        db.session.add(handler)
        db.session.commit()
        return handler
