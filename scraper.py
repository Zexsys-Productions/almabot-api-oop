# importing external modules
import requests
from bs4 import BeautifulSoup
import lxml

# importing all internal modules 
from resources import rubric

# declaring class for Subject
class Subject:
    
    def __init__(self, name, weight, gradeLetter):
        
        self.name = name
        self.weight = weight
        self.gradeLetter = gradeLetter
        self.gradePoint = rubric.gradepointdictionary[gradeLetter]
        self.weightedGradePoint = self.gradePoint * weight
    
def sessionOf(username, password):

    payload = {
        "username": username,
        "password": password
    }

    loginurl = "https://cbcs.getalma.com/login"

    session = requests.Session()
    session.post(loginurl, data=payload)
    return session

def getgpa(username, password):

    # declaring necessary URLs
    gradeurl = "https://cbcs.getalma.com/home/schedule?view=list"
    weighturl = "https://cbcs.getalma.com/home/schedule?view=split"

    # declaring the current session as a variable
    currentSession = sessionOf(username, password)

    gradesoup = BeautifulSoup(currentSession.get(gradeurl).content, "lxml")
    gradelistofsubjects = gradesoup.tbody("tr")

    weightsoup = BeautifulSoup(currentSession.get(weighturl).content, "lxml")
    weightlistofsubjects = weightsoup.find_all("div", class_="class-row nav-class")

    SubjectList = list()

    for eachSubject in gradelistofsubjects:
        currentSubject = list(eachSubject.a.stripped_strings)[0]
        gradeLetter = list(eachSubject.find(class_="grade snug").stripped_strings)[0]
        for eachWeightSubject in weightlistofsubjects:
            if "Homeroom" not in currentSubject and eachWeightSubject.a.get_text() == currentSubject:
                currentWeight = eachWeightSubject.find("span", class_="credit-hours charcoal").get_text().split(" ")[1]
                SubjectList.append(Subject(currentSubject, float(currentWeight), gradeLetter))

    # closing the current session
    currentSession.close()

    gradepointaverage = (sum(everySubject.weightedGradePoint for everySubject in SubjectList)/sum(everySubject.weight for everySubject in SubjectList))
    return round(gradepointaverage, 2)

