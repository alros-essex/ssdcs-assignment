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
    USERNAME       VARCHAR(30)      NOT NULL,
    EMAIL          VARCHAR(100)     NOT NULL,
    ROLE           TINYINT          NOT NULL,
    
    PRIMARY KEY(ID),
    FOREIGN KEY (ROLE) REFERENCES ROLES(ID)
);

INSERT INTO USERS(ID, NAME, USERNAME, EMAIL, ROLE)
VALUES(
    'A001', 
    'Default Admin',
    'admin',
    'noreply@localhost', 
    (SELECT ID FROM ROLES WHERE NAME = 'ADMIN')
);

INSERT INTO USERS(ID, NAME, USERNAME, EMAIL, ROLE)
VALUES(
    'S001', 
    'Peter Higg',
    'phigg',
    'phigg@localhost', 
    (SELECT ID FROM ROLES WHERE NAME = 'SCIENTIST')
);

INSERT INTO USERS(ID, NAME, USERNAME, EMAIL, ROLE)
VALUES(
    'S002', 
    'Katie Bouman',
    'kbouman',
    'kbouman@localhost', 
    (SELECT ID FROM ROLES WHERE NAME = 'SCIENTIST')
);