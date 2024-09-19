# PRODUCTO

# id: int
# name: str
# price:float
# section:int 

# 1. techt
# 2 clothes
# 3 food

store[]

id = int(input("ingrese el id de su producto"))
name =input("porfavor ingrese el nombre de su producto")
price = float(input("porfavor ingrese el valor de su producto"))
section = input("porfavor ingrese la secion para su produccion ")

product1 = {
    "id": id,
    "name": name,
    "price": price,
    "section":section

}


store.append(product1)

#mostrar los productos del almacen

for product in store :
    print(product)