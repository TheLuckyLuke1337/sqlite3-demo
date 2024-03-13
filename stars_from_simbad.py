from astroquery.simbad import Simbad
# test star "* tet Per"
parsec_distance = 2  # 15.33
Simbad.add_votable_fields("distance", "diameter", "flux(U)", "flux(B)",
                          "flux(V)", "flux(R)", "flux(I)", "flux(J)", "flux(H)", "flux(K)", "flux(G)")
result_table = Simbad.query_criteria(
    "Distance.unit = 'pc'",
    f"Distance.distance < {parsec_distance}")

print(result_table["MAIN_ID", "FLUX_J", "FLUX_H", "FLUX_K", "FLUX_G",
      "FLUX_U", "FLUX_B", "FLUX_V", "FLUX_R", "FLUX_I"])
