from datetime import datetime

from flask import Flask, render_template, request
import socket

app = Flask(__name__)


@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


@app.route("/api/v1/objects/logs", methods=['GET'])
def get_all_actions():
    with open('message.txt', 'r') as f:
        return f.read()


@app.route("/health")
def health():
    return "OK"

# @app.route("/api/v2/objects/cars/<car_id>")
# def search_cars():
#     print(request.args.get('car_id'))
#     # if request.method == 'GET':
#     #     return get_car(car_id=request.args.get('car_id'))

@app.route("/api/v1/objects/cars/<cars>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def cars(cars):
    # get the user posted data
    json_data = request.get_json()
    if request.method == 'GET':
        return get_car(car_id=cars)
    if request.method == 'POST':
        return create_car(json_data)
    elif request.method == 'PUT':
        return update_car()
    elif request.method == 'DELETE':
        return delete_car()





# following functions write the message and append to a file
def write_message(message):
    with open('message.txt', 'a') as f:
        # write the message with time stamp
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + message + '\n')


def get_car(car_id):
    write_message("GET /api/v1/objects/cars" + str(car_id))
    return "{'first': 'Foo', 'last': 'Bar'}"


def create_car(json_data):
    write_message("POST /api/v1/objects/cars" + str(json_data))

    return json_data


def update_car():
    write_message("PUT /api/v1/objects/cars")
    return "{'message': 'Car updated'}"


def delete_car():
    write_message("DELETE /api/v1/objects/cars")
    return "{'message': 'Car deleted'}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
