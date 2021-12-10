from prettytable import PrettyTable

def read_table(path):
    file = open(path, 'r', encoding = 'utf-8')
    data = file.read()
    file.close()
    
    arr = data.split('\n')
    for i in range(len(arr)):
        arr[i] = arr[i].split(',')
    
    return arr

def write_file(s, path):
    file = open(path, 'w', encoding = 'utf-8')
    file.write(s)
    file.close()

table1 = read_table('D:\Olena\Навчання\Комп. науки/table1.txt')
table2 = read_table('D:\Olena\Навчання\Комп. науки/table2.txt')

t1 = PrettyTable([
    'Код товарної групи',
    'План',
    'Очікуєме виконання',
    'Рік'
])
t1.add_rows(table1)

t2 = PrettyTable([
    'Код товарної групи',
    'Найменування товарної групи',
    'Торгова скидка, %'
])
t2.add_rows(table2)

print(t1)
print('\n')
print(t2)

table3 = []

for row1 in table1:
    for row2 in table2:
        if row1[0] == row2[0]:
            table3.append([row2[1], row1[3], row1[1], row1[2], row2[2]])

t3 = PrettyTable([
    'Найменування товарної групи',
    'Рік',
    'План',
    'Очікуєме виконання',
    'Торгова скидка, %'
])
t3.add_rows(table3)

write_file(t3.get_string(), 'D:\Olena\Навчання\Комп. науки/table3.txt')
write_file(str(table3).replace('\'', '\"'), 'D:\Olena\Навчання\Комп. науки/table3.json')
input()