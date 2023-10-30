# importing external modules
import requests
from bs4 import BeautifulSoup
import lxml

# importing all internal modules 
import credentials
from resources import rubric

# declaring class for Subject
class Subject:
    def __init__(
        self, 
        # name, 
        # code, 
        grade, 
        weight
        ):

        # self.name = name
        # self.code = code
        self.grade = grade
        self.weight = weight
        self.weightedGrade = weight * grade

SubjectList = list()
# bi
SubjectList.append(Subject(4, .5))
# chem
SubjectList.append(Subject(4, 1))
# history
SubjectList.append(Subject(4, .5))
# elective
SubjectList.append(Subject(4, .5))
# la
SubjectList.append(Subject(4, .5))
# pe
SubjectList.append(Subject(2.7, .5))
# bible
SubjectList.append(Subject(4, .5))
# ppkn
SubjectList.append(Subject(4, .5))
# physics
SubjectList.append(Subject(4, 1))
# math
SubjectList.append(Subject(3, 1))
# rhetoric
SubjectList.append(Subject(4, 1))

gpa = (sum(eachSubject.weightedGrade for eachSubject in SubjectList)/sum(eachSubject.weight for eachSubject in SubjectList))
print(gpa)
