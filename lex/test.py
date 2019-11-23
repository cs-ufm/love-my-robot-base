say = 'SAY TEXT'
test = ['SAY TEXT', 'DRIVE 90']
instructions = []
for i in test:
    instructions.append(i.split(' '))

for x in instructions:
    print(x[0], x[1])