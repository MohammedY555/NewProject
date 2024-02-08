from flask import jsonify, Blueprint, request
from connection import get_session
from repository import *

app = Blueprint('routes', __name__)


@app.route('/')
def index():
    return "Raising the server"


# ======================================================================================================================

@app.route('/menu', methods=['GET'])
def get_menu_route():
    Session = get_session()
    try:
        menu_items = get_menu(Session)
        menu_data = [{
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'status': item.status,
            'price': item.price
        } for item in menu_items]
        return jsonify(menu_data)
    except Exception as e:
        app.logger.error(f"An error occurred while retrieving menu items: {e}")
        return jsonify({'error': 'An error occurred while retrieving menu items.'}), 500
    finally:
        Session.close()


@app.route('/menu', methods=['POST'])
def add_menu_route():
    Session = get_session()
    data = request.json
    title = data.get('title')
    description = data.get('description')
    status = data.get('status')
    status_time = data.get('status_time')
    price = data.get('price')

    if not all([title, description, status, status_time, price]):
        return jsonify({'error': 'Missing required fields for menu item.'}), 400

    try:
        add_menu(Session, title, description, status, status_time, price)
        return jsonify({'message': 'Menu item added successfully.'}), 201
    except Exception as e:
        app.logger.error(f"An error occurred while adding menu item: {e}")
        return jsonify({'error': 'An error occurred while adding menu item.'}), 500
    finally:
        Session.close()


@app.route('/menu/<int:menu_id>', methods=['DELETE'])
def delete_menu_route(menu_id):
    Session = get_session()
    try:
        deleted_menu = delete_menu(Session, menu_id)
        if deleted_menu:
            return jsonify({'message': 'Menu item deleted successfully.'}), 200
        else:
            return jsonify({'error': 'Menu item not found.'}), 404
    except Exception as e:
        app.logger.error(f"An error occurred while deleting menu item: {e}")
        return jsonify({'error': 'An error occurred while deleting menu item.'}), 500
    finally:
        Session.close()


@app.route('/menu/<int:menu_id>', methods=['PUT'])
def update_menu_route(menu_id):
    Session = get_session()
    data = request.json
    new_title = data.get('title')

    if not new_title:
        return jsonify({'error': 'New title is required for updating menu item.'}), 400

    try:
        update_menu(Session, menu_id, new_title)
        return jsonify({'message': 'Menu item updated successfully.'}), 200
    except Exception as e:
        app.logger.error(f"An error occurred while updating menu item: {e}")
        return jsonify({'error': 'An error occurred while updating menu item.'}), 500
    finally:
        Session.close()


# ======================================================================================================================
@app.route('/personals', methods=['GET'])
def get_personals_route():
    Session = get_session()
    try:
        personals = get_personals(Session)
        personals_data = [{
            'id': personal.id,
            'job_title': personal.job_title,
            'salary': personal.salary,
            'first_name': personal.first_name,
            'last_name': personal.last_name,
            'age': personal.age,
            'status': personal.status
        } for personal in personals]
        return jsonify(personals_data)
    except Exception as e:
        app.logger.error(f"An error occurred while retrieving personals: {e}")
        return jsonify({'error': 'An error occurred while retrieving personals.'}), 500
    finally:
        Session.close()


@app.route('/personals', methods=['POST'])
def add_personal_route():
    Session = get_session()
    data = request.json
    job_title = data.get('job_title')
    salary = data.get('salary')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    age = data.get('age')
    status = data.get('status')

    if not all([job_title, salary, first_name, last_name, age, status]):
        return jsonify({'error': 'Missing required fields for personal data.'}), 400

    try:
        add_personal(Session, job_title, salary, first_name, last_name, age, status)
        return jsonify({'message': 'Personal data added successfully.'}), 201
    except Exception as e:
        app.logger.error(f"An error occurred while adding personal data: {e}")
        return jsonify({'error': 'An error occurred while adding personal data.'}), 500
    finally:
        Session.close()


@app.route('/personals/<int:personal_id>', methods=['DELETE'])
def delete_personal_route(personal_id):
    Session = get_session()
    try:
        deleted_personal = delete_personal(Session, personal_id)
        if deleted_personal:
            return jsonify({'message': 'Personal data deleted successfully.'}), 200
        else:
            return jsonify({'error': 'Personal data not found.'}), 404
    except Exception as e:
        app.logger.error(f"An error occurred while deleting personal data: {e}")
        return jsonify({'error': 'An error occurred while deleting personal data.'}), 500
    finally:
        Session.close()


@app.route('/personals/<int:personal_id>', methods=['PUT'])
def update_personal_route(personal_id):
    Session = get_session()
    data = request.json
    new_job_title = data.get('job_title')

    if not new_job_title:
        return jsonify({'error': 'New job title is required for updating personal data.'}), 400

    try:
        update_personal(Session, personal_id, new_job_title)
        return jsonify({'message': 'Personal data updated successfully.'}), 200
    except Exception as e:
        app.logger.error(f"An error occurred while updating personal data: {e}")
        return jsonify({'error': 'An error occurred while updating personal data.'}), 500
    finally:
        Session.close()


