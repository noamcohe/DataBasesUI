import Utils


def insert(sqlite_connection, soldier_id, sl_name,
           weight, sf_name, room_id, equ_id, duty_id):
    query = f"insert into Soldiers(soldierId, slName, Weight," \
            f"sfName, roomId, equId, dutyId) " \
            f"values({soldier_id}, '{sl_name}', {weight}," \
            f"'{sf_name}', {room_id}, {equ_id}, {duty_id})"
    Utils.execute_action(sqlite_connection, query)


def update(sqlite_connection, soldier_id, sl_name,
           weight, sf_name, room_id, equ_id, duty_id):
    query = f"update Soldiers " \
            f"set " \
            f"slName='{sl_name}', " \
            f"Weight='{weight}', " \
            f"sfName='{sf_name}', " \
            f"roomId='{room_id}', " \
            f"equId='{equ_id}', " \
            f"dutyId={duty_id} " \
            f"where soldierId={soldier_id}"
    Utils.execute_action(sqlite_connection, query)
