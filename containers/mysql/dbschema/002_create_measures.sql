use my_monit;

CREATE TABLE measures
(
    ID                  INT NOT NULL AUTO_INCREMENT,
    EXPERIMENT_ID       INT NOT NULL,
    MEASURE_ID          VARCHAR(30) NOT NULL,
    MEASURE_VALUE       INT NOT NULL,

    PRIMARY KEY (ID)
);
