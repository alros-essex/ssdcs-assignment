//ID                  BIGINT         NOT NULL AUTO_INCREMENT,
//TYPE                SMALLINT       NOT NULL,
//TIMESTAMP           TIMESTAMP      NOT NULL,
//EXPERIMENT_ID       MEDIUMINT      NOT NULL,
//MEASURE_VALUE       DOUBLE         NOT NULL,

//create a data structure
export interface Measure{
    id: number;
    type: number;
    timestamp: string;
    experiment_id: number;
    measure_value: number;  
  }

