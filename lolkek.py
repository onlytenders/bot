listik = [["Влад", 12],
              ["Рахат", 12],
              ["Ильяс", 9],
              ["Искандер", 10],
              ["Касым", 11],
              ["Арыстан", 9]]

def getStudentByNumber(a):
    try:
        return listik[a-1]
    except:
        return "Your number is incorrect"
    
def getStudentsList():
    return listik

def getMediumMarks():
    aver = 0
    for student in listik:
        aver += student[1]
    return aver / len(listik)

