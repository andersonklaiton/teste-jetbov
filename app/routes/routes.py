from http import HTTPStatus
from flask import Flask, request, jsonify
from app.controllers.areas_controllers.area import del_area, register_a_area, show_all_areas

from app.controllers.cattle_controllers.cattle import register_a_cattle, sell_a_cattle, show_a_cattle, show_all_cattles, update_a_cattle

def routes(app:Flask):
    @app.post("/cattle")
    def register_cattle():
        data = request.get_json()
        data_cattle = register_a_cattle(data)
        return data_cattle

    @app.get("/cattle/<brinco>")
    def show_cattle(brinco):
        cattle = show_a_cattle(brinco)
        return cattle

    @app.get("/cattles")
    def show_cattles():
        return show_all_cattles()
    
    @app.delete("/cattle/<brinco>")
    def sell_cattle(brinco):
        try:
            return sell_a_cattle(brinco)
        except TypeError:
            return {"message":"Brinco não encontrado"}, HTTPStatus.NOT_FOUND

    @app.patch("/cattle/<brinco>")
    def patch_cattle(brinco):
        try:
            return update_a_cattle(brinco)
        except TypeError:
            return {"message":"Brinco não encontrado"}, HTTPStatus.NOT_FOUND

    @app.post("/area")
    def register_area():
        data = request.get_json()
        data_area = register_a_area(data)
        return data_area

    @app.get("/areas")
    def show_areas():
        return show_all_areas()

    @app.delete("/area/<area>")
    def del_a_area(area):
        try:
            return del_area(area)
        except TypeError:
            return {"message":"Área não cadastrada"}, HTTPStatus.NOT_FOUND