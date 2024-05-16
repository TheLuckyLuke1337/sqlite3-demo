import sqlite3 as sql


def main():
    with open('users.sql') as f:
        with sql.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.executescript(f.read())

        conn.commit()


if __name__ == '__main__':
    main()