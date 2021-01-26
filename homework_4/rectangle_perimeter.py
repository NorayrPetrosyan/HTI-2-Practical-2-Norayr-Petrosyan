def segment_length(x1, y1, x2, y2):
    d = (x2 - x1)**2 + (y2 - y1)**2
    root_of_d = d**(1/2)

    return root_of_d

def rectangle_perimeter(x1, y1, x2, y2 ,x3 ,y3 ,x4 ,y4):
    a = segment_length(x4, y4, x1, y1)
    b = segment_length(x1, y1, x2, y2)
    c = segment_length(x2, y2, x3, y3)
    d = segment_length(x3, y3, x4, y4)

    perimeter = a + b + c + d

    return perimeter

numbers = [float(i) for i in input("Enter corners' coordinates of a quadrangular: ").split()]
x1, y1, x2, y2, x3, y3, x4, y4 = numbers

print(rectangle_perimeter(x1, y1, x2, y2, x3, y3, x4, y4))