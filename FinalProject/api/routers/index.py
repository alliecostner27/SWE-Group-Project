from . import orders, order_details, promo, review


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(promo.router)
    app.include_router(review.router)
