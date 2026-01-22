marks=85
optional=30
if marks>=90:
    grade='A'
elif marks>=80:
    grade='B'
elif marks>=70:
    grade='C'
else:
    grade='D'
print("The grade is:",grade) 


if marks>=90:
    if optional>=25:
        grade='A+'
    else:
        grade='A'
elif marks>=80:
    grade='B'
elif marks>=70:
    grade='C'
else:
    grade='D'
print("The grade is:",grade)


day="vai"

match day:
    case "sai":
        print("Monday")
    case "asd":
        print("Tuesday")
    case "vai":
        print("Wednesday")
    case _:
        print("Invalid day")