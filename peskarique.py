#Что определяет сторону пескарика? Глаз смотрящего или то, куда пескарик направляется?

import sys
#python peskarique.py before.xyz after.xyz inner_ring_first ..._last outer_first outer last

before = open(sys.argv[1], 'r')
after = open(sys.argv[2], 'r')

atoms_b = [line.split() for line in before.readlines()[1:]]
# атомы имеют 1-индексацию, прямо как в КВЬЮ! atoms_b[i] возвратит информацию о типе атома, и координатах i-го атома
# x, y, z компоненты координат имеют индексы 1, 2, 3 соответственно. 0-ой индекс тип атома.

atoms_b_inner = atoms_b[int(sys.argv[3]): int(sys.argv[4])+1]
atoms_b_outer = atoms_b[int(sys.argv[5]): int(sys.argv[6])+1]

#Для внутреннего кольца
max_y_b_in = max(float(coords[2]) for coords in atoms_b_inner if len(coords) >1)
min_y_b_in = min(float(coords[2]) for coords in atoms_b_inner if len(coords) >1)

max_z_b_in = max(float(coords[3]) for coords in atoms_b_inner if len(coords) >1)
min_z_b_in = min(float(coords[3])for coords in atoms_b_inner if len(coords)>1)

max_y_b_index_in, min_y_b_index_in, max_z_b_index_in, min_z_b_index_in = 0, 0, 0, 0


for coords in atoms_b_inner:
    if len(coords)>1:
        if float(coords[2])==max_y_b_in:
            max_y_b_index_in = atoms_b_inner.index(coords)
        if float(coords[2]) == min_y_b_in:
            min_y_b_index_in = atoms_b_inner.index(coords)
        if float(coords[3])==max_z_b_in:
            max_z_b_index_in = atoms_b_inner.index(coords)
        if float(coords[3]) == min_z_b_in:
            min_z_b_index_in = atoms_b_inner.index(coords)

#для внешнего кольца
max_y_b_out = max(float(coords[2]) for coords in atoms_b_outer if len(coords) >1)
min_y_b_out = min(float(coords[2]) for coords in atoms_b_outer if len(coords) >1)

max_z_b_out = max(float(coords[3]) for coords in atoms_b_outer if len(coords) >1)
min_z_b_out = min(float(coords[3])for coords in atoms_b_outer if len(coords)>1)

max_y_b_index_out, min_y_b_index_out, max_z_b_index_out, min_z_b_index_out = 0, 0, 0, 0

for coords in atoms_b_outer:
    if len(coords)>1:
        if float(coords[2])==max_y_b_out:
            max_y_b_index_out= atoms_b_outer.index(coords)
        if float(coords[2]) == min_y_b_out:
            min_y_b_index_out= atoms_b_outer.index(coords)
        if float(coords[3])==max_z_b_out:
            max_z_b_index_out= atoms_b_outer.index(coords)
        if float(coords[3]) == min_z_b_out:
            min_z_b_index_out= atoms_b_outer.index(coords)

#расстояния

Y_inner_before = max_y_b_in - min_y_b_in
Z_inner_before = max_z_b_in - min_z_b_in

Y_outer_before = max_y_b_out - min_y_b_out
Z_outer_before = max_z_b_out - min_z_b_out

#для структуры после
atoms_a = [line.split() for line in after.readlines()[1:]]
# атомы имеют 1-индексацию, прямо как в КВЬЮ! atoms_b[i] возвратит информацию о типе атома, и координатах i-го атома
# x, y, z компоненты координат имеют индексы 1, 2, 3 соответственно. 0-ой индекс тип атома.

atoms_a_inner = atoms_a[int(sys.argv[3]): int(sys.argv[4])+1]
atoms_a_outer = atoms_a[int(sys.argv[5]): int(sys.argv[6])+1]

#внутреннее кольцо

max_y_a_in = float(atoms_a_inner[max_y_b_index_in][2])
min_y_a_in = float(atoms_a_inner[min_y_b_index_in][2])
max_z_a_in = float(atoms_a_inner[max_z_b_index_in][3])
min_z_a_in = float(atoms_a_inner[min_z_b_index_in][3])

#внешнее кольцо
max_y_a_out= float(atoms_a_outer[max_y_b_index_out][2])
min_y_a_out= float(atoms_a_outer[min_y_b_index_out][2])
max_z_a_out= float(atoms_a_outer[max_z_b_index_out][3])
min_z_a_out= float(atoms_a_outer[min_z_b_index_out][3])

#толщины после

Y_inner_after = max_y_a_in - min_y_a_in
Z_inner_after = max_z_a_in - min_z_a_in

Y_outer_after = max_y_a_out - min_y_a_out
Z_outer_after = max_z_a_out - min_z_a_out


print("Внутреннее кольцо:")
print(f"Толщина Z до = {Z_inner_before}, после = {Z_inner_after}")
print(f"Высота Y до = {Y_inner_before}, после = {Y_inner_after}")
print(f"Соотношение толщины к высоте до = {Z_inner_before/Y_inner_before}, после = {Z_inner_after/Y_inner_after}")

print("Внешнее кольцо:")
print(f"Толщина Z до = {Z_outer_before}, после = {Z_outer_after}")
print(f"Высота Y до = {Y_outer_before}, после = {Y_outer_after}")
print(f"Соотношение толщины к высоте до = {Z_outer_before/Y_outer_before}, после = {Z_outer_after/Y_outer_after}")