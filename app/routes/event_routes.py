from flask import Blueprint, request, jsonify, render_template, redirect
from flask_login import login_required, current_user
from app.models.event import Event
from app.serializers.event_schema import EventSchema

event_bp = Blueprint("event", __name__)

event_schema = EventSchema()

def serialize_event(event):
    return event_schema.dump(event)

@event_bp.route("/events", methods=["POST"])
@login_required
def create_event():
    name = request.form.get("name")
    description = request.form.get("description")
    date = request.form.get("date")
    location = request.form.get("location")
    seats = request.form.get("seats")

    request.form.clear()
    
    if not all([name, date, location]):
        return render_template("new_event.html", error="Missing required fields")
    
    Event.create_event(name, description, date, location, current_user.id, seats)
    events = Event.get_all_event_by_user_id(current_user.id)
    return render_template("events.html", events= events, message="Event created successfully")


@event_bp.route("/events/<int:event_id>", methods=["GET"])
@login_required
def get_event(event_id):
    event = Event.get_event_by_id(event_id)
    stringa = Event.update_seats_by_event_id(event_id)
    print(stringa)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    return redirect(f"/booking/{event_id}")

@event_bp.route("/events", methods=["GET"])
@login_required
def get_user_events():
    events = Event.get_all_events()
    return render_template("events.html", events=events)

@event_bp.route("/events/new", methods=["GET"])
@login_required
def new_event_page():
    return render_template("new_event.html")