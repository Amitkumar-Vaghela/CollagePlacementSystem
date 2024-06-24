
from flask import render_template
from placement_management import app, db
from placement_management.models import User, Placement

@app.route('/')
def home():
    placements = Placement.query.all()
    return render_template('index.html', placements=placements)
