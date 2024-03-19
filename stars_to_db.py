import sqlite3 as sql
from tap_simbad import tap_simbad


SYSTEM_INSERT = """
INSERT INTO StarSystem (id, x, y, z)
VALUES (:id, :x, :y, :z);
"""

BODY_INSERT = """
INSERT INTO CelestialBody (id, flux_V, temperature_K, body_class, radius_km, system_id)
VALUES (:oid, :flux_v, :temperature, :sp_type, :radius_km, :system_id);
"""

NAME_INSERT = """
INSERT INTO CelestialBodyNames (body_name, body_id)
VALUES (:main_id, :oid);
"""


def masked_to_float(masked):
    try:
        return float(masked)
    except ValueError:
        return None


def masked_to_int(masked):
    try:
        return round(masked_to_float(masked))
    except ValueError:
        return None


def stars_from_simbad(radius=15.33):
    stars = tap_simbad(radius=radius)
    with sql.connect('database.sqlite3') as conn:
        cursor = conn.cursor()
        i = 0
        for values in stars.iterrows():
            i += 1
            star = {
                key: value for key, value in zip(stars.colnames, values)
            }

            system = {
                "id": masked_to_int(star["oid"]),
                "x": masked_to_float(star["x"]),
                "y": masked_to_float(star["y"]),
                "z": masked_to_float(star["z"])
            }

            body = {
                "oid": masked_to_int(star["oid"]),
                "flux_v": masked_to_float(star["flux_v"]),
                "temperature": masked_to_int(star["temperature"]),
                "sp_type": str(star["sp_type"]),
                "radius_km": masked_to_float(star["radius_km"]),
                "system_id": masked_to_int(star["oid"])
            }

            name = {
                "main_id": str(star["main_id"]),
                "oid": masked_to_int(star["oid"])
            }

            cursor.execute(SYSTEM_INSERT, system)
            cursor.execute(BODY_INSERT, body)
            cursor.execute(NAME_INSERT, name)
        conn.commit()
        print(f"Inserted {i} stars")


def main():
    stars_from_simbad()


if __name__ == "__main__":
    main()
