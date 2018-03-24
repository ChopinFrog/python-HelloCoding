# 딕셔너리를 리턴하는 함수를 선언합니다.
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

# 학생을 처리하는 함수를 선언합니다.
def student_get_sum(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )
    


# 학생 리스트를 선언합니다.
students = [
    create_student("가", 10, 10, 10, 10),
    create_student("나", 10, 10, 10, 10),
    create_student("다", 10, 10, 10, 10),
    create_student("라", 10, 10, 10, 10),
    create_student("마", 10, 10, 10, 10),
    create_student("바", 10, 10, 10, 10),
    create_student("사", 10, 10, 10, 10),
    create_student("아", 10, 10, 10, 10),
    create_student("자", 10, 10, 10, 10),
    create_student("차", 10, 10, 10, 10)
]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))