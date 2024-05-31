def get_coordinate(record):
    tesoro, coordenada = record
    return coordenada


def convert_coordinate(coordinate):
    num1= coordinate[0]
    num2= coordinate[1]
    return (num1,num2)


def create_record(azara, rui):
    treasure, coordinate1= azara
    location,coordinate2,quadrant = rui

    if coordinate1[0] != coordinate2[0] or coordinate1[1] != coordinate2[1]:
        return "not a match"

    return (treasure, coordinate1, location, coordinate2, quadrant)
