def shop(product_name: str) -> None:
    with open("shopping_list.txt", "a") as file:
        file.write(f"\n{product_name}\n")

while True:
    
    pruduct = input("Mahsulot nomini kiriting: ")
    Input = input("Malumot kiritmoqchi bolsangiz 1 ni nosing, chiqmoqchi bolsangiz 0 ni kiriting: ")
    
    if Input == '1':
        shop(pruduct)
    elif Input == '0':
        shop(pruduct)
        break
    else:
        print("Bunday buyruq mavjud emas!")
        break

with open("shopping_list.txt", "r")as file:
    pruduct(file.read())