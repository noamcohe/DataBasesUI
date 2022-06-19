import Utils


def insert(sqlite_connection, soldier_id, equipment_id, date_of_lending, equipment_weight, date_of_return):
    query = f"insert into Lending(SoldierId, EquipmentId, DateOfLending, EquipmentWeight, DateOfReturn) " \
            f"values({soldier_id}, {equipment_id}, {date_of_lending}, {equipment_weight}, {date_of_return})"
    Utils.execute_action(sqlite_connection, query)


def update(sqlite_connection, soldier_id, equipment_id, date_of_lending, equipment_weight, date_of_return):
    query = f"update Lending " \
            f"set " \
            f"EquipmentId='{equipment_id}', " \
            f"DateOfLending='{date_of_lending}', " \
            f"EquipmentWeight={equipment_weight}, " \
            f"DateOfReturn={date_of_return} " \
            f"where SoldierId={soldier_id}"
    Utils.execute_action(sqlite_connection, query)
