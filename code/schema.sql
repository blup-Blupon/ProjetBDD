-- REMARQUES D'ORDRE GÉNÉRAL
-- utiliser des caractères comme le circonflexe dans des requêtes peut mener à des messages d'erreur louches...

-- ACTIVATION DES FOREIGN KEYS EN SQLITE 3

PRAGMA foreign_keys = ON;

-- CRÉATION DE LA BDD

CREATE TABLE Personnes(
        nom TEXT,
        prénom TEXT,
        statut TEXT,
        adresse TEXT,
        téléphone INTEGER,
        nbrParcours INTEGER, 
        personneID INTEGER PRIMARY KEY
);

-- cours et étudiant sont foreign key
-- la primary key est l'ensemble des attributs ici en fait
-- peut pas avoir foreign key as primary cf.:
-- https://stackoverflow.com/questions/10982992/is-it-fine-to-have-foreign-key-as-primary-key
CREATE TABLE Étudiants(
        coursID INTEGER,
        parcoursID INTEGER,
        étudiantID INTEGER PRIMARY KEY,
        étudiantPersonneID INTEGER,
        CONSTRAINT coursExiste
            FOREIGN KEY (coursID)
            REFERENCES Cours(coursID)
            ON DELETE CASCADE,
        CONSTRAINT personneExiste
            FOREIGN KEY (étudiantPersonneID)
            REFERENCES Personnes(personneID)
            ON DELETE CASCADE,
        CONSTRAINT parcoursExiste
            FOREIGN KEY (parcoursID)
            REFERENCES Parcours(parcoursID)
            ON DELETE CASCADE
);

CREATE TABLE Parcours(
        nomParcours TEXT,
        secrétaireID INTEGER,
        directeurID INTEGER,
        parcoursID INTEGER PRIMARY KEY
);

CREATE TABLE Cours(
        nomCours TEXT,
        enseignantID INTEGER,
        parcoursID INTEGER,
        coursID INTEGER PRIMARY KEY,
        CONSTRAINT avoirUnEnseignant
            FOREIGN KEY(enseignantID) 
            REFERENCES Personnes(personneID)
            ON DELETE CASCADE,
        CONSTRAINT avoirUnParcours
            FOREIGN KEY(parcoursID)
            REFERENCES Parcours(parcoursID)
            ON DELETE CASCADE
);

-- utiliser TEXT pour storer des dates en  ISO8601 string format
-- cf. http://www.sqlitetutorial.net/sqlite-date/
-- use %Y-%m-%d %H:%M format
CREATE TABLE Validations(
        validationID INTEGER PRIMARY KEY,
        nomExamen TEXT,
        dateExamen TEXT,
        coefficient INTEGER,
        nbrCrédits REAL,
        parcoursID INTEGER,
        coursID INTEGER,
        CONSTRAINT appartenanceParcours
            FOREIGN KEY (parcoursID)
            REFERENCES Parcours(parcoursID)
            ON DELETE CASCADE,
        CONSTRAINT avoirUnCours
            FOREIGN KEY(coursID)
            REFERENCES Cours(coursID)
            ON DELETE CASCADE
);

-- il faut une table notes avec étudiants à part car sinon on ne peut plus choisir une liste d'étudiants pour un seul validationID qui est une primary key

CREATE TABLE Notes(
        noteID INTEGER PRIMARY KEY,
        note FLOAT,
        validationID INTEGER,
        étudiantPersonneID INTEGER,
        CONSTRAINT avoirUnEtudiant
            FOREIGN KEY(étudiantPersonneID)
            REFERENCES Étudiants(étudiantPersonneID)
);

CREATE TABLE Salles(
        nomSalle TEXT,
        capacité INTEGER,
        salleID INTEGER PRIMARY KEY
);


-- utiliser TEXT pour storer des dates en  ISO8601 string format
-- cf. http://www.sqlitetutorial.net/sqlite-date/
-- use %Y-%m-%d %H:%M format
CREATE TABLE Séances(
        séanceID INTEGER PRIMARY KEY,
        salleID INTEGER,
        coursID INTEGER,
        début TEXT,
        fin TEXT,
        CONSTRAINT avoirUneSalle
            FOREIGN KEY(salleID)
            REFERENCES Salles(salleID)
            ON DELETE CASCADE,
        CONSTRAINT coursDeLaSeance
            FOREIGN KEY(coursID)
            REFERENCES Cours(coursID)
);

