from connection import get_session as session
from models import *

import logging


# ======================================================================================================================

def get_menu(session):
    return session.query(Menu).all()


def add_menu(db, title, description, status, status_time, price):
    try:
        menu = Menu(title=title, description=description, status=status, status_time=status_time, price=price)
        db.add(menu)
        db.commit()
    except Exception as e:
        logging.error(f"ERROR is: {e}")
        db.rollback()
        return str(e)


def delete_menu(db, menu_id):
    try:
        menu = db.query(Menu).filter_by(id=menu_id).first()
        if menu:
            db.delete(menu)
            db.commit()
            return menu
        else:
            raise ValueError("Menu data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


def update_menu(db, menu_id, new_title):
    try:
        menu = db.query(Menu).filter_by(id=menu_id).first()
        if menu:
            menu.title = new_title
            db.commit()
        else:
            raise ValueError("Menu data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


# ======================================================================================================================

def get_personals(session):
    return session.query(Personal).all()


def add_personal(db, job_title, job_title_id, salary, first_name, last_name, age, status):
    try:
        personal = Personal(job_title=job_title, job_title_id=job_title_id, salary=salary, first_name=first_name,
                            last_name=last_name, age=age, status=status)
        db.add(personal)
        db.commit()
    except Exception as e:
        logging.error(f"ERROR is: {e}")
        db.rollback()
        return str(e)


def delete_personal(db, personal_id):
    try:
        personal = db.query(Personal).filter_by(id=personal_id).first()
        if personal:
            db.delete(personal)
            db.commit()
            return personal
        else:
            raise ValueError("Personal data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


def update_personal(db, personal_id, new_job_title):
    try:
        personal = db.query(Personal).filter_by(id=personal_id).first()
        if personal:
            personal.job_title = new_job_title
            db.commit()
        else:
            raise ValueError("Personal data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


# ======================================================================================================================

def get_table_statuses(session):
    return session.query(TableStatus).all()


def add_table_status(db, status_name):
    try:
        table_status = TableStatus(status_name=status_name)
        db.add(table_status)
        db.commit()
    except Exception as e:
        logging.error(f"ERROR is: {e}")
        db.rollback()
        return str(e)


def delete_table_status(db, table_status_id):
    try:
        table_status = db.query(TableStatus).filter_by(id=table_status_id).first()
        if table_status:
            db.delete(table_status)
            db.commit()
            return table_status
        else:
            raise ValueError("Table status data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


def update_table_status(db, table_status_id, new_status_name):
    try:
        table_status = db.query(TableStatus).filter_by(id=table_status_id).first()
        if table_status:
            table_status.status_name = new_status_name
            db.commit()
        else:
            raise ValueError("Table status data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


# ======================================================================================================================


def get_tables(session):
    return session.query(Tables).all()


def add_table(db, table_name, personal_id, table_status_id, is_deleted=False):
    try:
        table = Tables(table_name=table_name, personal_id=personal_id, table_status_id=table_status_id,
                       is_deleted=is_deleted)
        db.add(table)
        db.commit()
    except Exception as e:
        logging.error(f"ERROR is: {e}")
        db.rollback()
        return str(e)


def delete_table(db, table_id):
    try:
        table = db.query(Tables).filter_by(id=table_id).first()
        if table:
            db.delete(table)
            db.commit()
            return table
        else:
            raise ValueError("Table data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


def update_table(db, table_id, new_table_name):
    try:
        table = db.query(Tables).filter_by(id=table_id).first()
        if table:
            table.table_name = new_table_name
            db.commit()
        else:
            raise ValueError("Table data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


# ======================================================================================================================


def get_orders(session):
    return session.query(Orders).all()


def add_order(db, order_id, menu_id, description_id, order_status, dish_status, table_id, personal_id,
              created_at=None, completion_date=None, is_deleted=False):
    try:
        order = Orders(order_id=order_id, menu_id=menu_id, description_id=description_id, order_status=order_status,
                       dish_status=dish_status, table_id=table_id, personal_id=personal_id, created_at=created_at,
                       completion_date=completion_date, is_deleted=is_deleted)
        db.add(order)
        db.commit()
    except Exception as e:
        logging.error(f"ERROR is: {e}")
        db.rollback()
        return str(e)


def delete_order(db, order_id):
    try:
        order = db.query(Orders).filter_by(id=order_id).first()
        if order:
            db.delete(order)
            db.commit()
            return order
        else:
            raise ValueError("Order data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


def update_order(db, order_id, new_order_status):
    try:
        order = db.query(Orders).filter_by(id=order_id).first()
        if order:
            order.order_status = new_order_status
            db.commit()
        else:
            raise ValueError("Order data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()


# ======================================================================================================================

def get_invoices(session):
    return session.query(Invoices).all()


def add_invoice(db, order_id, menu_id, description_id, table_id, personal_id, status, created_at=None,
                canceled_at=None):
    try:
        invoice = Invoices(order_id=order_id, menu_id=menu_id, description_id=description_id, table_id=table_id,
                           personal_id=personal_id, status=status, created_at=created_at, canceled_at=canceled_at)
        db.add(invoice)
        db.commit()
    except Exception as e:
        logging.error(f"ERROR is: {e}")
        db.rollback()
        return str(e)


def cancel_invoice(db, invoice_id):
    try:
        invoice = db.query(Invoices).filter_by(id=invoice_id).first()
        if invoice:
            invoice.status = "отменен"
            invoice.canceled_at = func.current_timestamp()
            db.commit()
            return invoice
        else:
            raise ValueError("Invoice data not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()

# ======================================================================================================================
