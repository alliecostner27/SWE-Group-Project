from . import orders, order_details, promo, review, customer, menu, payment_method


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(promo.router)
    app.include_router(review.router)
    app.include_router(customer.router)
    app.include_router(menu.router)
    app.include_router(payment_method.router)
