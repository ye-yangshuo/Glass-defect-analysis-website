from flask import Flask

from app.routes import image_routes
from app.routes import gallery_routes
from app.routes import labels_routes
from app.routes import analyze_routes
from app.routes import authentic_routes
from app.routes import auth_routes
def create_app():
    app = Flask(__name__)

    
    
    #注册蓝图
    app.register_blueprint(image_routes.bp)
    app.register_blueprint(labels_routes.bp)
    app.register_blueprint(authentic_routes.bp)

    app.register_blueprint(gallery_routes.bp)
    app.register_blueprint(analyze_routes.bp)
    app.register_blueprint(auth_routes.bp)

    return app