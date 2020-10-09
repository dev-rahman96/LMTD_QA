from flask import Flask, request
from AWSManager import Events
import pytest
 
 
app = Flask(__name__)
t1 = Events()

@app.route("/event")
def create():
    t1.put(Event_name = "Presentation", Event_date = "October 3rd", Event_time = "2pm", User = "Class", Event_desc = "Presenting things", Event_image = "None", Event_location = "Zoom")
    
# @app.route("/event/viewing", methods= ["GET"])
# def view_event():
#     return 

# @app.route("/event/update")
# def update_event():
#     t1.put("Event_name", "Event_desc", "Date_time", "Price", "Address", "Virtual")


# @app.route("/event/delete", methods=["POST"])
# def delete_eventç():
#      t1.put("Event_name", "Event_date", "Event_time", "User", "Event_desc", "Event_image", "Event_location")

# @app.route("/event/rsvp", methods=["POST"])
# def rsvp():
#      t1.put("Event_name", "Event_date", "Event_time", "User", "Event_desc", "Event_image", "Event_location")

if __name__ == '__main__':
    app.run(debug=True)

# @pytest.fixture(scope = "module")
def test_createEvent():
        with app.test_client() as c:
            response = c.get('/event')
            #print((response.status_code))
            assert response.status_code == 200

# def test_eventViewing():
#         with app.test_client() as c:
#             response = c.get('/event/viewing')
#             assert(response.status_code, 200)

# def test_eventUpdate():
#         with app.test_client() as c:
#             response = c.get('/event/update')
#             assert(response.status_code, 200)

# def test_eventDelete():
#         with app.test_client() as c:
#             response = c.get('/event/delete')
#             assert(response.status_code, 200)

def test_eventRSVP():
        with app.test_client() as c:
            response = c.get('/event/rsvp')
            assert(response.status_code, 200)

