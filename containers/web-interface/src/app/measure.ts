// ID                  BIGINT         NOT NULL AUTO_INCREMENT,
// TYPE                SMALLINT       NOT NULL,
// TIMESTAMP           TIMESTAMP      NOT NULL,
// EXPERIMENT_ID       MEDIUMINT      NOT NULL,
// MEASURE_VALUE       DOUBLE         NOT NULL,

// create a data structure
export interface Measure {
    id: string;
    measure_type: string;
    timestamp: string;
    experiment: string;
    value: string;
}
