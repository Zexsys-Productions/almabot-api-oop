# importing external modules
from bs4 import BeautifulSoup
import lxml
import aiohttp
import asyncio

# importing all internal modules 
from subject import Subject

async def fetch(url, usr, pwd):

    payload = {
        "username": usr,
        "password": pwd
    }

    async with aiohttp.ClientSession() as session:
        await session.post('https://cbcs.getalma.com/login', data = payload)
        async with session.get(url) as response:
            return await response.text()

async def async_get_gpa(usr, pwd):

    grade_html, weight_html = await asyncio.gather(fetch('https://cbcs.getalma.com/home/schedule?view=list', usr, pwd), fetch('https://cbcs.getalma.com/home/schedule?view=split', usr, pwd))

    gradelistofsubjects = BeautifulSoup(grade_html, "lxml").tbody("tr")
    weightlistofsubjects = BeautifulSoup(weight_html, "lxml").find_all("div", class_="class-row nav-class")

    SubjectList = list()

    for eachSubject in gradelistofsubjects:
        currentSubject = list(eachSubject.a.stripped_strings)[0]
        gradeLetter = list(eachSubject.find(class_="grade snug").stripped_strings)[0]
        for eachWeightSubject in weightlistofsubjects:
            if ("Homeroom" not in currentSubject) and (eachWeightSubject.a.get_text() == currentSubject) and (gradeLetter != "-"):
                currentWeight = eachWeightSubject.find("span", class_="credit-hours charcoal").get_text().split(" ")[1]
                SubjectList.append(Subject(currentSubject, float(currentWeight), gradeLetter))

    gradepointaverage = (sum(everySubject.weightedGradePoint for everySubject in SubjectList)/sum(everySubject.weight for everySubject in SubjectList))
    return round(gradepointaverage, 2)