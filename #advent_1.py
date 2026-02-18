file = open('#list_1.txt')
input = []

for i in file:
	input.append(i.strip('\n'))

print(input)
direction  = []
distances = []
for i in input:
    print(i)
    direction.append(i[0])
    distances.append(i[1:])

location = 50
count = 0

for index in range(len(direction)):
    if direction[index] == 'R':
        location = location + int(distances[index])
        location = location % 100
        if location == 0:
            count += 1
    else:
        location = location - int(distances[index])
        location = location % 100
        if location == 0:
            count += 1


print(count)
