import math

def paint_calc(height, width, cover):
    number_of_cans = (height*width)/cover
    return (math.ceil(number_of_cans))

test_h = int(input("Height of wall (m)")) # Height of wall (m)
test_w = int(input("Width of wall (m)")) # Width of wall (m)
cover = 5
#paint_calc(height=test_h, width=test_w, cover=5)
print(f"You'll need {paint_calc(height=test_h, width=test_w, cover=5)} cans of paint")