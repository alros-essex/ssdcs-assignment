use safe_repository;

CREATE TABLE User
(
    STAFF_ID       INT NOT NULL AUTO_INCREMENT,      
   `USER_NAME`     VARCHAR(30) NOT NULL,
    EMAIL          VARCHAR(100) NOT NULL,

    PRIMARY KEY (STAFF_ID)
     
);
