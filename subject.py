from resources import rubric

# declaring class for Subject
class Subject:
    def __init__(self, name, weight, gradeLetter):
        self.name = name
        self.weight = weight
        self.gradeLetter = gradeLetter
        self.gradePoint = rubric.gradepointdictionary[gradeLetter]
        self.weightedGradePoint = self.gradePoint * weight