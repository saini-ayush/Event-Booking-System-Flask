from flask import Blueprint, redirect
from flask_login import login_required, current_user
from app.models.booking import Booking

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/booking/<int:event_id>",methods=["GET"])
@login_required
def createBooking(event_id):
    Booking.create_booking(event_id, current_user.id)
    return redirect("/events")