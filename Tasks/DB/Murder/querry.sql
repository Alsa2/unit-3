-- SQLite
SELECT name FROM sqlite_master WHERE type='table';

SELECT * FROM crime_scene_report;

SELECT * FROM crime_scene_report WHERE date = "20180115" AND city = "SQL City";

SELECT * FROM person WHERE address_street_name = "Northwestern Dr" ORDER BY address_number DESC;

SELECT * FROM person WHERE address_street_name = "Franklin Ave" AND name LIKE "Annabel%";

SELECT * FROM person WHERE id = 14887;

SELECT * FROM interview where person_id = 14887 OR person_id = 16371;

SELECT * FROM get_fit_now_member WHERE id LIKE "48Z%" AND membership_status = "gold";

SELECT * FROM get_fit_now_check_in WHERE membership_id LIKE "48Z%" AND check_in_date = "20180109" AND membership_id = "48Z7A" OR membership_id = "48Z55";

SELECT * FROM person WHERE name = "Joe Germuska" OR name = "Jeremy Bowers";

SELECT * FROM facebook_event_checkin WHERE person_id = 28819 OR person_id = 67318;

INSERT INTO solution VALUES (1, "Jeremy Bowers");

SELECT value FROM solution;


SELECT * FROM interview WHERE person_id = "67318";

SELECT * FROM drivers_license WHERE car_make = "Tesla" AND car_model = "Model S" AND gender = "female";

SELECT * FROM person;

SELECT * FROM person WHERE license_id = "918773" OR license_id = "291182" OR license_id = "202298"; 

SELECT * FROM income WHERE ssn = "961388910" OR ssn = "337169072" OR ssn = "987756388";

INSERT INTO solution VALUES (1, "Miranda Priestly");

SELECT value FROM solution;