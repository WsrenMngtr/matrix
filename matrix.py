from row import Row


class Matrix:
    def __init__(self):
        self.matrix = []

    def addRow(self, row):
        if isinstance(row, Row):
            self.matrix.append(row)
        else:
            self.matrix.append(Row(row[0:-1], row[-1]))

    def sort(self):
        self.matrix.sort(reverse=True)

    def clear(self):
        self.matrix.clear()

    def __len__(self):
        return len(self.matrix)

    def makeRowAfterThisToSimple(self, index):
        i = self[index].findFirstNotZero()
        if i is not None:
            self[index].toSimple(i)
            for eachRow in self[index + 1:]:
                eachRow += (-self[index] * eachRow[i])

    def toRowLadderMatrix(self):
        self.sort()
        for eachRow in range(len(self)):
            self.makeRowAfterThisToSimple(eachRow)

    def makeRowFrontOfThisToSimple(self, index):
        i = self[index].findFirstNotZero()
        if i is not None:
            for eachRow in self[:index]:
                eachRow += (-self[index] * eachRow[i])

    def toRowSimplestMatrix(self):
        self.sort()
        self.toRowLadderMatrix()
        for eachRow in range(len(self) - 1, -1, -1):
            self.makeRowFrontOfThisToSimple(eachRow)

    def __getitem__(self, key):
        return self.matrix[key]

    def __str__(self):
        rs = ''
        for eachRow in self.matrix:
            rs += (str(eachRow) + '\n')
        return rs

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.matrix)


if __name__ == '__main__':
    tm = Matrix()
    tm.addRow(Row([1, 2], 2))
    tm.addRow(Row([2, 1], -2))
    tm.addRow(Row([2, -2], 1))
    print(tm)
    tm.sort()
    tm.toRowLadderMatrix()
    tm.toRowSimplestMatrix()
    print(tm)
