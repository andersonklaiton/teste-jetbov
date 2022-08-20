from http import HTTPStatus
from flask import jsonify
from app.models.areas import Areas
from app import db

def register_a_area(data):
    model_area = Areas(data.get("area"), data.get("gmd"), data.get("total_de_animais"))
    area = model_area.__dict__
    have_area = list(db.areas.find({"area":area["area"]}))
    if len(have_area) == 0:
        db.areas.insert_one(area)
        del area["_id"]
        return jsonify(area), HTTPStatus.CREATED
    
    else:
        return {"message":"Área já cadastrada"}, HTTPStatus.CONFLICT

def show_all_areas():
    response = list(db.areas.find())
    for area in response:
        del area["_id"]
    return jsonify(response), HTTPStatus.OK

def del_area(area):
    db.areas.delete_one({"area":area})
    return jsonify(), HTTPStatus.NO_CONTENT