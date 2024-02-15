INSERT INTO StarSystem (id, x, y, z) VALUES
(1, 25.0, -10.5, 100.0);

INSERT INTO CelestialBody (id, temperature_K, radius_km, mass_M, system_id) VALUES
(1, 5778, 696340, 1.0, 1),
(2, 200, 2370, 0.002, 1);

INSERT INTO CelestialBodyNames (name, body_id) VALUES
('Solara', 1),
('Tiny Cold One', 2);

INSERT INTO User (id, username, password, is_admin) VALUES
(1, 'star_gazer', 'password123', FALSE),
(2, 'admin_user', 'securePass!9', TRUE);

INSERT INTO List (id, name, user_id) VALUES
(1, 'Favorite Star Systems', 1),
(2, 'Observation List', 1);

INSERT INTO ListEntry (list_id, body_id) VALUES
(1, 1),
(2, 2);
