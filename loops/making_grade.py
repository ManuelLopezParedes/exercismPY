# redondeamos cada elemento de la lista
def round_scores(student_scores):
    lista = []
    for score in student_scores:
        lista.append(round(score))
    return lista

# regresamos el numero de estudiantes con un puntaje menor o igual a 40
def count_failed_students(student_scores):
    num = 0 
    for score in student_scores:
        if score <= 40:
            num += 1
    return num

# regresamos una lista donde el puntaje sea mayor o igual al limite
def above_threshold(student_scores, threshold):
    lista = []
    for score in student_scores:
        if score >= threshold:
            lista.append(score)
    return lista

# clasificamos el rango de calificaciones dependiendo de la nota mayor
def letter_grades(highest):
    var = (highest - 40) // 4
    var2 = 41
    lista = []
    for i in range(4):
        lista.append(var2)
        var2 += var
    return lista

def student_ranking(student_scores, student_names):
    lista = []
    for index, student in enumerate(student_names):
        lista.append(f"{index + 1}. {student}: {student_scores[index]}")
    return lista

def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []