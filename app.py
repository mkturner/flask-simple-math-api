from flask import Flask, jsonify, request
from flask_restful import Api, Resource


# Instantiate Flask Instance
app = Flask(__name__)

# Instantiate API
api = Api(app)

# HELPER FUNCTIONS
def check_posted_data(posted_data, function_name):
    if (function_name in {'add', 'sub', 'mtpy'}):
        # check errors
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
            return 200
    elif (function_name == 'div'):
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        # Cannot divide by 0, must validate
        elif int(posted_data["y"]) == 0:
            return 302
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
    def post(self):
        # What happens if SUBTRACT was request using POST method
        # Step 1: Get posted data
        posted_data = request.get_json()

        # Step : Validate the data
        status_code = check_posted_data(posted_data, 'sub')
        # If not OK
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
        res = x - y

        # Step 4: Return result
        res_obj = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(res_obj)

class Multiply(Resource):
    def post(self):
        # What happens if Add was request using POST method
        # Step 1: Get posted data
        posted_data = request.get_json()

        # Step : Validate the data
        status_code = check_posted_data(posted_data, 'mtpy')
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
        res = x * y

        # Step 4: Return result
        res_obj = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(res_obj)

class Divide(Resource):
    def post(self):
        # What happens if Add was request using POST method
        # Step 1: Get posted data
        posted_data = request.get_json()

        # Step : Validate the data
        status_code = check_posted_data(posted_data, 'div')
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
        # Mulitply by 1.0 to ensure float
        res = (x * 1.0) / y

        # Step 4: Return result
        res_obj = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(res_obj)

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

# Use api to expose Subtract resource
api.add_resource(
    Subtract,
    "/subtract"
)

# Use api to expose Multiply resource
api.add_resource(
    Multiply,
    "/multiply"
)

# Use api to expose Divide resource
api.add_resource(
    Divide,
    "/divide"
)

if __name__=="__main__":
    app.run(debug=True)