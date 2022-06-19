import Utils


def insert(sqlite_connection, vid, v_type,
           v_model, building_id, v_description, max_weight):
    query = f"insert into Vehicles(vid, vType, vModel," \
            f"buildingId, vDescription, maxWight) " \
            f"values({vid}, '{v_type}', '{v_model}'," \
            f"{building_id}, '{v_description}', {max_weight})"
    Utils.execute_action(sqlite_connection, query)


def update(sqlite_connection, vid, v_type,
           v_model, building_id, v_description, max_weight):
    query = f"update Vehicles " \
            f"set " \
            f"vType='{v_type}', " \
            f"vModel='{v_model}', " \
            f"buildingId='{building_id}', " \
            f"vDescription='{v_description}', " \
            f"maxWight={max_weight} " \
            f"where vid={vid}"
    Utils.execute_action(sqlite_connection, query)
