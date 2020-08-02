# PROVIDE A FUNCTION
def draw_square(size):
    rows = 0
    while rows < size:
        print(" * "*size)
        rows += 1


def inputInt(message):
    # incercat cu float, ca sa fie acceptate si cifrele zecimale,
    # dupa convertite in int (int(input(message)))
    my_nr = float(input(message))
    return int(my_nr)

# CONSUME A FUNCTION
draw_square(inputInt("Size 1st sq: "))
draw_square(inputInt("Size 2nd sq: "))
