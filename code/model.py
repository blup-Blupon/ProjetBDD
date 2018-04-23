#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sqlite3


class Model:
    def __init__(self):
        self.connection = sqlite3.connect('univ.db')
        self.connection.text_factory = str
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if (self.connection):
            self.connection.close()

##############################################
######      Queries for tab  PERSONS    ######
##############################################

    # Create a new person
    def createPerson(self, lastname, firstname, address, phone):
        self.cursor.execute("""
        INSERT INTO Personnes (nom,prénom,adresse,téléphone) VALUES (?,?,?,?)
        """, (lastname, firstname, address, phone))
        self.connection.commit()

    # Return a list of (lastname, firstname, address, phone,
    # number of curriculums) corresponding to all persons
    def listPersons(self):
        self.cursor.execute(""" 
        SELECT personneID,nom,prénom,adresse,téléphone,nbrParcours FROM Personnes
        """)
        return self.cursor.fetchall()

    # Delete a person given by its ID (beware of the foreign constraints!)
    def deletePerson(self, idPerson):
        self.cursor.execute("""
        DELETE FROM Personnes WHERE personneID = ?
        """, [idPerson]) # rajout de crochets https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta#16856730
        self.connection.commit()
    # 1) problème car idPerson ne désigne pas à la fois un étudiant et une personne ?
    # 2) supprimer un parcours dont le directeur est supprimé ?
    # 3) potentiel problème de destruction propre lorsqu'on a une table dotée
    # de plusieurs foreign keys

##############################################
######     Queries for  CURRICULUMS     ######
##############################################

    # Create a curriculum
    # secretary et director seront des IDs (primary key integer) associées à des entrées
    # préexistantes de la table 
    def createCurriculum(self, name, secretaryID, directorID):
        self.cursor.execute("""
        INSERT INTO Parcours (nomParcours,secrétaireID,directeurID) VALUES (?,?,?)
        """, (name, secretaryID, directorID))
        self.connection.commit()

    # Delete a curriculum given by its ID (beware of the foreign constraints!)
    def deleteCurriculum(self, idCurriculum):
        self.cursor.execute("""
        DELETE FROM Parcours WHERE parcoursID = ?
        """, [idCurriculum])
        self.connection.commit()

    # List all curriculums and return a list
    # (id,name of curriculum,director lastname, director firstname,
    # secretary lastname, secretary firstname)
    def listCurriculums(self):
        self.cursor.execute(""" 
        SELECT 
            Parcours.parcoursID,
            Parcours.nomParcours,
            Perso1.nom,
            Perso1.prénom,
            Perso2.nom,
            Perso2.prénom
        FROM
            Parcours
        INNER JOIN Personnes AS Perso1 ON Parcours.secrétaireID = Perso1.personneID
        INNER JOIN Personnes AS Perso2 ON Parcours.directeurID = Perso2.personneID
        """)
        return self.cursor.fetchall()

##############################################
######     Queries for  COURSES         ######
##############################################

    # Create a course using the name of the course and the id of the
    # teacher of the course
    def createCourse(self, name, idProfessor):
        self.cursor.execute("""
        INSERT INTO Cours (nomCours,enseignantID) VALUES (?,?)
        """, (name, idProfessor))
        self.connection.commit()

    # Delete a given course (beware that the course might be registered to course
    # and have grades that should also be deleted)
    # commentaires avec typos ? a priori cours à supprimer avec crédits et validations associés
    def deleteCourse(self, idCourse):
        self.cursor.execute("""
        DELETE FROM Cours WHERE coursID = ?
        """, [idCourse])
        self.connection.commit()

    # Lists all the courses and return a list of
    # (course id, course name, teacher id,  teacher lastname, teacher firstname)
    def listCourses(self):
        self.cursor.execute(""" 
        SELECT
            Cours.coursID,
            Cours.nomCours,
            Cours.enseignantID,
            Personnes.nom,
            Personnes.prénom
        FROM
            Cours
        INNER JOIN Personnes ON Cours.enseignantID = Personnes.personneID
        """)
        return self.cursor.fetchall()

##############################################
######        Queries for  ROOMS        ######
##############################################

    # Create a new room
    def createRoom(self, name, capacity):
        self.cursor.execute("""
        INSERT INTO Salles (nomSalle,capacité) VALUES (?,?)
        """, (name, capacity))
        self.connection.commit()

    # Delete a room given by its ID (beware of the foreign constraints!)
    # foreign constraints -> supprimer les séances prévues dans la salle
    def deleteRoom(self, idRoom):
        self.cursor.execute("""
        DELETE FROM Salles WHERE salleID = ?
        """, [idRoom])
        self.connection.commit()

    # List rooms and return a list of (id, name, capacity)
    def listRooms(self):
        self.cursor.execute(""" 
        SELECT salleID, nomSalle, capacité FROM Salles
        """)
        return self.cursor.fetchall()

