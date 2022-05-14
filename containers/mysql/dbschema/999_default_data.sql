--
-- MyMONIT DB Data examples
-- 
--
-- adds examples for evaluation purposes
--
-- delete this script in a production environment

--
-- add some users
--

use my_monit;

INSERT INTO USERS(ID, NAME, USERNAME, EMAIL, ROLE)
VALUES(
    'A001', 
    'Allan Alcorn',
    '5MS0kr1nE5Qm7ZNzAyHNCVfapcf2',
    'aalcorn@home.cern',
    (SELECT ID FROM ROLES WHERE NAME = 'ADMIN')
);

INSERT INTO USERS(ID, NAME, USERNAME, EMAIL, ROLE)
VALUES(
    'S001', 
    'Peter Higg',
    'uJayGH994iVa2TY5auSNYZoUpwk1',
    'phigg@home.cern', 
    (SELECT ID FROM ROLES WHERE NAME = 'SCIENTIST')
);

INSERT INTO USERS(ID, NAME, USERNAME, EMAIL, ROLE)
VALUES(
    'S002', 
    'Katie Bouman',
    'hirbBCceXlWUGdpNHUpaNtworjm2',
    'kbouman@home.cern', 
    (SELECT ID FROM ROLES WHERE NAME = 'SCIENTIST')
);

--
-- add some experiments
--
INSERT INTO EXPERIMENTS(NAME) VALUE('device-vibrations');

INSERT INTO EXPERIMENTS(NAME) VALUE('black-holes');


--
-- links users with experiments
--

INSERT INTO USER_EXPERIMENTS(USER_ID, EXPERIMENT_ID)
VALUES(
    (SELECT ID FROM USERS WHERE NAME = 'Peter Higg'),
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations')
);

INSERT INTO USER_EXPERIMENTS(USER_ID, EXPERIMENT_ID)
VALUES(
    (SELECT ID FROM USERS WHERE NAME = 'Katie Bouman'),
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'black-holes')
);

--
-- inserts examples of measures
--

INSERT INTO MEASURES(TYPE, TIMESTAMP, EXPERIMENT_ID, MEASURE_VALUE)
VALUES
(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:00:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    100
),(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:01:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    95
),(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:02:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    94
),(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:03:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    110
),(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:04:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    120
),(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:05:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    130
),(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:06:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    110
),(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:07:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    110
),(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:08:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    105
),(
    (SELECT ID FROM MEASURE_TYPES WHERE NAME = 'hertz'),
    '2022-04-06 7:09:00',
    (SELECT ID FROM EXPERIMENTS WHERE NAME = 'device-vibrations'),
    120
)