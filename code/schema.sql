-- CRÉATION DE LA BDD

CREATE TABLE Personnes(nom TEXT,prénom TEXT,statut TEXT,adresse TEXT,téléphone INTEGER,personneID INTEGER PRIMARY KEY);
CREATE TABLE Étudiants(cours TEXT,parcours TEXT,étudiantID INTEGER PRIMARY KEY);
CREATE TABLE Parcours(nom TEXT,secrétaire TEXT,directeur TEXT,parcoursID INTEGER PRIMARY KEY);
CREATE TABLE Cours(nom TEXT, enseignantID INTEGER,coursID INTEGER PRIMARY KEY);
CREATE TABLE Validations(validationID INTEGER PRIMARY KEY,nom TEXT,jour DATE,coefficient INTEGER,note FLOAT,coursID INTEGER,étudiantID INTEGER);
CREATE TABLE Salle(nom TEXT,capacité INTEGER,salleID INTEGER PRIMARY KEY);
CREATE TABLE Séance(séanceID INTEGER PRIMARY KEY,salleID INTEGER,début TIMESTAMP,fin TIMESTAMP);
CREATE TABLE Crédits(créditsID INTEGER PRIMARY KEY,coursID INTEGER,parcoursID INTEGER,nbrECTS INTEGER);

-- PERSONNES

INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('smith','john','président',1);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('chu','pika','normalien',2);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('flex','ron','auditeur',3);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('hontas','poca',"professeur des universités",4);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('sparrow','jack',"professeur des universités",5);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('beckett','cutler',"maître de conférences",6);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('pan','peter',"thésard",7);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('phlosion','ty',"normalien",8);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('doran','ni',"auditeur",9);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('cool','tenta',"secrétaire",10);
INSERT INTO Personnes (nom,prénom,statut,téléphone) VALUES ('feu','draco',"professeur agrégé",0700407030);

-- ÉTUDIANTS

INSERT INTO Étudiants (cours,parcours,étudiantID) VALUES ("électronique",'M1-EEA',2);
INSERT INTO Étudiants (cours,parcours,étudiantID) VALUES ("optimisation",'M1-MATHÉMATIQUES',3);

-- PARCOURS

--INSERT INTO Parcours (nom,secrétaire,directeur) VALUES (M1-EEA,);
--INSERT INTO Parcours (nom,secrétaire,directeur) VALUES (M1-MATHÉMATIQUES,lili,titi);
