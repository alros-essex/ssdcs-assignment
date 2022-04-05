use safe_repository;

CREATE TABLE Admin
(
    STAFF_ID       INT NOT NULL AUTO_INCREMENT,      
    `ROLE`         VARCHAR(30) NOT NULL,
             
    PRIMARY KEY (STAFF_ID),
    FOREIGN KEY (STAFF_ID) REFERENCES User(STAFF_ID)
     
);