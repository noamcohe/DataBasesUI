"""
Authors: Noam Cohen & Assaf Bigel
"""


# Some imports:
import sqlite3
from flask import Flask, jsonify, request
import Utils
import Buildings
import Duties
import Equipment
import Lending
import Manufacturer
import Rooms
import Soldiers
import Vehicles


DB_PATH = 'C:\\Users\\noamc\\PycharmProjects\\DataBasesUI\\identifier.sqlite'


app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


@app.route('/')
def index():
    query = "select * from Equipment"
    with get_db_connection().cursor() as cursor:
        cursor.execute(query)
        result = Utils.cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/tables')
def get_table():
    table_name = request.args.get('table')
    return jsonify(Utils.get_table(get_db_connection(), table_name))


# ------------------------------------- Buildings -----------------------------------


@app.route('/Buildings/select')
def buildings_select():
    """Select"""
    result = Utils.get_table(get_db_connection(), 'Buildings')
    return jsonify({'data': result})


@app.route('/Buildings/delete')
def buildings_delete_row():
    """Delete"""
    bid = request.args.get('bid')
    try:
        Utils.delete_from_table(get_db_connection(), "Buildings", bid)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Buildings/update')
def buildings_update():
    """Update"""
    bid = request.args.get('bid')
    b_name = request.args.get('bName')
    position = request.args.get('position')
    b_description = request.args.get('bDescription')

    try:
        Buildings.update(get_db_connection(), bid, b_name, position, b_description)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Buildings/insert')
def buildings_insert():
    """Insert"""
    bid = request.args.get('bid')
    b_name = request.args.get('bName')
    position = request.args.get('position')
    b_description = request.args.get('bDescription')

    try:
        Buildings.insert(get_db_connection(), bid, b_name, position, b_description)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# ------------------------------------- Duties -----------------------------------


@app.route('/Duties/select')
def duties_select():
    """Select"""
    result = Utils.get_table(get_db_connection(), 'Duties')
    return jsonify({'data': result})


@app.route('/Duties/delete')
def duties_delete_row():
    """Delete"""
    did = request.args.get('did')
    try:
        Utils.delete_from_table(get_db_connection(), "Duties", did)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Duties/update')
def duties_update():
    """Update"""
    did = request.args.get('did')
    d_name = request.args.get('dName')
    d_description = request.args.get('dDescription')

    try:
        Duties.update(get_db_connection(), did, d_name, d_description)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Duties/insert')
def duties_insert():
    """Insert"""
    did = request.args.get('did')
    d_name = request.args.get('dName')
    d_description = request.args.get('dDescription')

    try:
        Duties.insert(get_db_connection(), did, d_name, d_description)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# ------------------------------------- Equipment -----------------------------------


@app.route('/Equipment/select')
def equipment_select():
    """Select"""
    result = Utils.get_table(get_db_connection(), 'Equipment')
    return jsonify({'data': result})


@app.route('/Equipment/delete')
def equipment_delete_row():
    """Delete"""
    e_id = request.args.get('Id')
    try:
        Utils.delete_from_table(get_db_connection(), "Equipment", e_id)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Equipment/update')
def equipment_update():
    """Update"""
    e_id = request.args.get('Id')
    name = request.args.get('Name')
    manu_id = request.args.get("ManufacturerId")
    min_of_stack = request.args.get("MinOfStack")
    amount = request.args.get("Amount")
    weight = request.args.get("Weight")
    worker = request.args.get("worker")
    room_id = request.args.get("roomId")
    e_description = request.args.get("eDescription")
    cost = request.args.get("cost")
    vehicle_id = request.args.get("onVehicleId")
    area = request.args.get("area")

    try:
        Equipment.update(get_db_connection(), e_id, name,
                         manu_id, min_of_stack, amount,
                         weight, worker, room_id,
                         e_description, cost, vehicle_id, area)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Equipment/insert')
