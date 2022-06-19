import Utils


def insert(sqlite_connection, m_id, name):
    query = f"insert into Manufacturer(Id, Name) " \
            f"values({m_id},{name})"
    Utils.execute_action(sqlite_connection, query)


def update(sqlite_connection, m_id, name):
    query = f"update Manufacturer " \
            f"set " \
            f"Name='{name}' " \
            f"where Id={m_id}"
    Utils.execute_action(sqlite_connection, query)