# ======================================================================================================================

@app.route('/table_statuses', methods=['GET'])
def get_table_statuses_route():
    Session = get_session()
    try:
        table_statuses = get_table_statuses(Session)
        table_statuses_data = [{
            'id': table_status.id,
            'status_name': table_status.status_name
        } for table_status in table_statuses]
        return jsonify(table_statuses_data)
    except Exception as e:
        app.logger.error(f"An error occurred while retrieving table statuses: {e}")
        return jsonify({'error': 'An error occurred while retrieving table statuses.'}), 500
    finally:
        Session.close()


@app.route('/table_statuses', methods=['POST'])
def add_table_status_route():
    Session = get_session()
    data = request.json
    status_name = data.get('status_name')

    if not status_name:
        return jsonify({'error': 'Missing required field for table status.'}), 400

    try:
        add_table_status(Session, status_name)
        return jsonify({'message': 'Table status added successfully.'}), 201
    except Exception as e:
        app.logger.error(f"An error occurred while adding table status: {e}")
        return jsonify({'error': 'An error occurred while adding table status.'}), 500
    finally:
        Session.close()


@app.route('/table_statuses/<int:table_status_id>', methods=['DELETE'])
def delete_table_status_route(table_status_id):
    Session = get_session()
    try:
        deleted_table_status = delete_table_status(Session, table_status_id)
        if deleted_table_status:
            return jsonify({'message': 'Table status deleted successfully.'}), 200
        else:
            return jsonify({'error': 'Table status not found.'}), 404
    except Exception as e:
        app.logger.error(f"An error occurred while deleting table status: {e}")
        return jsonify({'error': 'An error occurred while deleting table status.'}), 500
    finally:
        Session.close()


@app.route('/table_statuses/<int:table_status_id>', methods=['PUT'])
def update_table_status_route(table_status_id):
    Session = get_session()
    data = request.json
    new_status_name = data.get('status_name')

    if not new_status_name:
        return jsonify({'error': 'New status name is required for updating table status.'}), 400

    try:
        update_table_status(Session, table_status_id, new_status_name)
        return jsonify({'message': 'Table status updated successfully.'}), 200
    except Exception as e:
        app.logger.error(f"An error occurred while updating table status: {e}")
        return jsonify({'error': 'An error occurred while updating table status.'}), 500
    finally:
        Session.close()


# ======================================================================================================================

@app.route('/tables', methods=['GET'])
def get_tables_route():
    Session = get_session()
    try:
        tables = get_tables(Session)
        tables_data = [{
            'id': table.id,
            'table_name': table.table_name,
            'personal_id': table.personal_id,
            'table_status_id': table.table_status_id,
            'is_deleted': table.is_deleted
        } for table in tables]
        return jsonify(tables_data)
    except Exception as e:
        app.logger.error(f"An error occurred while retrieving tables: {e}")
        return jsonify({'error': 'An error occurred while retrieving tables.'}), 500
    finally:
        Session.close()


@app.route('/tables', methods=['POST'])
def add_table_route():
    Session = get_session()
    data = request.json
    table_name = data.get('table_name')
    personal_id = data.get('personal_id')
    table_status_id = data.get('table_status_id')
    is_deleted = data.get('is_deleted', False)

    if not all([table_name, personal_id, table_status_id]):
        return jsonify({'error': 'Missing required fields for table.'}), 400

    try:
        add_table(Session, table_name, personal_id, table_status_id, is_deleted)
        return jsonify({'message': 'Table added successfully.'}), 201
    except Exception as e:
        app.logger.error(f"An error occurred while adding table: {e}")
        return jsonify({'error': 'An error occurred while adding table.'}), 500
    finally:
        Session.close()


@app.route('/tables/<int:table_id>', methods=['DELETE'])
def delete_table_route(table_id):
    Session = get_session()
    try:
        deleted_table = delete_table(Session, table_id)
        if deleted_table:
            return jsonify({'message': 'Table deleted successfully.'}), 200
        else:
            return jsonify({'error': 'Table not found.'}), 404
    except Exception as e:
        app.logger.error(f"An error occurred while deleting table: {e}")
        return jsonify({'error': 'An error occurred while deleting table.'}), 500
    finally:
        Session.close()


@app.route('/tables/<int:table_id>', methods=['PUT'])
def update_table_route(table_id):
    Session = get_session()
    data = request.json
    new_table_name = data.get('table_name')

    if not new_table_name:
        return jsonify({'error': 'New table name is required for updating table.'}), 400

    try:
        update_table(Session, table_id, new_table_name)
        return jsonify({'message': 'Table updated successfully.'}), 200
    except Exception as e:
        app.logger.error(f"An error occurred while updating table: {e}")
        return jsonify({'error': 'An error occurred while updating table.'}), 500
    finally:
        Session.close()


# ======================================================================================================================