##############################################
######   Queries for tab  ROOM/<ID>     ######
##############################################

    # get the name of a Room given by its id
    def getNameOfRoom(self, id):
        self.cursor.execute(""" 
        SELECT nomSalle FROM Salles WHERE salleID = ?
        """, id)
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # Mark a time range (since, until) occupied in room idRoom
    # for idCourse
    def occupyRoom(self, idRoom, idCourse, since, until):
        self.cursor.execute("""
        INSERT INTO Séances (salleID,coursID,début,fin) VALUES (?,?,?,?)
        """, (idRoom, idCourse, since, until))
        self.connection.commit()

    # This function should return the occupation of a given room
    # ordered by start_date decreasing in the form
    # (start,end,course name)
    def listCoursesInRoom(self, idRoom):
        self.cursor.execute("""
        SELECT
            Séances.début,
            Séances.fin,
            Cours.nomCours
        FROM
            Séances
        INNER JOIN Cours ON Séances.coursID = Cours.coursID
        WHERE Séances.salleID = ?
        ORDER BY datetime(Séances.début)
        """, [idRoom])
        return self.cursor.fetchall()

##############################################
###### Queries for tab  CURRICULUM/<ID> ######
##############################################

    # Get the name of the curriculum given by its id
    def getNameOfCurriculum(self, id):
        self.cursor.execute(""" 
        SELECT nomParcours FROM Parcours WHERE parcoursID = ?
        """, id)
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # List the courses registered to a curriculum (given by its ID) it
    # should return a list (course ID, course name, course teacher
    # lastname and firstname, ECTS)
    def listCoursesOfCurriculum(self, idCurriculum):
        self.cursor.execute("""
        
        """, (idCurriculum))
        return self.cursor.fetchall()

    #  !! HARD !!
    # This function should return the students registered
    # in a given curriculum. The result is a list of:
    # (lastname, firstname, averageGrade) beware that students
    # might miss some exams or some course (in which case they
    # should have 0 despite not being registered).
    # The average has to be computed by course using the coefficient
    # of the validation then a course contribute to a cursus to the
    # pro-rata of ects
    def averageGradesOfStudentsInCurriculum(self, idCurriculum):
        self.cursor.execute("""
        TODO18
        """, idCurriculum)
        return self.cursor.fetchall()

    # Register a person (given by its ID) to a curriculum (given by its ID)
    def registerPersonToCurriculum(self, idPerson, idCurriculum):
        self.cursor.execute("""
        TODO19
        """, (idPerson, idCurriculum))
        self.connection.commit()

    # Register a course (given by its ID) to a curriculum  (by its ID)
    def registerCourseToCurriculum(self, idCourse, idCurriculum):
        self.cursor.execute("""
        TODO20
        """, (idCurriculum, idCourse))
        self.connection.commit()

    # Unregister a course (given by its ID) to a curriculum (by its ID)
    def deleteCourseFromCurriculum(self, idCourse, idCurriculum):
        self.cursor.execute("""
        TODO21
        """, (idCurriculum, idCourse))
        self.connection.commit()

