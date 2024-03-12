from astroquery.simbad import Simbad

parsec_distance = 15.33

result_table = Simbad.query_criteria(
    "Distance.unit = 'pc'", f"Distance.distance < {parsec_distance}")

for row in result_table:
    print(row["MAIN_ID"])

print(len(result_table))
