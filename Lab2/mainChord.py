from ChordNode import ChordArray

# Кол-во бит, используемых для генерации идентификаторов
M_intM = int(input("Введите кол-во бит для генерации идентификаторов: "))  # 4

# Идентификаторы позиций, в которых находятся узлы
m_arPos = [
    int(m)
    for m in input("Введите идентификатора позиций, в которых находятся узлы: ").split()
]  # [0, 1, 3]

# Удаление узла с id
del_id = int(input("Введите номер узла для удаления: "))  # 3

# Добавление нового узла
new_id = int(input("Введите номер узла для добавления: "))  # 6

# Значения для функция поиска узла
id = int(input("Введите номер узла для поиска: "))  # 5
id_0 = int(input("Введите номер узла, с которого будет производится поиск: "))  # 1

# Задаем начальное состояние сети
ChordArray_1 = ChordArray(M_intM, m_arPos)
ChordArray_1.initial_massive()

# Отображение начального состояния
j = 0
print("Изначальные узлы: ", str(m_arPos))
print("")
for i in ChordArray_1.myArray:
    print("Таблица finger для узла с id", str(m_arPos[j]))
    for k in i.finger:
        print(
            "start: "
            + str(k.start[0])
            + "; interval: ["
            + str(k.interval[0])
            + ","
            + str(k.interval[1])
            + "); node: "
            + str(k.node[0])
        )
    j += 1

# Проверка функции поиска узла
# id = 5
# id_0 = 1
print(" ")
print("Выводим узел с id " + str(id))
print("Сейчас находимся на узле: " + str(m_arPos[id_0]))
r_0 = ChordArray_1.closest_preceding_finger(m_arPos, id_0, id)
print("Результат функции closest_preceding_finger:", str(r_0))
r_1 = ChordArray_1.find_predecessor(m_arPos, id_0, id)
print("Результат функции find_predecessor:", str(r_1.finger[2].interval[1]))
r_2 = ChordArray_1.find_successor(m_arPos, id_0, id)
print("Результат функции find_successor:", str(r_2))
print(" ")

print("Добавление нового узла: ", str(new_id))
ChordArray_1.join(new_id)

print(" ")
print("Отображение состояния после добавления узла")
j = 0
for i in ChordArray_1.myArray:
    print("Таблица finger для узла с id ", str(m_arPos[j]))
    for k in i.finger:
        print(
            "start: "
            + str(k.start[0])
            + "; interval: ["
            + str(k.interval[0])
            + ","
            + str(k.interval[1])
            + "); node: "
            + str(k.node[0])
        )
    j += 1

print(" ")
print("3. Удаление узла с id ", str(del_id))
ChordArray_1.remove_node(del_id)
print(" ")
print("Отображение состояния после удаления узла")
j = 0
for i in ChordArray_1.myArray:
    print("Таблица finger для узла с id", str(m_arPos[j]))
    for k in i.finger:
        print(
            "start: "
            + str(k.start[0])
            + "; interval: ["
            + str(k.interval[0])
            + ","
            + str(k.interval[1])
            + "); node: "
            + str(k.node[0])
        )
    j += 1