@app.route('/orders', methods=['GET'])
def get_orders_route():
    Session = get_session()
    try:
        orders = get_orders(Session)
        orders_data = [{
            'id': order.id,
            'order_id': order.order_id,
            'menu_id': order.menu_id,
            'description_id': order.description_id,
            'order_status': order.order_status,
            'dish_status': order.dish_status,
            'table_id': order.table_id,
            'personal_id': order.personal_id,
            'created_at': order.created_at,
            'completion_date': order.completion_date,
            'is_deleted': order.is_deleted
        } for order in orders]
        return jsonify(orders_data)
    except Exception as e:
        app.logger.error(f"An error occurred while retrieving orders: {e}")
        return jsonify({'error': 'An error occurred while retrieving orders.'}), 500
    finally:
        Session.close()


@app.route('/orders', methods=['POST'])
def add_order_route():
    Session = get_session()
    data = request.json
    order_id = data.get('order_id')
    menu_id = data.get('menu_id')
    description_id = data.get('description_id')
    order_status = data.get('order_status')
    dish_status = data.get('dish_status')
    table_id = data.get('table_id')
    personal_id = data.get('personal_id')
    created_at = data.get('created_at')
    completion_date = data.get('completion_date')
    is_deleted = data.get('is_deleted', False)

    if not all([order_id, menu_id, description_id, order_status, dish_status, table_id, personal_id]):
        return jsonify({'error': 'Missing required fields for order.'}), 400

    try:
        add_order(Session, order_id, menu_id, description_id, order_status, dish_status, table_id, personal_id,
                  created_at, completion_date, is_deleted)
        return jsonify({'message': 'Order added successfully.'}), 201
    except Exception as e:
        app.logger.error(f"An error occurred while adding order: {e}")
        return jsonify({'error': 'An error occurred while adding order.'}), 500
    finally:
        Session.close()


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order_route(order_id):
    Session = get_session()
    try:
        deleted_order = delete_order(Session, order_id)
        if deleted_order:
            return jsonify({'message': 'Order deleted successfully.'}), 200
        else:
            return jsonify({'error': 'Order not found.'}), 404
    except Exception as e:
        app.logger.error(f"An error occurred while deleting order: {e}")
        return jsonify({'error': 'An error occurred while deleting order.'}), 500
    finally:
        Session.close()


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_route(order_id):
    Session = get_session()
    data = request.json
    new_order_status = data.get('order_status')

    if not new_order_status:
        return jsonify({'error': 'New order status is required for updating order.'}), 400

    try:
        update_order(Session, order_id, new_order_status)
        return jsonify({'message': 'Order updated successfully.'}), 200
    except Exception as e:
        app.logger.error(f"An error occurred while updating order: {e}")
        return jsonify({'error': 'An error occurred while updating order.'}), 500
    finally:
        Session.close()


# ======================================================================================================================

@app.route('/invoices', methods=['GET'])
def get_invoices_route():
    Session = get_session()
    try:
        invoices = get_invoices(Session)
        invoices_data = [{
            'id': invoice.id,
            'order_id': invoice.order_id,
            'menu_id': invoice.menu_id,
            'description_id': invoice.description_id,
            'table_id': invoice.table_id,
            'personal_id': invoice.personal_id,
            'status': invoice.status,
            'created_at': invoice.created_at,
            'canceled_at': invoice.canceled_at
        } for invoice in invoices]
        return jsonify(invoices_data)
    except Exception as e:
        app.logger.error(f"An error occurred while retrieving invoices: {e}")
        return jsonify({'error': 'An error occurred while retrieving invoices.'}), 500
    finally:
        Session.close()


@app.route('/invoices', methods=['POST'])
def add_invoice_route():
    Session = get_session()
    data = request.json
    order_id = data.get('order_id')
    menu_id = data.get('menu_id')
    description_id = data.get('description_id')
    table_id = data.get('table_id')
    personal_id = data.get('personal_id')
    status = data.get('status')
    created_at = data.get('created_at')
    canceled_at = data.get('canceled_at')

    if not all([order_id, menu_id, description_id, table_id, personal_id, status]):
        return jsonify({'error': 'Missing required fields for invoice.'}), 400

    try:
        add_invoice(Session, order_id, menu_id, description_id, table_id, personal_id, status, created_at, canceled_at)
        return jsonify({'message': 'Invoice added successfully.'}), 201
    except Exception as e:
        app.logger.error(f"An error occurred while adding invoice: {e}")
        return jsonify({'error': 'An error occurred while adding invoice.'}), 500
    finally:
        Session.close()


@app.route('/invoices/<int:invoice_id>/cancel', methods=['PUT'])
def cancel_invoice_route(invoice_id):
    Session = get_session()
    try:
        canceled_invoice = cancel_invoice(Session, invoice_id)
        if canceled_invoice:
            return jsonify({'message': 'Invoice canceled successfully.'}), 200
        else:
            return jsonify({'error': 'Invoice not found.'}), 404
    except Exception as e:
        app.logger.error(f"An error occurred while canceling invoice: {e}")
        return jsonify({'error': 'An error occurred while canceling invoice.'}), 500
    finally:
        Session.close()

# ======================================================================================================================
