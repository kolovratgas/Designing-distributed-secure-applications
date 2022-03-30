#Кол-во бит, используемых для генерации идентификаторов
M_intM = 4
#Идентификаторы позиций, в которых находятся узлы
m_arPos = [0, 1, 2]

from ChordNode import ChordArray

#Задаем начальное состояние сети
ChordArray_1 = ChordArray(M_intM, m_arPos)
ChordArray_1.initial_massiv()

#Отображение начального состояния
j = 0
print('Изначальные узлы ', str(m_arPos))
print('')
for i in ChordArray_1.myArray:
    print('Таблица finger для узла с id', str(m_arPos[j]))
    for k in i.finger:
        print('start: ' + str(k.start[0]) + '; interval: [' + str(k.interval[0]) + str(k.interval[1]) + '); node: ' + str(k.node[0]))
    j += 1

#Проверка функции поиска узла
id = 5
id_0 = 1
print(' ')
print('Выводим узел с id' + str(id))
print('Сейчас находимся на узле' + str(m_arPos[id_0]))
r_0 = ChordArray_1.closest_preceding_finger(m_arPos, id_0, id)
print('Результат функции closest_preceding_finger:', str(r_0))
r_1 = ChordArray_1.find_predecessor(m_arPos, id_0, id)
print('Результат функции find_predecessor: ', str(r_1.finger[2].interval[1]))
r_2 = ChordArray_1.find_successor(m_arPos, id_0, id)
print('Результат функции find_successor', str(r_2))
print(' ')

new_id = 6
print('Добавление нового узла: ', str(new_id))
ChordArray_1.join(new_id)

print(' ')
print('Отображение состояния после добавления узла')
j=0
for i in ChordArray_1.myArray:
    print('Таблица finger для узла с id', str(m_arPos[j]))
    for k in i.finger:
        print('start: ' + str(k.start[0]) + '; interval: [' + str(k.interval[0]) + ','
              + str(k.interval[1]) + '); node: ' + str(k.node[0]))
    j += 1

del_id = 3
print(' ')
print('3. Удаление узла с id ', str(del_id))
ChordArray_1.remove_node(del_id)
print(' ')
print('Отображение состояния после удаления узла')
j=0
for i in ChordArray_1.myArray:
    print('Таблица finger для узла с id', str(m_arPos[j]))
    for k in i.finger:
        print('start: ' + str(k.start[0]) + '; interval: [' + str(k.interval[0]) + ','
              + str(k.interval[1]) + '); node: ' + str(k.node[0]))
    j += 1

g = 0