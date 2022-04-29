--
-- MyMONIT DB Schema definition
-- 
--
-- definition of the USER_EXPERIMENTS table

use my_monit;

-- models the relation between experiments and users

CREATE TABLE USER_EXPERIMENTS
(
    USER_ID           VARCHAR(30)      NOT NULL,
    EXPERIMENT_ID     MEDIUMINT        NOT NULL,
    
    PRIMARY KEY(USER_ID, EXPERIMENT_ID),
    FOREIGN KEY (USER_ID) REFERENCES USERS(ID),
    FOREIGN KEY (EXPERIMENT_ID) REFERENCES EXPERIMENTS(ID)
);

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