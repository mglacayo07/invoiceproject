from flask_restx import Namespace, Resource, fields
from invoice_project.models import Invoice, InvoiceItem
from invoice_project.db import db
from datetime import datetime
from flask import abort

items_namespace = Namespace('invoice/item', description='InvoiceItem methods')

item_model = items_namespace.model("InvoiceItem",{
    'id': fields.Integer,
    'units': fields.Integer,
    'description': fields.String,
    'amount': fields.Float,
    'invoice_id': fields.Integer,
})

item_parser = items_namespace.parser()
item_parser.add_argument("units", type=int, required=True, help="1")
item_parser.add_argument("description", type=str, required=True, help="Product description")
item_parser.add_argument("amount", type=float, required=True, help="10.00")
item_parser.add_argument("invoice_id", type=int, required=True, help="Id of the invoice you want to link")

@items_namespace.route('')
class InvoiceItemClass(Resource):

    @items_namespace.doc('post_items')
    @items_namespace.expect(item_parser)
    @items_namespace.marshal_with(item_model,as_list=False)
    @items_namespace.response(200, 'Success')
    @items_namespace.response(400, 'Invalid data')
    def post(self):
        '''
            Create new item
        '''

        kw = item_parser.parse_args()

        if kw['units'] < 1:
            abort(400, 'The minimum value form units is 1')

        invoice_handler = db.session.query(Invoice).filter_by(id=kw['invoice_id']).first()
        if invoice_handler == None:
            abort(400, 'No invoice was found with this id {'+str(kw['invoice_id'])+'}')

        item_handler = db.session.query(InvoiceItem).filter_by(units=kw['units'],description=kw['description'],amount=kw['amount'],invoice_id=kw['invoice_id']).first()
        if item_handler != None:
            abort(400, 'This information already exist')

        item_handler = InvoiceItem.add(kw['units'],kw['description'],kw['amount'],kw['invoice_id'])

        return {'id':item_handler.id,'units':item_handler.units,'description':item_handler.description,'amount':item_handler.amount,'invoice_id':item_handler.invoice_id}

@items_namespace.route('/<int:id>')
class SpecificInvoiceItemClass(Resource):

    @items_namespace.doc('get_item')
    @items_namespace.marshal_with(item_model, as_list=False)
    @items_namespace.response(200, 'Success')
    @items_namespace.response(400, 'Invalid data')
    def get(self,id):
        '''
            Return item information
        '''

        item_handler = db.session.query(InvoiceItem).filter_by(id=id).first()
        if item_handler == None:
            abort(400, 'No item was found with this id {'+str(id)+'}')

        return {'id': item_handler.id, 'units': item_handler.units, 'description': item_handler.description, 'amount': item_handler.amount, 'invoice_id': item_handler.invoice_id}