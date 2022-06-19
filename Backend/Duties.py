import Utils


def insert(sqlite_connection, did, d_name, d_description):
    query = f"insert into Duties(did, dName, dDescription) " \
            f"values({did},'{d_name}','{d_description}')"
    Utils.execute_action(sqlite_connection, query)


def update(sqlite_connection, did, d_name, d_description):
    query = f"update Duties " \
            f"set " \
            f"dName='{d_name}', " \
            f"dDescription='{d_description}' " \
            f"where did={did}"
    Utils.execute_action(sqlite_connection, query)
