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
        def max_(self):
                max_x = max(float(coords[1]) for coords in self.atom_coords if len(coords) >1)
                max_y = max(float(coords[2]) for coords in self.atom_coords if len(coords) >1)
                max_z = max(float(coords[3]) for coords in self.atom_coords if len(coords) >1)
                maxs = [0.0, max_x,max_y, max_z]
                return maxs
        def min_(self):
                min_x = min(float(coords[1]) for coords in self.atom_coords if len(coords) >1)
                min_y = min(float(coords[2]) for coords in self.atom_coords if len(coords) >1)
                min_z = min(float(coords[3]) for coords in self.atom_coords if len(coords) >1)
                mins = [0.0, min_x, min_y, min_z]
                return mins

        def width(self, axis: int):
                return abs(self.maxs[axis] - self.mins[axis])
        def length(self, axis:int):
                return abs(self.maxs[axis] - self.mins[axis])
        def boxing(self, axis_first: int, axis_second: int):
                return self.width(axis_first)/self.length(axis_second)

def kolcevanie():
        pass
def gorcevanie():
        pass

def main():
        tubes = open(sys.argv[1], 'r')
        atoms = [line.split() for line in tubes.readlines()[1:]]

        top_outer = Tubes(atoms, int(sys.argv[8]), int(sys.argv[9]))
        top_inner = Tubes(atoms, int(sys.argv[6]), int(sys.argv[7]))

        bottom_outer = Tubes(atoms, int(sys.argv[4]), int(sys.argv[5]))
        bottom_inner = Tubes(atoms, int(sys.argv[2]), int(sys.argv[3]))

        print (f"Скукоживание Верхней трубки:\n"
        f"Внешнее кольцо : {top_outer.boxing(3,2)}\n"
        f"Внутреннее кольцо : {top_inner.boxing(3,2)}\n"
        f"Скукоживание Нижней трубки:\n"
        f"Внешнее кольцо : {bottom_outer.boxing(3,1)}\n"
        f"Внутреннее кольцо : {bottom_inner.boxing(3,1)}")

        log_out = open("log.txt", 'w', encoding='utf-8')
        log_out.write(f"Верхняя трубка:\n"
                      f"кольцо\tвнешнее\tвнутреннее\n"
                      f"ширина\t{top_outer.width(3):.5f}\t{top_inner.width(3):.5f}\n"
                      f"длина\t{top_outer.length(2):.5f}\t{top_inner.length(2):.5f}\n"
                      f"жимка\t{top_outer.boxing(3,2):.5f}\t{top_inner.boxing(3,2):.5f}\n")
        log_out.write(f"Нижняя трубка:\n"
                      f"кольцо\tвнешнее\tвнутреннее\n"
                      f"ширина\t{bottom_outer.width(3):.5f}\t{bottom_inner.width(3):.5f}\n"
                      f"длина\t{bottom_outer.length(1):.5f}\t{bottom_inner.length(1):.5f}\n"
                      f"жимка\t{bottom_outer.boxing(3, 1):.5f}\t{bottom_inner.boxing(3, 1):.5f}\n")
        log_out.close()
        tubes.close()
if __name__ == "__main__":
        main()

