from . import orders, order_details, customer, promo, payment_method, review, menu

from ..dependencies.database import engine


def index():
    customer.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    promo.Base.metadata.create_all(engine)
    payment_method.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)
