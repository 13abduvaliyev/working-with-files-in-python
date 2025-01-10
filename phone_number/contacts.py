def func(name: str, phone: str) ->None:
    with open("contacts.txt", "a") as file:
        file.write(f"\n{name}:{phone}\n")
        
while True:
    name = input("Ism kiriting:")
    phone_number = input("Tel nomer kiriting: ")

    Input = input("Malumot kiritmoqchi bolsangiz 1 ni nosing, chiqmoqchi bolsangiz 0 ni kiriting: ")
    
    if Input == '1':
        func(name, phone_number)
    elif Input == '0':
        func(name, phone_number)
        break
    else:
        print("Bunday buyruq mavjud emas!")
        break

with open("contacts.txt", "r") as file:
    print(file.read())