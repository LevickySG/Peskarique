#Что определяет сторону пескарика? Глаз смотрящего или то, куда пескарик направляется?
#long live peskarique

import sys
#python pupfish file.xyz bottom_inner bottom_outer top_inner top_outer
#указан порядок, в котором задаются кольца трубок. Каждое кольцо задаётся двумя числами

class Tubes:
        def __init__(self, atoms, first_atom, last_atom):
                self.atom_coords = atoms[first_atom: last_atom+1]
                self.mins = self.min_()
                self.maxs = self.max_()
        def max_(self): # Получение списка с максимумами координат (xyz >[1][2][3]). Нолик для удобной нумерации
                maxs = [0.0]
                for i in range(1, 4):
                        maxs.append(max(float(coords[i]) for coords in self.atom_coords if len(coords) >1))
                return maxs
        def min_(self):# ... с минимумами координат (xyz >[1][2][3]). Нолик для удобной нумерации
                mins = [0.0]
                for l in range(1, 4):
                        mins.append(min(float(coords[l]) for coords in self.atom_coords if len(coords) >1))
                return mins

        def side(self, axis: int): # сторона "коробочки"
                return abs(self.maxs[axis] - self.mins[axis])
        def boxing(self, axis_first: int, axis_second: int):#соотношение стороны first к second
                return self.side(axis_first)/self.side(axis_second)

def kolcevanie():
        pass
def gorcevanie():
        pass

def main():
        tubes = open(sys.argv[1], 'r') #загрузка файла
        atoms = [line.split() for line in tubes.readlines()[1:]]#получение списка координат атомов, 1-индексация
#инициализация трубок
        bottom_inner = Tubes(atoms, int(sys.argv[2]), int(sys.argv[3]))#нижняя внутренняя
        bottom_outer = Tubes(atoms, int(sys.argv[4]), int(sys.argv[5]))#... внешняя

        top_inner = Tubes(atoms, int(sys.argv[6]), int(sys.argv[7]))#верхняя внутренняя
        top_outer = Tubes(atoms, int(sys.argv[8]), int(sys.argv[9]))#... внешняя

        print (f"Скукоживание Верхней трубки:\n"
        f"Внешнее кольцо : {top_outer.boxing(3,2)}\n"
        f"Внутреннее кольцо : {top_inner.boxing(3,2)}\n"
        f"Скукоживание Нижней трубки:\n"
        f"Внешнее кольцо : {bottom_outer.boxing(3,1)}\n"
        f"Внутреннее кольцо : {bottom_inner.boxing(3,1)}")

        log_out = open("log.txt", 'w', encoding='utf-8')
        log_out.write(f"Верхняя трубка:\n"
                      f"кольцо\tвнешнее\tвнутреннее\n"
                      f"ширина\t{top_outer.side(3):.5f}\t{top_inner.side(3):.5f}\n"
                      f"длина\t{top_outer.side(2):.5f}\t{top_inner.side(2):.5f}\n"
                      f"жимка\t{top_outer.boxing(3,2):.5f}\t{top_inner.boxing(3,2):.5f}\n")
        log_out.write(f"Нижняя трубка:\n"
                      f"кольцо\tвнешнее\tвнутреннее\n"
                      f"ширина\t{bottom_outer.side(3):.5f}\t{bottom_inner.side(3):.5f}\n"
                      f"длина\t{bottom_outer.side(1):.5f}\t{bottom_inner.side(1):.5f}\n"
                      f"жимка\t{bottom_outer.boxing(3, 1):.5f}\t{bottom_inner.boxing(3, 1):.5f}\n")
        log_out.close()
        tubes.close()
if __name__ == "__main__":
        main()

