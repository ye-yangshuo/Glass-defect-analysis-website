from app import create_app
from flask_cors import CORS
app = create_app()

if __name__ == '__main__':
    CORS(app,resources=r'/*')
    app.run(host= '192.168.123.84',port=8081)
    