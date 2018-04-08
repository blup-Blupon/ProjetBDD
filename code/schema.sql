-- CRÉATION DE LA BDD

CREATE TABLE Personnes(nom TEXT,prénom TEXT,statut TEXT,adresse TEXT,téléphone INTEGER,personneID NOT NULL INTEGER PRIMARY KEY);
CREATE TABLE Étudiants(cours TEXT,parcours TEXT,étudiantID NOT NULL INTEGER PRIMARY KEY);
CREATE TABLE Parcours(nom TEXT,secrétaire TEXT,directeur TEXT,parcoursID NOT NULL INTEGER PRIMARY KEY);
CREATE TABLE Cours(nom TEXT, enseignantID NOT NULL INTEGER,coursID NOT NULL INTEGER PRIMARY KEY);
CREATE TABLE Validations(validationID NOT NULL INTEGER PRIMARY KEY,nom TEXT,jour DATE,coefficient NOT NULL INTEGER,note FLOAT,coursID NOT NULL INTEGER,étudiantID NOT NULL INTEGER);
CREATE TABLE Salle(nom TEXT,capacité NOT NULL INTEGER,salleID NOT NULL INTEGER PRIMARY KEY);
CREATE TABLE Séance(séanceID NOT NULL INTEGER PRIMARY KEY,salleID NOT NULL INTEGER,début TIMESTAMP,fin TIMESTAMP);
CREATE TABLE Crédits(créditsID NOT NULL INTEGER PRIMARY KEY,coursID NOT NULL INTEGER,parcoursID NOT NULL INTEGER,nbrECTS NOT NULL INTEGER);

-- PERSONNES

INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (smith,john,président,1);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (chu,pika,normalien,2);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (flex,ron,auditeur,3);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (hontas,poca,professeur des universités,4);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (sparrow,jack,professeur des universités,5);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (beckett,cutler,maître de conférences,6);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (pan,peter,thésard,7);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (phlosion,ty,normalien,8);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (doran,ni,auditeur,9);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES (cool,tenta,secrétaire,10);
INSERT INTO Personnes (nom,prénom,statut,téléphone) VALUES (feu,draco,prag,0700407030);

-- ÉTUDIANTS

INSERT INTO Étudiants (cours,parcours,étudiantID) VALUES (électronique,M1-EEA,2);
INSERT INTO Étudiants (cours,parcours,étudiantID) VALUES (optimisation,M1-MATHÉMATIQUES,3);

-- PARCOURS

INSERT INTO Parcours (nom,secrétaire,directeur) VALUES (M1-EEA,lulu,toto);
INSERT INTO Parcours (nom,secrétaire,directeur) VALUES (M1-MATHÉMATIQUES,lili,titi);
