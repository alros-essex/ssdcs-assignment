--
-- MyMONIT DB Schema definition
-- 
--
-- definition of the USERS table

use my_monit;

-- models a user as
-- * id: staff id as defined by HR
-- * name: given name
-- * surname: family name
-- * email: professional email
-- * role: role's id as defined in the ROLES table

CREATE TABLE USERS
(
    ID             VARCHAR(30)      NOT NULL,
    NAME           VARCHAR(50)      NOT NULL,
    EMAIL          VARCHAR(50)      NOT NULL,
    ROLE           TINYINT          NOT NULL,
    
    PRIMARY KEY(ID),
    FOREIGN KEY (ROLE) REFERENCES ROLES(ID)
);

INSERT INTO USERS(ID, NAME, EMAIL, ROLE)
VALUES(
    'none', 
    'Default User', 
    'noreply@localhost', 
    (SELECT ID FROM ROLES WHERE NAME = 'ADMIN')
);