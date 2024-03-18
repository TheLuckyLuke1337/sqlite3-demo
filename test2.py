import pyvo
from cartesian import polar2cartesian

tap_service_url = "http://simbad.cds.unistra.fr/simbad/sim-tap"

tap_service = pyvo.dal.TAPService(tap_service_url)

query = """
SELECT oid,
AVG(teff) AS avg_temperature,
AVG(diameter) AS avg_diameter,
AVG(dist) AS avg_distance, ra, dec,
sp_type, main_id, AVG(allfluxes.v) as avg_v
FROM basic
JOIN mesDiameter ON basic.oid = mesDiameter.oidref
JOIN mesDistance ON basic.oid = mesDistance.oidref
JOIN mesSpT ON basic.oid = mesSpT.oidref
JOIN mesFe_H ON basic.oid = mesFe_H.oidref
JOIN allfluxes ON basic.oid = allfluxes.oidref
WHERE mesDiameter.unit = 'km'
AND mesDistance.unit = 'pc'
GROUP BY basic.oid;
"""


table = tap_service.run_async(query).to_table()


table["x"], table["y"], table["z"] = polar2cartesian(
    table["ra"], table["dec"], table["avg_distance"])

print(table["x", "y", "z", "avg_v", "avg_temperature",
            "avg_diameter", "sp_type", "main_id",
            ])
