while True:
    user = input("\nIngrese su numbre de Usario: ")
    login = input("\nIngrese una Contraseña: ")
    pass1 = len(user)
    pass2 = len(login)
    if 8 <= pass1 and 16 >= pass1 and 8 <= pass2 and 16 >= pass2:
        print("\n\t.:Bienvenido:.")
        break
    else:
        print("\n\tSu nombre de usuario y contraseña tiene que tener al menos 8 a 16 caracteres.")
    
'''AQUI YA PUEDES HACER LO QUE NECESITES EL LOGIN COMO TAL YA ESTA GUARDADO ☂️'''