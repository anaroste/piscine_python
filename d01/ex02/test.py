from vector import Vector

v1 = Vector([[4.0], [4.0], [4.0], [4.0]])
v2 = Vector([[4.0], [4.0], [4.0], [4.0]])
# v1 = Vector([[4.0, 4.0, 4.0, 4.0]])
# v2 = Vector([[4.0, 4.0, 4.0, 4.0]])

# print(v1)

# print(v2)
print(Vector([1. , 2e-3, 3.14, 5.]).values)
print(Vector(4).values)
# Vector(-1)
print(Vector((10, 12)).values)
# print(Vector((3, 1)).values)
# print(Vector((1, 1)).values)
# Vector((4, 7.1))
print('-----------------------------')
print('operator *')
print(v1 * 4)
print(4 * v1)
v1 * 'hi'
print('-----------------------------')
print('operator +')
v = Vector(4)
v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
print((v + v2).values)
v + Vector([0.0, 0.0, 0.0, 0.0])
v + "hello"
v + None
print('-----------------------------')
print('operator -')
print((v - v2).values, (v2 - v).values)
print('-----------------------------')
print('operator /')
print(v1 / 2)
print(v1 / 3.14)
try:
    v1 / 0
except ValueError:
    print('div par 0 good')
v1 / None
3 / Vector(3)
print('-----------------------------')
print('operation dot')
print(v1.dot(v2))
print([[16.0], [16.0], [16.0], [16.0]])
print('-----------------------------')
print('operation T')
v1.T()
print(v1.shape)
print((4, 1))
print('-----------------------------')
