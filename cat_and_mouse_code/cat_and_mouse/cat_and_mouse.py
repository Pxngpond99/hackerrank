def catAndMouse(x, y, z):
    dis_a = abs(x-z)
    dis_b = abs(y-z)
    if dis_a < dis_b :
        return "Cat A"
    elif dis_a > dis_b :
        return "Cat B"
    elif dis_a == dis_b :
        return "Mouse C"