##############################################
######   Queries for tab  COURSE/<ID>   ######
##############################################

    # Get the name of the course given by its id
    def getNameOfCourse(self, id):
        self.cursor.execute(""" 
        TODO22
        """, id)
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # Lists the curriculum in which a course is registered
    # and returns a list of (id, name, ECTS) for each curriculum
    def listCurriculumsOfCourse(self, idCourse):
        self.cursor.execute("""
        TODO23
        """, (idCourse))
        return self.cursor.fetchall()

    # Returns a list of (id, date, name, coefficent) for a validation
    def listValidationsOfCourse(self, idCourse):
        self.cursor.execute("""
        TODO24
        """, idCourse)
        return self.cursor.fetchall()

    # This function should return a list
    # (lastname,firstname, id)
    # for each student registered in a curriculum
    # with this course
    def listStudentsOfCourse(self, idCourse):
        self.cursor.execute("""
        TODO25
        """, idCourse)
        return self.cursor.fetchall()

    # Return a list (id, lastname, firstname) of persons that are
    # registered in a curriculum with the course
    def listStudentsOfCourse(self, idCourse):
        self.cursor.execute("""
        SELECT
            Personnes.personneID,
            Personnes.nom,
            Personnes.prénom
        FROM
            Cours
        INNER JOIN Étudiants ON Étudiants.coursID = Cours.coursID
        INNER JOIN Personnes ON Personnes.personneID = Étudiants.étudiantPersonneID
        WHERE
            Cours.coursID = ?
        """, [idCourse])
        return self.cursor.fetchall()

    # This function should return a list (id, date, curriculum name,
    # student lastname,student firstname , exam name, grade) for the
    # given student of exams taken sorted by date of the exam
    # decreasing
    # -------------------------------
    # "for the given course" plutôt non ?
    # sinon idCourse en entrée et firstname + lastname n'a pas trop de sens
    def listGradesOfCourse(self, idCourse):
        self.cursor.execute("""
        SELECT
            Validations.validationID,
            Validations.dateExamen,
            Parcours.nomParcours,
            Personnes.nom,
            Personnes.prénom,
            Validations.nomExamen,
            Notes.note
        FROM
            Cours
        INNER JOIN Validations ON Validations.coursID = Cours.coursID
        INNER JOIN Parcours ON Validations.parcoursID = Parcours.parcoursID
        INNER JOIN Notes ON Notes.validationID = Validations.validationID
        INNER JOIN Personnes ON Personnes.personneID = Notes.étudiantPersonneID
        WHERE
            Cours.coursID = ?
        """, idCourse)
        return self.cursor.fetchall()

    # Add an examination to a course with a name, a coefficient and the
    # id of the relevant course
    def addValidationToCourse(self, name, coef, idCourse):
        self.cursor.execute(""" 
        INSERT INTO Validations (nomExamen,coefficient,coursID) VALUES (?,?,?)
        """, (name, coef, idCourse))
        self.connection.commit()

    # Add a grade to a student
    def addGrade(self, idValidation, idStudent, grade):
        self.cursor.execute(""" 
        INSERT INTO Notes (validationID,étudiantPersonneID,note) VALUES (?,?,?)
        """, (idValidation, idStudent, grade))
        self.connection.commit()

##############################################
######       Queries for tab            ######
######      COURSE/<ID1>/<ID2           ######
###### corresponding to validations     ######
##############################################

   # This function should return a list
   # (grade, lastname, firstname)
    def listGradesOfValidation(self, idValidation):
        self.cursor.execute("""
        SELECT
            Notes.note,
            Personnes.nom,
            Personnes.prénom
        FROM
            Validations
        INNER JOIN Notes ON Notes.validationID = Validations.validationID
        INNER JOIN Personnes ON Personnes.personneID = Notes.étudiant
        WHERE
            Validations.validationID = ?
        """, [idValidation])
        return self.cursor.fetchall()

    # Get the complete name of the validation given by its id The
    # complete name of a validation with name "exam" of a course "BDD"
    # is "BDD - exam". You should therefore preppend the name of the
    # course
    def getNameOfValidation(self, id):
        self.cursor.execute(""" 
        TODO31
        """, id)
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

##############################################
######   Queries for tab  PERSON/<ID>   ######
##############################################

    # Get the name of the person given by its id
    def getNameOfPerson(self, id):
        self.cursor.execute(""" 
        SELECT nom FROM Personnes WHERE personneID = ? 
        """, [id])
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # This function should return a list
    # (id, date, curriculum name, course name, exam name, grade)
    # for the given student of exams taken
    # sorted by date of the exam decreasing
    def listValidationsOfStudent(self, idStudent):
        self.cursor.execute("""
        SELECT
            Validations.validationID,
            Validations.dateExamen,
            Parcours.nomParcours,
            Cours.nomCours,
            Validations.nomExamen,
            Notes.note
        FROM
            Étudiants
        INNER JOIN Notes ON Notes.étudiantPersonneID = Étudiants.étudiantPersonneID
        INNER JOIN Validations ON Validations.validationID = Notes.validationID
        INNER JOIN Parcours ON Parcours.parcoursID = Validations.parcoursID
        INNER JOIN Cours ON Cours.coursID = Validations.coursID
        WHERE
            Étudiants.étudiantID = ?
        """, [idStudent])
        return self.cursor.fetchall()

    # !!! HARD !!!
    # List the curriculum in which a student is registered and return a
    # list (curriculum name, grade) where grade is the average grade
    def listCurriculumsOfStudent(self, idStudent):
        self.cursor.execute("""
        TODO34
        """, idStudent)
        return self.cursor.fetchall()
