with open("grades.txt", "w") as file:
    while True:
        name = input("Talabaning ismini kiriting : ")
        try:
            grade = float(input(f"{name}ning bahosini kiriting: "))
        except ValueError:
            print("Iltimos, to'g'ri baho kiriting!")
            continue
        
        file.write(f"{name}: {grade}\n")


with open("grades.txt", "r") as file:
    grades = []
    for line in file:
        print(line.strip())
        _, grade = line.split(": ")
        grades.append(float(grade))
    
    if grades:
        average = sum(grades) / len(grades)
        print(f"\nO'rtacha baho:\n({'+'.join(map(str, grades))}) / {len(grades)} = {average:.2f}")
    else:
        print("Fayl bosh!")

