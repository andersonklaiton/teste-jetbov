from flask import Flask

def init_app(app:Flask):
    from app.routes.routes import routes
    routes(app)