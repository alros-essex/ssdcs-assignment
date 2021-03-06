--
-- MyMONIT DB Schema definition
-- 
--
-- definition of the EXPERIMENTS table

use my_monit;

-- models an experiment as
-- * id: unique syntetic id
-- * name: human readable name of the experiment

CREATE TABLE EXPERIMENTS
(
    ID       MEDIUMINT      NOT NULL AUTO_INCREMENT,
    NAME     VARCHAR(255)   NOT NULL UNIQUE,
    
    PRIMARY KEY(ID)
);
