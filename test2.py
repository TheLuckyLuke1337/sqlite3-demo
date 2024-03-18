import pyvo
from cartesian import polar2cartesian
from astropy.table import Table

tap_service_url = "http://simbad.cds.unistra.fr/simbad/sim-tap"

tap_service = pyvo.dal.TAPService(tap_service_url)

query = """
SELECT oid,
AVG(teff) AS avg_temperature,
AVG(diameter) AS avg_diameter,
AVG(dist) AS avg_distance, ra, dec,
sp_type, main_id, AVG(allfluxes.v) as avg_v
FROM basic
JOIN mesDistance ON basic.oid = mesDistance.oidref
LEFT JOIN mesDiameter ON basic.oid = mesDiameter.oidref AND mesDiameter.unit = 'km'
LEFT JOIN mesSpT ON basic.oid = mesSpT.oidref
LEFT JOIN mesFe_H ON basic.oid = mesFe_H.oidref
JOIN allfluxes ON basic.oid = allfluxes.oidref
AND mesDistance.unit = 'pc'
AND mesDistance.dist < 15.33
GROUP BY basic.oid;
"""


table = tap_service.run_async(query).to_table()


table["x"], table["y"], table["z"] = polar2cartesian(
    table["ra"], table["dec"], table["avg_distance"])
result = Table()

result_keys = ["x", "y", "z", "flux_v", "temperature", "sp_type", "main_id"]
table_keys = ["x", "y", "z", "avg_v", "avg_temperature", "sp_type", "main_id"]
for result_key, table_key in zip(result_keys, table_keys):
    result[result_key] = table[table_key]
result["radius_km"] = table["avg_diameter"] / 2
print(result.colnames)
