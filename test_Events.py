from flask import Flask, request
from AWSManager import Events
 
event = Events()
app = Flask(__name__)

# works

@app.route("/create-event", methods=["POST"])
def create():
    #event.put(Event_name = "trPresentation", Event_date = "October 3rd", Event_time = "2pm", User = "Class", Event_desc = "Presenting things", Event_image = "None", Event_location = "Zoom")
    res = request.json
    Event_name = res['Event_name']
    Event_date = res['Event_date']
    Event_time = res['Event_time']
    User = res['User']
    Event_desc = res['Event_desc']
    Event_image = res['Event_image']
    Event_location = res['Event_location']
    Online = res['Online']

    created = event.check_if_event_exists(Event_name = Event_name, Event_date = Event_date, Event_time = Event_time, User = User, Event_desc= Event_desc, Event_image = Event_image, Event_location = Event_location, Online = Online)
    return created


# works 
@app.route("/event-delete", methods=["POST"])
def delete():
    res = request.json
    Event_name = res['Event_name']
    
    deleted = event.delete(Event_name = Event_name)
    return deleted




@app.route("/event-update", methods=["POST"]) 
def update():
    res = request.json
    Event_name = res["Event_name"]
    New_Event_date = res['New_Event_date']
    New_Event_time = res['New_Event_time']
    New_User = res['New_User']
    New_Event_desc = res['New_Event_desc']
    New_Event_image = res['New_Event_image']
    New_Event_location = res['New_Event_location']
    New_Online = res['New_Online']

    updated = event.update_event(Event_name = Event_name, New_Event_date = New_Event_date , New_Event_time = New_Event_time, New_User = New_User,  New_Event_desc = New_Event_desc,  New_Event_image = New_Event_image, New_Event_location = New_Event_location, New_Online = New_Online)
    return updated




@app.route("/event-view", methods= ["GET"])
def view_event():
    res = event.view()
    return res

#still a work in progress
@app.route("/event-rsvp", methods= ["GET"])
def rsvp():
    res = event.rsvp()
    return res
# @app.route("/event/rsvp", methods=["POST"])
# def rsvp():
#      t1.put("Event_name", "Event_date", "Event_time", "User", "Event_desc", "Event_image", "Event_location")

if __name__ == '__main__':
    app.run(debug=True)

# @pytest.fixture(scope = "module")
def test_createEvent():
        with app.test_client() as c:
            response = c.get('/create-event')
            #print((response.status_code))
            assert response.status_code == 200

def test_eventViewing():
        with app.test_client() as c:
            response = c.get('/event-view')
            assert response.status_code == 200

def test_eventUpdate():
        with app.test_client() as c:
            response = c.get('/event-update')
            assert response.status_code == 200

def test_eventDelete():
        with app.test_client() as c:
            response = c.get('/event-delete')
            assert response.status_code == 200

def test_eventRSVP():
        with app.test_client() as c:
            response = c.get('/event-rsvp')
            assert response.status_code == 200