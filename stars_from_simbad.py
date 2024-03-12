from astroquery.simbad import Simbad
# test star "* tet Per"
parsec_distance = 15.33  # 15.33
result_table = Simbad.query_criteria(
    "Distance.unit = 'pc'",
    f"Distance.distance < {parsec_distance}")


for row in result_table:
    try:
        Simbad.add_votable_fields("distance", "diameter")
        object = Simbad.query_object(row["MAIN_ID"])
        if object["Diameter_unit"] != "mas":
            continue
        print(object["MAIN_ID"], object["Distance_distance"],
              object["Distance_unit"], object["Diameter_diameter"], object["Diameter_unit"], sep="\n")
    except Exception as e:
        print(row["MAIN_ID"], row["RA"], row["DEC"], "No measurements")
        print(e)
print(len(result_table))