def equipment_insert():
    """Insert"""
    e_id = request.args.get('Id')
    name = request.args.get('Name')
    manu_id = request.args.get("ManufacturerId")
    min_of_stack = request.args.get("MinOfStack")
    amount = request.args.get("Amount")
    weight = request.args.get("Weight")
    worker = request.args.get("worker")
    room_id = request.args.get("roomId")
    e_description = request.args.get("eDescription")
    cost = request.args.get("cost")
    vehicle_id = request.args.get("onVehicleId")
    area = request.args.get("area")

    try:
        Equipment.insert(get_db_connection(), e_id, name,
                         manu_id, min_of_stack, amount,
                         weight, worker, room_id,
                         e_description, cost, vehicle_id, area)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# ------------------------------------- Lending -----------------------------------


@app.route('/Lending/select')
def lending_select():
    """Select"""
    result = Utils.get_table(get_db_connection(), 'Lending')
    return jsonify({'data': result})


@app.route('/Lending/delete')
def lending_delete_row():
    """Delete"""
    soldier_id = request.args.get('SoldierId')
    try:
        Utils.delete_from_table(get_db_connection(), "Lending", soldier_id)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Lending/update')
def lending_update():
    """Update"""
    soldier_id = request.args.get('SoldierId')
    equipment_id = request.args.get('EquipmentId')
    date_of_lending = request.args.get("DateOfLending")
    equipment_weight = request.args.get("EquipmentWeight")
    date_of_return = request.args.get("DateOfReturn")

    try:
        Lending.update(get_db_connection(), soldier_id, equipment_id,
                       date_of_lending, equipment_weight, date_of_return)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Lending/insert')
def lending_insert():
    """Insert"""
    soldier_id = request.args.get('SoldierId')
    equipment_id = request.args.get('EquipmentId')
    date_of_lending = request.args.get("DateOfLending")
    equipment_weight = request.args.get("EquipmentWeight")
    date_of_return = request.args.get("DateOfReturn")

    try:
        Lending.insert(get_db_connection(), soldier_id, equipment_id,
                       date_of_lending, equipment_weight, date_of_return)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# ------------------------------------- Manufacturer ---------------------------------


@app.route('/Manufacturer/select')
def manufacturer_select():
    """Select"""
    result = Utils.get_table(get_db_connection(), 'Manufacturer')
    return jsonify({'data': result})


@app.route('/Manufacturer/delete')
def manufacturer_delete_row():
    """Delete"""
    m_id = request.args.get('Id')
    try:
        Utils.delete_from_table(get_db_connection(), "Manufacturer", m_id)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Manufacturer/update')
def manufacturer_update():
    """Update"""
    m_id = request.args.get('Id')
    name = request.args.get('Name')

    try:
        Manufacturer.update(get_db_connection(), m_id, name)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Manufacturer/insert')
def manufacturer_insert():
    """Insert"""
    m_id = request.args.get('Id')
    name = request.args.get('Name')

    try:
        Manufacturer.insert(get_db_connection(), m_id, name)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# ------------------------------------- Rooms ---------------------------------


@app.route('/Rooms/select')
def rooms_select():
    """Select"""
    result = Utils.get_table(get_db_connection(), 'Rooms')
    return jsonify({'data': result})


@app.route('/Rooms/delete')
def rooms_delete_row():
    """Delete"""
    rid = request.args.get('Id')
    try:
        Utils.delete_from_table(get_db_connection(), "Rooms", rid)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Rooms/update')
def rooms_update():
    """Update"""
    rid = request.args.get('rid')
    r_number = request.args.get('rNumber')
    building_id = request.args.get('buildingId')
    size = request.args.get('size')
    r_description = request.args.get('rDescription')
    num_of_soldiers = request.args.get('numOfSoldiers')
    max_soldiers = request.args.get('maxSoldiers')

    try:
        Rooms.update(get_db_connection(), rid, r_number,
                     building_id, size, r_description,
                     num_of_soldiers, max_soldiers)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Rooms/insert')
