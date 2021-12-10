from prettytable import PrettyTable

def reading(path):
    file = open(path, 'r', encoding = 'utf-8')
    data = file.read()
    file.close()
    
    arr = data.split('\n')
    for i in range(len(arr)):
        arr[i] = arr[i].split(',')
    
    return arr

def writing(s, path):
    file = open(path, 'w', encoding = 'utf-8')
    file.write(s)
    file.close()

table1 = reading('D:\Olena\Навчання\Комп. науки\Project/table1.txt')
table2 = reading('D:\Olena\Навчання\Комп. науки\Project/table2.txt')

part1 = PrettyTable([
    'Код товарної групи',
    'План',
    'Очікуєме виконання',
    'Рік'
])
part1.add_rows(table1)

part2 = PrettyTable([
    'Код товарної групи',
    'Найменування товарної групи',
    'Торгова скидка, %'
])
part2.add_rows(table2)

print(part1)
print('\n')
print(part2)

table3 = []

for row1 in table1:
    for row2 in table2:
        if row1[0] == row2[0]:
            table3.append([row2[1], row1[3], row1[1], row1[2], row2[2]])

part3 = PrettyTable([
    'Найменування товарної групи',
    'Рік',
    'План',
    'Очікуєме виконання',
    'Торгова скидка, %'
])
part3.add_rows(table3)

writing(part3.get_string(), 'D:\Olena\Навчання\Комп. науки\Project/table3.txt')
writing(str(table3).replace('\'', '\"'), 'D:\Olena\Навчання\Комп. науки\Project/table3.json')
input()
