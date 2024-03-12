from astroquery.simbad import Simbad


result_table = Simbad.query_criteria(
    "Distance.unit = 'pc'", "Distance.distance < 15.33")

for row in result_table:
    print(row["MAIN_ID"])

print(len(result_table))
