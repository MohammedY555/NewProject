from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean, CheckConstraint, func
from sqlalchemy.orm import DeclarativeBase
from connection import engine


class Base(DeclarativeBase):
    pass


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(String(500))
    title_id = Column(Integer, unique=True)
    description = Column(String(500), unique=True)
    description_id = Column(Integer, unique=True)
    status = Column(String(100))
    status_time = Column(Integer, default=0)
    price = Column(Float)

    # def __repr__(self):
    #     return (f"<Menu(id={self.id}, title={self.title}, title_id={self.title_id}, description={self.description}"
    #             f"description_id={self.description_id}, status={self.status},status_time={self.status_time}, "
    #             f"price={self.price})>")


class Personal(Base):
    __tablename__ = 'personal'
    id = Column(Integer, primary_key=True)
    job_title = Column(String(255))
    job_title_id = Column(Integer, unique=True)
    salary = Column(Float)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)
    status = Column(String(100), CheckConstraint('status IN ("Уволен", "Работает")'))
    created_at = Column(DateTime, server_default=func.current_timestamp())
    delete_at = Column(DateTime)
    is_deleted = Column(Boolean, default=False)

    # def __repr__(self): return ( f"<personal(id={self.id}, job_title={self.job_title}, job_title_id={
    # self.job_title_id}, salary={self.salary}" f"first_name={self.first_name}, last_name={self.last_name},
    # age={self.age},status={self.status} " f"created_at={self.created_at}), delete_at={self.delete_at}, is_deleted={
    # self.is_deleted}>")


class TableStatus(Base):
    __tablename__ = 'table_status'
    id = Column(Integer, primary_key=True)
    status_name = Column(String(100), unique=True)
    # CheckConstraint('status_name IN ("Свободен", "Занят", "Зарезервирован")'))


class Tables(Base):
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True)
    table_name = Column(String(255), unique=True)
    personal_id = Column(Integer, ForeignKey('personal.id'))
    table_status_id = Column(Integer, ForeignKey('table_status.id'))
    is_deleted = Column(Boolean, default=False)


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, unique=True)
    menu_id = Column(Integer, ForeignKey('menu.id'))
    description_id = Column(Integer, ForeignKey('menu.description_id'))
    order_status = Column(String(50),
                          CheckConstraint('order_status IN ("в обработке", "выполнен", "отменен", "в ожидании")'))
    dish_status = Column(String(50),
                         CheckConstraint('dish_status IN ("готовится", "готово", "в ожидании", "отменено")'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    personal_id = Column(Integer, ForeignKey('personal.id'))
    created_at = Column(DateTime),
    completion_date = Column(DateTime),
    is_deleted = Column(Boolean)


class Invoices(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    menu_id = Column(Integer, ForeignKey('menu.id'))
    description_id = Column(Integer, ForeignKey('menu.description_id'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    personal_id = Column(Integer, ForeignKey('personal.id'))
    status = Column(String(50), CheckConstraint('status IN ("оплачен", "отменен")'))
    created_at = Column(DateTime, server_default=func.current_timestamp())
    canceled_at = Column(DateTime)


Base.metadata.create_all(bind=engine)
