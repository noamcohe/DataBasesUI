import Utils


def insert(sqlite_connection, bid, b_name, position, b_description):
    query = f"insert into Buildings(bid, bName, position, bDescription) " \
            f"values({bid},'{b_name}','{position}',{b_description})"
    Utils.execute_action(sqlite_connection, query)


def update(sqlite_connection, bid, b_name, position, b_description):
    query = f"update Buildings " \
            f"set " \
            f"bName='{b_name}', " \
            f"position='{position}', " \
            f"bDescription='{b_description}' " \
            f"where bid={bid}"
    Utils.execute_action(sqlite_connection, query)
