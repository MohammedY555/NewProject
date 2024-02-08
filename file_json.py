def menu_json(self):
    return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'status': self.status,
        'status_time': self.status_time,
        'price': self.price
    }


def personal_json(self):
    return {
        'id': self.id,
        'job_title': self.job_title,
        'job_title_id': self.job_title_id,
        'salary': self.salary,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'age': self.age,
        'status': self.status,
        'created_at': self.created_at,
        'delete_at': self.delete_at,
        'is_deleted': self.is_deleted
    }


def table_status_json(self):
    return {
        'id': self.id,
        'status_name': self.status_name
    }


def tables_json(self):
    return {
        'id': self.id,
        'table_name': self.table_name,
        'personal_id': self.personal_id,
        'table_status_id': self.table_status_id,
        'is_deleted': self.is_deleted
    }


def orders_json(self):
    return {
        'id': self.id,
        'order_id': self.order_id,
        'menu_id': self.menu_id,
        'description_id': self.description_id,
        'order_status': self.order_status,
        'dish_status': self.dish_status,
        'table_id': self.table_id,
        'personal_id': self.personal_id,
        'created_at': self.created_at,
        'completion_date': self.completion_date,
        'is_deleted': self.is_deleted
    }


def invoices_json(self):
    return {
        'id': self.id,
        'order_id': self.order_id,
        'menu_id': self.menu_id,
        'description_id': self.description_id,
        'table_id': self.table_id,
        'personal_id': self.personal_id,
        'status': self.status,
        'created_at': self.created_at,
        'canceled_at': self.canceled_at
    }
