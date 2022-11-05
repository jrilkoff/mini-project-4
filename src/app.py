# import Flask and jsonify
from flask import Flask, jsonify, request

# import Resource, Api, reqparser
from flask_restful import Resource, Api
import pandas as pd
import pickle

app = Flask(__name__)
api = Api(app)

model = pickle.load(open('model.p', 'rb'))

class LoanApprove(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        res = model.predict(df)

        return res.tolist()

api.add_resource(LoanApprove, '/loans')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4242)