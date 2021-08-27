from invoice_project.app import create_app

if __name__ == '__main__':
    application = create_app()
    application.app_context().push()
    # Initialise the DB
    print("QUE ONDA")
    application.db.create_all()