from shapes import Paper, Triangle, Rectangle, Oval

def main():
    paper = Paper()
    shapeList = []

    for i in range(100):
        shapeList.append(0)

    # Borders
    shapeList[0] = generateRectangle("black", 30, 10, 200, 100)
    shapeList[1] = generateRectangle("black", 30, 10, 180, 110)
    shapeList[2] = generateRectangle("black", 10, 10, 170, 120)
    shapeList[3] = generateRectangle("black", 10, 20, 160, 130)
    shapeList[4] = generateRectangle("black", 10, 30, 150, 150)
    shapeList[5] = generateRectangle("black", 10, 20, 160, 180)
    shapeList[6] = generateRectangle("black", 10, 10, 170, 200)
    shapeList[7] = generateRectangle("black", 10, 10, 180, 210)
    shapeList[8] = generateRectangle("black", 50, 10, 190, 220)
    shapeList[9] = generateRectangle("black", 10, 10, 240, 210)
    shapeList[10] = generateRectangle("black", 20, 10, 250, 200)
    shapeList[11] = generateRectangle("black", 10, 70, 260, 140)
    shapeList[12] = generateRectangle("black", 10, 10, 250, 130)
    shapeList[13] = generateRectangle("black", 10, 10, 240, 120)
    shapeList[14] = generateRectangle("black", 10, 10, 230, 110)
    shapeList[15] = generateRectangle("black", 20, 10, 130, 160)
    shapeList[16] = generateRectangle("black", 20, 10, 110, 170)
    shapeList[17] = generateRectangle("black", 10, 10, 100, 180)
    shapeList[18] = generateRectangle("black", 10, 30, 90, 190)
    shapeList[19] = generateRectangle("black", 10, 10, 100, 220)
    shapeList[20] = generateRectangle("black", 10, 10, 110, 230)
    shapeList[21] = generateRectangle("black", 10, 10, 120, 240)
    shapeList[22] = generateRectangle("black", 20, 10, 130, 250)
    shapeList[23] = generateRectangle("black", 10, 10, 140, 260)
    shapeList[24] = generateRectangle("black", 10, 10, 130, 270)
    shapeList[25] = generateRectangle("black", 10, 10, 120, 280)
    shapeList[26] = generateRectangle("black", 10, 10, 110, 290)
    shapeList[27] = generateRectangle("black", 20, 10, 90, 300)
    shapeList[28] = generateRectangle("black", 20, 10, 70, 310)
    shapeList[29] = generateRectangle("black", 10, 20, 60, 320)
    shapeList[30] = generateRectangle("black", 90, 10, 60, 330)
    shapeList[31] = generateRectangle("black", 10, 10, 140, 320)
    shapeList[32] = generateRectangle("black", 10, 10, 150, 310)
    shapeList[33] = generateRectangle("black", 10, 10, 160, 300)
    shapeList[34] = generateRectangle("black", 20, 10, 170, 290)
    shapeList[35] = generateRectangle("black", 10, 20, 190, 300)
    shapeList[36] = generateRectangle("black", 10, 20, 180, 320)
    shapeList[37] = generateRectangle("black", 90, 10, 180, 330)
    shapeList[38] = generateRectangle("black", 10, 10, 260, 320)
    shapeList[39] = generateRectangle("black", 30, 10, 230, 310)
    shapeList[40] = generateRectangle("black", 10, 20, 240, 290)
    shapeList[41] = generateRectangle("black", 10, 10, 230, 280)
    shapeList[42] = generateRectangle("black", 10, 30, 220, 250)
    shapeList[43] = generateRectangle("black", 10, 10, 230, 240)
    shapeList[44] = generateRectangle("black", 50, 10, 240, 230)
    shapeList[45] = generateRectangle("black", 10, 40, 290, 190)
    shapeList[46] = generateRectangle("black", 30, 10, 270, 190)
    shapeList[47] = generateRectangle("black", 40, 10, 300, 180)
    shapeList[48] = generateRectangle("black", 30, 10, 330, 190)
    shapeList[49] = generateRectangle("black", 10, 20, 360, 200)
    shapeList[50] = generateRectangle("black", 40, 10, 300, 230)
    shapeList[51] = generateRectangle("black", 30, 10, 330, 220)
    shapeList[52] = generateRectangle("black", 10, 40, 340, 190)
    shapeList[53] = generateRectangle("black", 10, 10, 150, 240)
    shapeList[54] = generateRectangle("black", 10, 20, 160, 220)
    shapeList[55] = generateRectangle("black", 10, 10, 150, 210)
    shapeList[56] = generateRectangle("black", 10, 10, 140, 200)
    shapeList[57] = generateRectangle("black", 10, 20, 130, 210)
    shapeList[58] = generateRectangle("black", 10, 10, 210, 120)
    shapeList[59] = generateRectangle("black", 40, 10, 220, 130)
    shapeList[60] = generateRectangle("black", 10, 20, 220, 130)
    shapeList[61] = generateRectangle("black", 20, 10, 230, 150)
    shapeList[62] = generateRectangle("black", 40, 10, 200, 200)
    shapeList[63] = generateRectangle("black", 20, 20, 210, 170)
    shapeList[64] = generateRectangle("black", 10, 20, 240, 170)
    
    # Thin lines
    shapeList[65] = generateRectangle("black", 0, 10, 190, 200)
    shapeList[66] = generateRectangle("black", 10, 0, 180, 200)
    shapeList[67] = generateRectangle("black", 0, 30, 180, 170)
    shapeList[68] = generateRectangle("black", 10, 0, 180, 170)
    shapeList[69] = generateRectangle("black", 0, 10, 190, 160)
    shapeList[70] = generateRectangle("black", 40, 0, 190, 160)
    shapeList[71] = generateRectangle("black", 0, 10, 230, 160)
    shapeList[72] = generateRectangle("black", 20, 0, 230, 170)
    shapeList[73] = generateRectangle("black", 0, 10, 250, 160)
    shapeList[74] = generateRectangle("black", 10, 0, 250, 160)
    shapeList[75] = generateRectangle("black", 0, 30, 170, 150)
    shapeList[76] = generateRectangle("white", 30, 10, 310, 200)
    shapeList[77] = generateRectangle("white", 10, 10, 350, 200)
    shapeList[78] = generateRectangle("white", 20, 10, 230, 140)

    # Diagonal "lines"
    shapeList[79] = generateTriangle("black", 90, 190, 120, 210, 135, 215)
    shapeList[80] = generateTriangle("black", 140, 270, 190, 278, 225, 275)
    shapeList[81] = generateTriangle("black", 120, 290, 130, 300, 152, 312)
    shapeList[82] = generateTriangle("black", 130, 280, 140, 290, 162, 302)
    shapeList[83] = generateTriangle("black", 192, 302, 207, 290, 222, 272)
    shapeList[84] = generateTriangle("black", 202, 312, 222, 304, 242, 292)

    # Ovals
    shapeList[85] = Oval()
    shapeList[85].randomize(smallest=20, largest=30)
    shapeList[85].set_x(400), shapeList[85].set_y(200)

    shapeList[86] = Oval()
    shapeList[86].randomize(smallest=20, largest=30)
    shapeList[86].set_x(500), shapeList[86].set_y(200)

    # Draws all shapes
    for i in range(len(shapeList)):
        if shapeList[i] != 0:
            shapeList[i].draw()

    paper.display()


def generateRectangle(color, width, height, coordX, coordY):
    rectangle = Rectangle()
    rectangle.set_color(color)
    rectangle.set_width(width)
    rectangle.set_height(height)
    rectangle.set_x(coordX)
    rectangle.set_y(coordY)
    return(rectangle)


def generateTriangle(color, x1, y1, x2, y2, x3, y3):
    triangle = Triangle(x1, y1, x2, y2, x3, y3)
    triangle.set_color(color)
    return(triangle)


if __name__ == "__main__":
    main()