def rooms_insert():
    """Insert"""
    rid = request.args.get('rid')
    r_number = request.args.get('rNumber')
    building_id = request.args.get('buildingId')
    size = request.args.get('size')
    r_description = request.args.get('rDescription')
    num_of_soldiers = request.args.get('numOfSoldiers')
    max_soldiers = request.args.get('maxSoldiers')

    try:
        Rooms.insert(get_db_connection(), rid, r_number,
                     building_id, size, r_description,
                     num_of_soldiers, max_soldiers)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# ------------------------------------- Soldiers ---------------------------------


@app.route('/Soldiers/select')
def soldiers_select():
    """Select"""
    result = Utils.get_table(get_db_connection(), 'Soldiers')
    return jsonify({'data': result})


@app.route('/Soldiers/delete')
def soldiers_delete_row():
    """Delete"""
    soldier_id = request.args.get('soldierId')
    try:
        Utils.delete_from_table(get_db_connection(), "Soldiers", soldier_id)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Soldiers/update')
def soldiers_update():
    """Update"""
    soldier_id = request.args.get('soldierId')
    sl_name = request.args.get('slName')
    weight = request.args.get('Weight')
    sf_name = request.args.get('sfName')
    room_id = request.args.get('roomId')
    equ_id = request.args.get('equId')
    duty_id = request.args.get('dutyId')

    try:
        Soldiers.update(get_db_connection(), soldier_id, sl_name,
                        weight, sf_name, room_id,
                        equ_id, duty_id)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Soldiers/insert')
def soldiers_insert():
    """Insert"""
    soldier_id = request.args.get('soldierId')
    sl_name = request.args.get('slName')
    weight = request.args.get('Weight')
    sf_name = request.args.get('sfName')
    room_id = request.args.get('roomId')
    equ_id = request.args.get('equId')
    duty_id = request.args.get('dutyId')

    try:
        Soldiers.insert(get_db_connection(), soldier_id, sl_name,
                        weight, sf_name, room_id,
                        equ_id, duty_id)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# ------------------------------------- Vehicles ---------------------------------


@app.route('/Vehicles/select')
def vehicles_select():
    """Select"""
    result = Utils.get_table(get_db_connection(), 'Vehicles')
    return jsonify({'data': result})


@app.route('/Vehicles/delete')
def vehicles_delete_row():
    """Delete"""
    vid = request.args.get('vid')
    try:
        Utils.delete_from_table(get_db_connection(), "Vehicles", vid)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Vehicles/update')
def vehicles_update():
    """Update"""
    vid = request.args.get('vid')
    v_type = request.args.get('vType')
    v_model = request.args.get('vModel')
    building_id = request.args.get('buildingId')
    v_description = request.args.get('vDescription')
    max_weight = request.args.get('maxWight')

    try:
        Vehicles.update(get_db_connection(), vid, v_type,
                        v_model, building_id, v_description,
                        max_weight)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


@app.route('/Vehicles/insert')
def vehicles_insert():
    """Insert"""
    vid = request.args.get('vid')
    v_type = request.args.get('vType')
    v_model = request.args.get('vModel')
    building_id = request.args.get('buildingId')
    v_description = request.args.get('vDescription')
    max_weight = request.args.get('maxWight')

    try:
        Vehicles.insert(get_db_connection(), vid, v_type,
                        v_model, building_id, v_description,
                        max_weight)
        return "success"

    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return "failed"


# *********************************************************************************
# -------------------------------------- Queries ----------------------------------
# *********************************************************************************


@app.route('/query/all_rooms')
def all_rooms():
    result = Utils.execute_select(get_db_connection(), 'Queries/all_rooms.sql')
    return jsonify({'data': result})


@app.route('/query/building_equip_query')
def building_equip_query():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/building_equip_query.sql')
    return jsonify({'data': result})


