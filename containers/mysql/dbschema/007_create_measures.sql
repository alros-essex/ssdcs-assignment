--
-- MyMONIT DB Schema definition
-- 
--
-- definition of the MEASURES table

use my_monit;

-- models a measure as
-- * id: synthetic key
-- * type: as defined in the MEASURE_TYPES table
-- * timestamp: when the measure was collected
-- * experiment id: as defined in the EXPERIMENTS table
-- * measure value: value of the measure

CREATE TABLE MEASURES
(
    ID                  BIGINT         NOT NULL AUTO_INCREMENT,
    TYPE                SMALLINT       NOT NULL,
    TIMESTAMP           TIMESTAMP      NOT NULL,
    EXPERIMENT_ID       MEDIUMINT      NOT NULL,
    MEASURE_VALUE       DOUBLE         NOT NULL,
    
    PRIMARY KEY(ID),
    FOREIGN KEY (TYPE) REFERENCES MEASURE_TYPES(ID)
);

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