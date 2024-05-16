import sqlite3 as sql


def main():
    with open('uhhtest.sql') as f:
        with sql.connect('old_database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT body_class FROM CelestialBody")
            result = cursor.fetchall()
            classes = []
            print(result[0][0][0])
            for body_class in result:

                if (body_class[0] != "" and body_class[0][0] in "dks"):
                    print(body_class[0])

                
                if (body_class[0] != "" and body_class[0][0] not in classes):
                    classes.append(body_class[0][0])
            print(classes)

'''
K: MS 3400 - 4900
M: MS 2100 - 3400
G: MS 4900 - 5700
D: White dwarfs
F: MS 5700 - 7200
d (dM): Dwarfs with calcuim emission lines. 
T: Cool brown dwarfs
L: Dwarfs
k (kA5hF0mF2III): prefix for "calcium K-line", kA5hF0mF2III is A(5)
s (sd): (cool) Subdwarf
A: MS 7200 - 9700
Y: Even cooler brown dwarfs
For the dM classification: https://adsabs.harvard.edu/full/1974ApJS...28....1J
For the k classification: https://www.star-facts.com/deneb-algedi/
The rest: https://en.wikipedia.org/wiki/Stellar_classification
'''

        


if __name__ == '__main__':
    main()