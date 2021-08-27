from flask_restx import Namespace, Resource, fields, inputs
from invoice_project.models import Invoice
from invoice_project.db import db
from flask import abort
from datetime import datetime

invoices_namespace = Namespace('invoice', description='Invoice methods')

invoice_model = invoices_namespace.model("Invoice", {
    'id': fields.Integer,
    'date': fields.Date
})

invoice_parser = invoices_namespace.parser()
invoice_parser.add_argument("date", type=inputs.date, required=True, help="YYYY-MM-DD")


@invoices_namespace.route('')
class InvoiceClass(Resource):

    @invoices_namespace.doc('post_invoices')
    @invoices_namespace.expect(invoice_parser)
    @invoices_namespace.marshal_with(invoice_model,as_list=False)
    @invoices_namespace.response(200, 'Success')
    def post(self):
        '''
            Create new invoice
        '''

        kw = invoice_parser.parse_args()
        invoice_handler = Invoice.add(kw['date'])

        return {'id':invoice_handler.id,'date':invoice_handler.date}

@invoices_namespace.route('/<int:id>')
class SpecificInvoiceClass(Resource):

    @invoices_namespace.doc('get_invoice')
    @invoices_namespace.marshal_with(invoice_model, as_list=False)
    @invoices_namespace.response(200, 'Success')
    @invoices_namespace.response(400, 'Invalid data')
    def get(self,id):
        '''
            Get invoice by id
        '''

        invoice_handler = db.session.query(Invoice).filter_by(id=id).first()
        if invoice_handler == None:
            abort(400, 'No invoice was found with this id {'+str(id)+'}')

        return {'id': invoice_handler.id, 'date': invoice_handler.date}