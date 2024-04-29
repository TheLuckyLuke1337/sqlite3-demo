import sqlite3 as sql


def main():
    with open("sample_users.sql") as f:
        script = f.read()

    with sql.connect("database.sqlite3") as conn:
        cursor = conn.cursor()
        cursor.executescript(script)


if __name__ == "__main__":
    main()
