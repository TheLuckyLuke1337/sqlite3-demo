import sqlite3 as sql


def main():
    with open("anotherTest.sql") as f:
        with sql.connect("old_database.sqlite3") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT count(*) FROM CelestialBodyNames")
            result = cursor.fetchall()
            print(result)


if __name__ == "__main__":
    main()
