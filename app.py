from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from db import db
from resources.campaign_resource import Campaign

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:boborock1986@127.0.0.1:3306/tonydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Campaign, '/campaign/<int:campaign_id>')
# api.add_resource(Campaign, '/campaign')
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
