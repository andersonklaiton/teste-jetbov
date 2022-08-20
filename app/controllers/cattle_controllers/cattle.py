from datetime import datetime, timedelta
from http import HTTPStatus
from app.models.cattle import Cattle
from app import db
from flask import jsonify, request

def register_a_cattle(data):
    model_cattle = Cattle(data.get("brinco"), data.get("peso_inicial"), data.get("area_inicial"), data.get("dias_na_area"))
    cattle = model_cattle.__dict__
    have_cattle = list(db.cattles.find({"brinco":cattle["brinco"]}))
    area2 = db.areas.find_one({"area":cattle["area_inicial"]})
    
    if area2==None:
        return jsonify({"message":"Área ainda não cadastrada"}), HTTPStatus.CONFLICT
    total_de_animais = area2["total_de_animais"]
    animais_na_area = area2["animais_na_area"]
    if animais_na_area < total_de_animais:
        if len(have_cattle) == 0:
            db.areas.update_one(area2, {"$set": {"animais_na_area":animais_na_area+1}})
            db.cattles.insert_one(cattle)
            del cattle["_id"]
            return jsonify(cattle), HTTPStatus.CREATED
        else:
            return {"message":"Brinco já cadastrado"}, HTTPStatus.CONFLICT
    else:
        return {"message":f"Já possui {total_de_animais} animais na área selecionada"}, HTTPStatus.UNAUTHORIZED

def show_a_cattle(brinco):
    response = list(db.cattles.find({"brinco":brinco}))
    if len(response) !=0:
        for cattle in response:
            del cattle["_id"]
        cattle_area = list(db.areas.find({"area":response[0]["area_inicial"]}))
        peso_final = (cattle_area[0]["gmd"]*response[0]["dias_na_area"])+response[0]["peso_inicial"]
        response[0]["peso_final"]=peso_final
        return jsonify(response), HTTPStatus.OK
    else:
        return jsonify({"message":"Brinco não encontrado"}), HTTPStatus.NOT_FOUND

def show_all_cattles():
    response = list(db.cattles.find())
    for cattle in response:
        del cattle["_id"]
    return jsonify(response), HTTPStatus.OK

def sell_a_cattle(brinco):
    response = db.cattles.find_one({"brinco":brinco})
    del response["_id"]
    area = db.areas.find_one({"area":response["area_inicial"]})
    animais_na_area = area["animais_na_area"]
    db.areas.update_one(area, {"$set": {"animais_na_area":animais_na_area-1}})
    db.cattles.delete_one({"brinco":brinco})
    return jsonify(), HTTPStatus.NO_CONTENT

def update_a_cattle(brinco):
    data = request.get_json()
    data_cattle = db.cattles.find_one({"brinco":brinco})
    if "dias_na_area" in data:
        dias_na_area = data["dias_na_area"]
    else:
        dias_na_area = data_cattle["dias_na_area"]
    segunda_area = db.areas.find_one({"area":data["area"]})
    cattle_area = db.areas.find_one({"area":data_cattle["area_inicial"]})
    peso_final = (cattle_area["gmd"]*data_cattle["dias_na_area"])+data_cattle["peso_inicial"]
    dias_na_area_antiga = data_cattle["dias_na_area"]
    animais_na_area_antiga = cattle_area["animais_na_area"]
    print(segunda_area)
    if segunda_area == None:
        return {"message":"Área não cadastrada"}, HTTPStatus.UNAUTHORIZED

    if segunda_area["area"]  == cattle_area["area"]:
        return {"message":"Este animal já está nesta área"}, HTTPStatus.UNAUTHORIZED
    
    if segunda_area == None:
        return {"message":"Área ainda não cadastrada"}, HTTPStatus.CONFLICT
    else:

        total_de_animais = segunda_area["total_de_animais"]
        animais_na_area = segunda_area["animais_na_area"]
        if animais_na_area == total_de_animais:
            return {"message":f"Já possui {total_de_animais} animais na área selecionada"}, HTTPStatus.UNAUTHORIZED
        
        db.areas.update_one(cattle_area,{"$set": {"animais_na_area":animais_na_area_antiga-1}})
        db.areas.update_one(segunda_area,{"$set":{"animais_na_area":animais_na_area+1}})
        db.cattles.update_one(data_cattle, {"$set":{"area_inicial":data["area"],"peso_inicial":peso_final, "dias_na_area":dias_na_area, "data_de_entrada":datetime.now().strftime("%d/%m/%y"), "data_de_saida": (datetime.now()+timedelta(dias_na_area_antiga)).strftime("%d/%m/%y")}})
        
        return show_a_cattle(brinco)