@app.route('/query/dwork_products')
def dwork_products():
    result = Utils.execute_select(get_db_connection(), 'Queries/dwork_products.sql')
    return jsonify({'data': result})


@app.route('/query/eweight_prec_from_bweight')
def eweight_prec_from_bweight():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/eweight_prec_from_bweight.sql')
    return jsonify({'data': result})


@app.route('/query/have_gun')
def have_gun():
    result = Utils.execute_select(get_db_connection(), 'Queries/have_gun.sql')
    return jsonify({'data': result})


@app.route('/query/have_prod_dwork')
def have_prod_dwork():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/have_prod_dwork.sql')
    return jsonify({'data': result})


@app.route('/query/lent_many_times')
def lent_many_times():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/lent_many_times.sql')
    return jsonify({'data': result})


@app.route('/query/man_have_eq_now_in_room')
def man_have_eq_now_in_room():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/man_have_eq_now_in_room.sql')
    return jsonify({'data': result})


@app.route('/query/most_expensive')
def most_expensive():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/most_expensive.sql')
    return jsonify({'data': result})


@app.route('/query/only_work_prod')
def only_work_prod():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/only_work_prod.sql')
    return jsonify({'data': result})


@app.route('/query/out_of_stack')
def out_of_stack():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/out_of_stack.sql')
    return jsonify({'data': result})


@app.route('/query/room_hold_too_much_eq')
def room_hold_too_much_eq():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/room_hold_too_much_eq.sql')
    return jsonify({'data': result})


@app.route('/query/vweight_more_than_can')
def vweight_more_than_can():
    result = Utils.execute_select(get_db_connection(),
                                  'Queries/vweight_more_than_can.sql')
    return jsonify({'data': result})


# *********************************************************************************
# ------------------------------ Queries with params ------------------------------
# *********************************************************************************


@app.route('/query/all_products_that_soldier_took')
def all_products_that_soldier_took():
    soldier_id = request.args.get('soldierId')
    with open(r"QueriesWithParams/all_products_that_soldier_took.sql") as query:
        with get_db_connection().cursor() as cursor:
            temp = query.read().replace(":soldierId", soldier_id)
            cursor.execute(temp)
            result = Utils.cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/query/prod_from_spe_man')
def prod_from_spe_man():
    company_id = request.args.get('companyId')
    with open(r"QueriesWithParams/prod_from_spe_man.sql") as query:
        with get_db_connection().cursor() as cursor:
            temp = query.read().replace(":companyId", company_id)
            cursor.execute(temp)
            result = Utils.cursor_result_to_json(cursor)
    return jsonify({'data': result})


@app.route('/query/weight_all_prod_sold_took')
def weight_all_prod_sold_took():
    soldier_id = request.args.get('soldierId')
    with open(r"QueriesWithParams/weight_all_prod_sold_took.sql") as query:
        with get_db_connection().cursor() as cursor:
            temp = query.read().replace(":soldierId", soldier_id)
            cursor.execute(temp)
            result = Utils.cursor_result_to_json(cursor)
    return jsonify({'data': result})


# *********************************************************************************
# ------------------------------ Views --------------------------------------------
# *********************************************************************************


@app.route('/view/building_equipment')
def building_equipment():
    result = Utils.get_table(get_db_connection(), 'building_equipment')
    return jsonify({'data': result})


@app.route('/view/dwork_sol_equipment')
def dwork_sol_equipment():
    result = Utils.get_table(get_db_connection(), 'dwork_sol_equipment')
    return jsonify({'data': result})


@app.route('/view/room_equipment')
def room_equipment():
    result = Utils.get_table(get_db_connection(), 'room_equipment')
    return jsonify({'data': result})


@app.route('/view/work_soldiers_equipment')
def room_equipment():
    result = Utils.get_table(get_db_connection(), 'work_soldiers_equipment')
    return jsonify({'data': result})


app.run()
