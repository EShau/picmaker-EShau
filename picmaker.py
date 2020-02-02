import math

def cot(theta):
    return 1 / math.tan(theta)

def in_heart(x, y):
    theta = math.atan2(y,x)
    r_calculated = math.sqrt(x**2 + y**2)
    if x == 0:
        return in_heart(x - 1, y) and in_heart(x + 1, y)
    if y == 0:
        return in_heart(x - 2, y - 1) and in_heart(x - 2, y + 1) and in_heart(x + 2, y - 1) and in_heart(x + 2, y + 1)
    r_actual = 150 * math.pow(abs(math.tan(theta)), abs(cot(theta)))
    return r_calculated <= r_actual

def draw():
    with open("picture.ppm", 'w+') as fileWriter:
        fileWriter.write("P3\n")
        fileWriter.write("500 500\n")
        fileWriter.write("255\n")
        for y in range(250, -250, -1):
            for x in range(-250, 250, 1):
                if in_heart(x, y):
                    if y == 0:
                        fileWriter.write("128 0 128")
                    elif y > 0:
                        fileWriter.write("255 0 0 ")
                    else:
                        fileWriter.write("0 0 255 ")
                else:
                    fileWriter.write("0 0 0 ")
            fileWriter.write("\n")

draw()
