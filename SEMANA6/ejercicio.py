while True:
    number_1 = input("ingrese un  un numeron\n")
    number_2 = input("ingrese un  un numeron\n")


    #para cuararse e salud es mejor poner esto

    try:
       result = int(number_1)/int(number_2)
       print(f"El resultado es . {result}")

    except Exception as e:
        print(f"se produjo un error de tipo{e}")
        

# tips para evitar que el programa se rompa y mejor envie un error 
   # try:
    #   result = int(number_1)/int(number_2)
     #  print(f"El resultado es . {result}")
    #except ValueError:
       # print("ERROR: porfavor ingrese tipos de datos numericos")
    #except ZeroDivisionError:
     #   print("INDERTERMINADO")    

