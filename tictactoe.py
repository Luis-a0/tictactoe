lista = ["_","_","_","_","_","_","_","_","_"]

# Funcion para determinar si el caracter evaluado es ganador
def val_win(lista, val):
    if (lista[:3].count(val) == 3) or (lista[3:6].count(val) == 3) or (lista[6:].count(val) == 3):
        return True
    elif (lista[:7:3].count(val) == 3) or (lista[1:8:3].count(val) == 3) or (lista[2:9:3].count(val) == 3):
        return True
    elif (lista[2:7:2].count(val) == 3) or (lista[0:9:4].count(val) == 3):
        return True
    else:
        return False

# Funcion para mostrar el tablero de juego en su estado actual
def show_table():
    global lista
    print("""
    ---------
    | {} {} {} |
    | {} {} {} |
    | {} {} {} |
    ---------
    """.format(lista[0], lista[1], lista[2],
                lista[3], lista[4], lista[5],
                lista[6], lista[7], lista[8]))

# Mapeo de coodenadas desde formato de Matrix a Arreglo
pos_xy = lambda x , y : x * 3 + y
           
def enter_value(val):
    global lista
    aux = True
    while aux:
        try:
            pos = input("Enter the coordinates (values ​​separated by a space) : ")
            x, y = int(pos[0]), int(pos[2])
            if x > 3 or y > 3:
                print("Coordinates should be from 1 to 3!")
            else:
                if lista[pos_xy(x-1, y-1)] == "_":
                    lista[pos_xy(x-1, y-1)] = val
                    aux = False
                else:
                    print("This cell is occupied! Choose another one!")
        except ValueError:
            print("You should enter numbers!")

# Revision de Status del tablero
def rev_status():
    global lista
    x_win = False
    o_win = False
    x_win = val_win(lista, "X")
    o_win = val_win(lista, "O")
    count_ = lista.count("_")
    count_o = lista.count("O")
    count_x = lista.count("X")

    if x_win:
        print("X wins")
        return False
    elif o_win:
        print("O wins")
        return False
    elif (count_ == 0) and (not x_win and not o_win):
        print("Draw")
        return False
    else:
        return True

# Ejecutor del Juego
def tictactoe():
    status = True
    cont = 0
    show_table()
    while status:
        if cont %2 == 0:
            enter_value("X")
            cont += 1
        else:
            enter_value("O")
            cont += 1
        show_table()
        status = rev_status()

tictactoe()
