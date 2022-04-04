--
-- MyMONIT DB Schema definition
-- 
--
-- definition of the ROLES table

use my_monit;

-- models a role as
-- * id: unique id
-- * name: role's short name

CREATE TABLE ROLES
(
    ID          TINYINT      NOT NULL AUTO_INCREMENT,
    NAME        VARCHAR(9)   NOT NULL,

    PRIMARY KEY(ID)
);

INSERT INTO ROLES(NAME) VALUES
    ('ADMIN'),
    ('SCIENTIST');