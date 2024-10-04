#1
f = 'note.txt'
with open(f) as file:
    for line in file:
        print(line, end='')

#2
print("\n\nLire les n premiers lignes")
f = 'note.txt'
n = 3  
file = open(f)
for i in range(n):
    line = next(file)
    print(line, end='')
file.close()

#3
print("\n\nLire les n derniers lignes")
file_path = 'note.txt'
n = 2 
lines = []
file = open(file_path)
for line in file:
    lines += [line]  
file.close()
for line in lines[-n:]:
    print(line, end='')

#4
print("\n\n Comptez le nombre de mots")
f = 'note.txt'
count = 0
with open(f) as file:
    for line in file:
        count += len(line.split())
print(f'Nombre de mots: {count}')

#5
print("\n\nLire les n derniers lignes")
file_path = 'note.txt'
n = 2 
lines = []
file = open(file_path)
for line in file:
    lines += [line]  
file.close()
for line in lines[-n:]:
    print(line, end='')