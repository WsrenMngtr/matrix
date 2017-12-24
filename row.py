import rationalNumber
Number = rationalNumber.RationalNumber
'Number = float'


class Row:
    class CoefficientNumberError(ValueError):
        pass

    def __init__(self, coefficient, constant):
        for index in range(len(coefficient)):
            coefficient[index] = Number(coefficient[index])
        constant = Number(constant)
        coefficient.insert(0, constant)
        self.coefficient = coefficient

    def toSimple(self, index):
        self *= (1 / self[index])

    def findFirstNotZero(self):
        for index in range(1, len(self)):
            if self[index]:
                return index
        return None

    def copy(self):
        return Row(self[1:], self[0])

    def solve(self):
        xNumber = self.findFirstNotZero()
        solution = ''
        if self[xNumber] == 1:
            solution += ('x%d = %d' % (xNumber, self[0]))
            for index in range(xNumber + 1, len(self)):
                if self[index]:
                    solution += (' %dx%d' % (-self[index], index))
        return solution

    def __len__(self):
        return len(self.coefficient)

    def __getitem__(self, key):
        return self.coefficient[key]

    def __setitem__(self, key, value):
        self.coefficient[key] = value

    def __lt__(self, other):
        return self[1:] < other[1:]

    def __imul__(self, other):
        other = Number(other)
        for index in range(len(self)):
            self[index] *= other
        return self

    def __mul__(self, other):
        reRow = self.copy()
        reRow *= other
        return reRow

    def __rmul__(self, other):
        return (self * other)

    def __iadd__(self, other):
        if len(self) != len(other):
            raise Row.CoefficientNumberError
        for index in range(len(self)):
            self[index] += other[index]
        return self

    def __add__(self, other):
        reRow = self.copy()
        reRow += other
        return reRow

    def __neg__(self):
        return (self * (-1))

    def __str__(self):
        return str(self[1:] + self[0:1])

    def __repr__(self):
        return 'Raw%s' % str(self)


if __name__ == '__main__':
    ar = Row([6, 2, 3, 4, 9, 0, 6], 2)
    br = Row([1, 2, 4, 8, 7, 6, 3], 6)
    br *= 4
    print(br.solve())
