class Bangles:
    material = "Glass"

    def __init__(self, s, c, p):
        self.size = s
        self.color = c
        self.price = p


b1 = Bangles("Medium", "Red", "100rs")
b2 = Bangles("Small", "Green", "150rs")

print(b1.material)
print(b1.size)
print(b1.color)
print(b1.price)

print(b2.material)
print(b2.size)
print(b2.color)
print(b2.price)

class Lipstick:
    Brand = "Swiss Beauty"

    def __init__(self, c, p, q):
        self.color = c
        self.price = p
        self.quality = q


l1 = Lipstick("Wine", "500rs", "Good")
l2 = Lipstick("Pink", "300rs", "Good")

print(l1.Brand)
print(l1.color)
print(l1.price)
print(l1.quality)

print(l2.Brand)
print(l2.color)
print(l2.price)
print(l2.quality)

class WaterBottle:
    brand = "Milton"

    def __init__(self, c, cap, m, p, w, s):
        self.color = c
        self.capacity = cap
        self.material = m
        self.price = p
        self.weight = w
        self.shape = s


w1 = WaterBottle("Blue", "2L", "Plastic", "250rs", "200g", "Cylindrical")
w2 = WaterBottle("Red", "1L", "Steel", "300rs", "250g", "Round")

print(w1.brand)
print(w1.color)
print(w1.capacity)
print(w1.material)
print(w1.price)
print(w1.weight)
print(w1.shape)

print(w2.brand)
print(w2.color)
print(w2.capacity)
print(w2.material)
print(w2.price)
print(w2.weight)
print(w2.shape)

class StudyTable:
    brand = "Godrej"

    def __init__(self, c, m, l, w, h, p, d):
        self.color = c
        self.material = m
        self.length = l
        self.width = w
        self.height = h
        self.price = p
        self.drawers = d


s1 = StudyTable("Brown", "Wood", "120cm", "60cm", "75cm", "2000rs", 2)
s2 = StudyTable("White", "Wood", "100cm", "50cm", "70cm", "2500rs", 3)

print(s1.brand)
print(s1.color)
print(s1.material)
print(s1.length)
print(s1.width)
print(s1.height)
print(s1.price)
print(s1.drawers)

print(s2.brand)
print(s2.color)
print(s2.material)
print(s2.length)
print(s2.width)
print(s2.height)
print(s2.price)
print(s2.drawers)

class Laptop:
    company = "Lenovo"

    def __init__(self, c, r):
        self.color = c
        self.RAM = r


l1 = Laptop("Black", "8GB")
l2 = Laptop("Silver", "16GB")

print(l1.company)
print(l1.color)
print(l1.RAM)

print(l2.company)
print(l2.color)
print(l2.RAM)