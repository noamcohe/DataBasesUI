import Utils


def insert(sqlite_connection,
           e_id, e_name, manufacturer_id,
           min_of_stack, amount, weight,
           worker, room_id, e_description,
           cost, on_vehicle_id, area):
    query = f"insert into Equipment(Id, Name, ManufacturerId," \
            f"MinOfStack, Amount, Weight," \
            f"worker, roomId, eDescription," \
            f"cost, onVehicleId, area) " \
            f"values({e_id},'{e_name}',{manufacturer_id}," \
            f"{min_of_stack}, {amount}, {weight}," \
            f"{worker}, {room_id}, '{e_description}'," \
            f"{cost}, {on_vehicle_id}, {area})"
    Utils.execute_action(sqlite_connection, query)


def update(sqlite_connection,
           e_id, e_name, manufacturer_id,
           min_of_stack, amount, weight,
           worker, room_id, e_description,
           cost, on_vehicle_id, area):
    query = f"update Equipment " \
            f"set " \
            f"Name='{e_name}', " \
            f"ManufacturerId={manufacturer_id}, " \
            f"MinOfStack={min_of_stack}, " \
            f"Amount={amount}, " \
            f"Weight={weight}, " \
            f"worker={worker}, " \
            f"roomId='{room_id}', " \
            f"eDescription='{e_description}', " \
            f"cost='{cost}', " \
            f"onVehicleId='{on_vehicle_id}', " \
            f"area={area} " \
            f"where Id={e_id}"
    Utils.execute_action(sqlite_connection, query)
