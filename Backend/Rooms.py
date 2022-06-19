import Utils


def insert(sqlite_connection, rid, r_number,
           building_id, size, r_description,
           num_of_soldiers, max_soldiers):
    query = f"insert into Rooms(rid, rNumber, buildingId," \
            f"size, rDescription, numOfSoldiers, maxSoldiers) " \
            f"values({rid}, {r_number}, {building_id}," \
            f"{size}, '{r_description}', {num_of_soldiers}, {max_soldiers})"
    Utils.execute_action(sqlite_connection, query)


def update(sqlite_connection, rid, r_number,
           building_id, size, r_description,
           num_of_soldiers, max_soldiers):
    query = f"update Rooms " \
            f"set " \
            f"rNumber='{r_number}', " \
            f"buildingId='{building_id}', " \
            f"size='{size}', " \
            f"rDescription='{r_description}', " \
            f"numOfSoldiers='{num_of_soldiers}', " \
            f"maxSoldiers={max_soldiers} " \
            f"where rid={rid}"
    Utils.execute_action(sqlite_connection, query)
