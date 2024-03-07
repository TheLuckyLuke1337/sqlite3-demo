CREATE TABLE StarSystem (
    id INTEGER PRIMARY KEY,
    x REAL NOT NULL,
    y REAL NOT NULL,
    z REAL NOT NULL
);

CREATE TABLE CelestialBody (
    id INTEGER PRIMARY KEY,
    temperature_K REAL NOT NULL,
    radius_km REAL NOT NULL,
    mass_M REAL NOT NULL,
    system_id INTEGER NOT NULL,
    apoapsis_au REAL NOT NULL,
    periapsis_au REAL NOT NULL,
    FOREIGN KEY (system_id) REFERENCES StarSystem(id)
);

CREATE TABLE CelestialBodyNames (
    name TEXT NOT NULL PRIMARY KEY,
    body_id INTEGER NOT NULL,
    FOREIGN KEY (body_id) REFERENCES CelestialBody(id)
);

CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    last_login TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL
);

CREATE TABLE List (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE ListEntry (
    list_id INTEGER NOT NULL,
    body_id INTEGER NOT NULL,
    FOREIGN KEY (list_id) REFERENCES List(id),
    FOREIGN KEY (body_id) REFERENCES CelestialBody(id)
);
