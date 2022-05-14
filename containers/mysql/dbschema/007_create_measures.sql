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
    FOREIGN KEY (TYPE) REFERENCES MEASURE_TYPES(ID),
    FOREIGN KEY (EXPERIMENT_ID) REFERENCES EXPERIMENTS(ID)
);
