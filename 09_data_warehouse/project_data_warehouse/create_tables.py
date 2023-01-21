import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """

    Method to drop tables.

    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """

    Method to create staging and dimensional tables.

    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """

    Method to create database.

    """
    config = configparser.ConfigParser()
    config.read_file(open("dwh.cfg"))

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            config.get("DWH", "DWH_HOST"),
            config.get("DWH", "DWH_DB"),
            config.get("DWH", "DWH_DB_USER"),
            config.get("DWH", "DWH_DB_PASSWORD"),
            config.get("DWH", "DWH_PORT"),
        )
    )
    print("Connected to redshift")
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
