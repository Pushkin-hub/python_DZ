list_names = ['Alex', 'Bob', 'Samuel', 'Sam']
list_names.sort()
print(list_names)

replaced_name = input('Какое имя вы хотите заменить?\n')
name = input('На какое имя вы хотите заменить?\n')

if replaced_name in list_names:
    index = list_names.index(replaced_name)
    list_names[index] = name 
else:
    print("Такого имени нет в списке.")

print(list_names)

adult = []
nonadult = []

while len(adult) < 5 and len(nonadult) < 5:
    name = input('Input name: ')
    age = int(input('Input age: '))
    if age > 18:
        adult.append([name, age])
    else:
        nonadult.append([name, age])

adult.sort(key=lambda x: x[1])
nonadult.sort(key=lambda x: x[1])

print('Взрослые:', adult)
print('Несовершеннолетние:', nonadult)