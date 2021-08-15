from flask import Flask, jsonify, request
from flask_restful import Api, Resource


# Instantiate Flask Instance
app = Flask(__name__)

# Instantiate API
api = Api(app)

# HELPER FUNCTIONS
def check_posted_data(posted_data, function_name):
    if (function_name == 'add'):
        # check errors
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
            return 200

# RESOURCES
class Add(Resource):
    def post(self):
        # What happens if Add was request using POST method
        # Step 1: Get posted data
        posted_data = request.get_json()

        # Step : Validate the data
        status_code = check_posted_data(posted_data, 'add')
        if (status_code != 200):
            # give insightful error message
            res_json = {
                "Message": "An error occured",
                "Status Code": status_code
            }
            # Send message back
            return jsonify(res_json)

        
        # Step 2: Convert data to usable format (int)
        # status_code == '200' past this point
        x = int(posted_data["x"])
        y = int(posted_data["y"])

        # Step 3: Operate on data
        res = x + y

        # Step 4: Return result
        res_obj = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(res_obj)


class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass

# ROUTES

# Homepage
@app.route('/')
def hello_world():
    return "Hello World!"

# Use api to expose Add resource
api.add_resource(
    Add,
    "/add"
)

if __name__=="__main__":
    app.run(debug=True)