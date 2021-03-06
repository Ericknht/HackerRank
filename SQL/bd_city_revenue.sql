CREATE TABLE IF NOT EXISTS CITIES (
    `CITY_CODE` INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `CITY_NAME` VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS REVENUE (
    `REVENUE_CODE` INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `CITY_CODE` INTEGER UNSIGNED,
    `REVENUE` INTEGER
);

INSERT INTO CITIES(`CITY_NAME`)
VALUES('New York'), ('London'), ('Paris');

INSERT INTO REVENUE(`CITY_CODE`, `REVENUE`)
VALUES(1, 10), (2, 5),(2, 10), (3, 15);