
    CREATE TABLE Region (
        ID_Region INT PRIMARY KEY,
        Nom VARCHAR(50) NOT NULL,
        Population INT
    );
    
    CREATE TABLE Departement (
        ID_Departement INT PRIMARY KEY,
        Nom VARCHAR(50) NOT NULL,
        ID_Region INT,
        FOREIGN KEY (ID_Region) REFERENCES Region(ID_Region)
    );
    
    CREATE TABLE Commune (
        ID_Commune INT PRIMARY KEY,
        Nom VARCHAR(50) NOT NULL,
        Code_Postal VARCHAR(10),
        ID_Region INT,
        ID_Departement INT,
        FOREIGN KEY (ID_Region) REFERENCES Region(ID_Region),
        FOREIGN KEY (ID_Departement) REFERENCES Departement(ID_Departement)
    );
    
    CREATE TABLE Bien (
        ID_Bien INT PRIMARY KEY,
        Type VARCHAR(30),
        Surface DECIMAL(10,2),
        ID_Commune INT,
        FOREIGN KEY (ID_Commune) REFERENCES Commune(ID_Commune)
    );
    
    CREATE TABLE Transaction (
        ID_Transaction INT PRIMARY KEY,
        Date DATE NOT NULL,
        Prix DECIMAL(15,2),
        ID_Bien INT,
        FOREIGN KEY (ID_Bien) REFERENCES Bien(ID_Bien)
    );
    