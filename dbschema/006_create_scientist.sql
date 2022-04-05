use safe_repository;

CREATE TABLE Scientist
(
    STAFF_ID       INT NOT NULL AUTO_INCREMENT,      
    EXPERIMENT     VARCHAR(30) NOT NULL,
             
    PRIMARY KEY (STAFF_ID),
    FOREIGN KEY (STAFF_ID) REFERENCES User(STAFF_ID)
     
);

-- Different scientists can have many experiments --


CREATE TABLE Scientist_Experiment
(
    SCIENTIST_ID       INT NOT NULL,      
    EXPERIMENT_ID      INT NOT NULL,   
    
 -- You cannot have the sanme combination more than once)

    PRIMARY KEY (SCIENTIST_ID, EXPERIMENT_ID),         
    FOREIGN KEY (SCIENTIST_ID) REFERENCES Scientist(STAFF_ID),
    FOREIGN KEY (EXPERIMENT_ID) REFERENCES Experiment(ID)
    
);

