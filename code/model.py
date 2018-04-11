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
        INSERT INTO Personnes (nom,prénom,adresse,téléphone) VALUES
        """, (lastname, firstname, address, phone))
        self.connection.commit()

    # Return a list of (lastname, firstname, address, phone,
    # number of curriculums) corresponding to all persons
    def listPersons(self):
        self.cursor.execute(""" 
        TODO2
        """)
        return self.cursor.fetchall()

    # Delete a person given by its ID (beware of the foreign constraints!)
    def deletePerson(self, idPerson):
        self.cursor.execute("""
        TODO3
        """, idPerson)
        self.connection.commit()

##############################################
######     Queries for  CURRICULUMS     ######
##############################################

    # Create a curriculum
    def createCurriculum(self, name, secretary, director):
        self.cursor.execute("""
        TODO4
        """, (name, secretary, director))
        self.connection.commit()

    # Delete a curriculum given by its ID (beware of the foreign constraints!)
    def deleteCurriculum(self, idCurriculum):
        self.cursor.execute("""
        TODO5
        """, idCurriculum)
        self.connection.commit()

    # List all curriculums and return a list
    # (id,name of curriculum,director lastname, director firstname,
    # secretary lastname, secretary firstname)
    def listCurriculums(self):
        self.cursor.execute(""" 
        TODO6
        """)
        return self.cursor.fetchall()

##############################################
######     Queries for  COURSES         ######
##############################################

    # Create a course using the name of the course and the id of the
    # teacher of the course
    def createCourse(self, name, idProfessor):
        self.cursor.execute("""
        TODO7
        """, (name, idProfessor))
        self.connection.commit()

    # Delete a given course (beware that the course might be registered to course
    # and have grades that should also be deleted)
    def deleteCourse(self, idCourse):
        self.cursor.execute("""
        TODO8
        """, idCourse)
        self.connection.commit()

    # Lists all the courses and return a list of
    # (course id, course name, teacher id,  teacher lastname, teacher firstname)
    def listCourses(self):
        self.cursor.execute(""" 
        TODO9
        """)
        return self.cursor.fetchall()

##############################################
######        Queries for  ROOMS        ######
##############################################

    # Create a new room
    def createRoom(self, name, capacity):
        self.cursor.execute("""
        TODO10
        """, (name, capacity))
        self.connection.commit()

    # Delete a room given by its ID (beware of the foreign constraints!)
    def deleteRoom(self, idRoom):
        self.cursor.execute("""
        TODO11
        """, idRoom)
        self.connection.commit()

    # List rooms and return a list of (id, name, capacity)
    def listRooms(self):
        self.cursor.execute(""" 
        TODO12
        """)
        return self.cursor.fetchall()

##############################################
######   Queries for tab  ROOM/<ID>     ######
##############################################

    # get the name of a Room given by its id
    def getNameOfRoom(self, id):
        self.cursor.execute(""" 
        TODO13
        """, id)
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # Mark a time range (since, until) occupied in room idRoom
    # for idCourse
    def occupyRoom(self, idRoom, idCourse, since, until):
        self.cursor.execute("""
        TODO14
        """, (idRoom, idCourse, since, until))
        self.connection.commit()

    # This function should return the occupation of a given room
    # ordered by start_date decreasing in the form
    # (start,end,course name)
    def listCoursesInRoom(self, idRoom):
        self.cursor.execute("""
        TODO15
        """, idRoom)
        return self.cursor.fetchall()

##############################################
###### Queries for tab  CURRICULUM/<ID> ######
##############################################

    # Get the name of the curriculum given by its id
    def getNameOfCurriculum(self, id):
        self.cursor.execute(""" 
        TODO16
        """, id)
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # List the courses registered to a curriculum (given by its ID) it
    # should return a list (course ID, course name, course teacher
    # lastname and firstname, ECTS)
    def listCoursesOfCurriculum(self, idCurriculum):
        self.cursor.execute("""
        TODO17
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
        TODO26
        """, idCourse)
        return self.cursor.fetchall()

    # This function should return a list (id, date, curriculum name,
    # student lastname,student firstname , exam name, grade) for the
    # given student of exams taken sorted by date of the exam
    # decreasing
    def listGradesOfCourse(self, idCourse):
        self.cursor.execute("""
        TODO27
        """, idCourse)
        return self.cursor.fetchall()

    # Add an examination to a course with a name, a coefficient and the
    # id of the relevant course
    def addValidationToCourse(self, name, coef, idCourse):
        self.cursor.execute(""" 
        TODO28
        """, (name, coef, idCourse))
        self.connection.commit()

    # Add a grade to a student
    def addGrade(self, idValidation, idStudent, grade):
        self.cursor.execute(""" 
        TODO29
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
        TODO30
        """, idValidation)
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
        TODO32
        """, id)
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # This function should return a list
    # (id, date, curriculum name, course name, exam name, grade)
    # for the given student of exams taken
    # sorted by date of the exam decreasing
    def listValidationsOfStudent(self, idStudent):
        self.cursor.execute("""
        TODO33
        """, idStudent)
        return self.cursor.fetchall()

    # !!! HARD !!!
    # List the curriculum in which a student is registered and return a
    # list (curriculum name, grade) where grade is the average grade
    def listCurriculumsOfStudent(self, idStudent):
        self.cursor.execute("""
        TODO34
        """, idStudent)
        return self.cursor.fetchall()
