cubes = []
for cube in range(1, 11):
    print(cube ** 3)
    cubes.append(cube **3)
print(cubes)

# List comprehension

new_cubes = [ i**3 for i in range(1,11)]
print(new_cubes)