CREATE TABLE Crédits(
        créditsID INTEGER PRIMARY KEY,
        coursID INTEGER,
        parcoursID INTEGER,
        nbrECTS INTEGER,
        CONSTRAINT creditPourCours
            FOREIGN KEY(coursID)
            REFERENCES Cours(coursID)
            ON DELETE CASCADE,
        CONSTRAINT creditPourParcours
            FOREIGN KEY(parcoursID)
            REFERENCES Parcours(parcoursID)
            ON DELETE CASCADE
);

-- PERSONNES

INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('smith','john','président',1);

INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('chu',"pika",'normalien',2);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('flex','ron','normalien',3);

INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('hontas','poca',"professeur des universités",4);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('sparrow','jack',"professeur des universités",5);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('beckett','cutler',"maître de conférences",6);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('blake','francis',"professeur des universités",17);

INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('pan','peter',"thésard",7);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('phlosion','ty',"normalien",8);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('doran','ni',"auditeur",9);

INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('cool','tenta',"secrétaire",10);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('puce','cara','secrétaire',11);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('bee','bumble','secrétaire',12);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('wave','sound','secrétaire',15);
INSERT INTO Personnes (nom,prénom,statut,personneID) VALUES ('tron','mega','secrétaire',16);

INSERT INTO Personnes (nom,prénom,statut,personneID,téléphone) VALUES ('feu','draco',"professeur agrégé",13,700407030);
INSERT INTO Personnes (nom,prénom,statut,personneID,téléphone) VALUES ('prime','optimus',"chargé de recherche",14,701417131);

-- il faut tester l'auto incrémentation des ID, nécessaire dans les créations de model.py

INSERT INTO Personnes (nom,prénom,statut,téléphone,adresse) VALUES ('man','iron',"infirmière",112,"23 Pavillon rose");
INSERT INTO Personnes (nom,prénom,téléphone,adresse) VALUES ('vaillante','colombe',750213324,"303 Pavillon bleu");

-- ÉTUDIANTS

INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (1,1,2);
INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (6,1,2);
INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (7,1,2);

INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (2,2,3);
INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (8,2,3);

INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (3,3,7);
INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (9,3,7);

INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (4,4,8);
INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (10,4,8);

INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (5,5,9);
INSERT INTO Étudiants (coursID,parcoursID,étudiantPersonneID) VALUES (11,5,9);

-- PARCOURS

INSERT INTO Parcours (nomParcours,secrétaireID,directeurID,parcoursID) VALUES ('M1-EEA',10,4,1);
INSERT INTO Parcours (nomParcours,secrétaireID,directeurID,parcoursID) VALUES ('M1-MATHEMATIQUES',11,5,2);
INSERT INTO Parcours (nomParcours,secrétaireID,directeurID,parcoursID) VALUES ('DOCTORAT',12,14,3);
INSERT INTO Parcours (nomParcours,secrétaireID,directeurID,parcoursID) VALUES ('M2-ECONOMIE',15,6,4);
INSERT INTO Parcours (nomParcours,secrétaireID,directeurID,parcoursID) VALUES ('L3-INFORMATIQUE',16,17,5);

-- COURS

INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("electronique",4,1);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("optimisation",5,2);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("gestion de projet",14,3);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("econometrie",6,4);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("algorithmique",17,5);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("electrotechnique",4,6);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("automatique",4,7);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("arithmetique",17,8);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("pedagogie",14,9);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("gestion",6,10);
INSERT INTO Cours (nomCours,enseignantID,coursID) VALUES ("reseaux",17,11);

-- SALLES

INSERT INTO Salles (nomSalle,capacité,salleID) VALUES ("Amphitheatre Jadielle",100,1);
INSERT INTO Salles (nomSalle,capacité,salleID) VALUES ("Amphitheatre Rivamar",150,2);
INSERT INTO Salles (nomSalle,capacité,salleID) VALUES ("Laboratoire Vestigion",30,3);

-- SÉANCES

-- plusieurs séances dans un même salle en désordre de début, pour vérifier l'affichage ORDER BY de listCoursesInRoom
-- d'après forms.py on veut un format datetime %Y-%m-%d %H:%M, ce qui ne perturbe pas notre ORDER BY
INSERT INTO Séances (séanceID,salleID,coursID,début,fin) VALUES (4,1,1,"2018-05-02 14:00","2018-05-02 18:00");
INSERT INTO Séances (séanceID,salleID,coursID,début,fin) VALUES (1,1,1,"2018-05-02 08:00","2018-05-02 12:00");
INSERT INTO Séances (séanceID,salleID,coursID,début,fin) VALUES (2,2,2,"2018-05-02 08:00","2018-05-02 12:00");
INSERT INTO Séances (séanceID,salleID,coursID,début,fin) VALUES (3,1,1,"2018-04-27 08:00","2018-04-27 12:00");
