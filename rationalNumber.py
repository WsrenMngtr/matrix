class RationalNumber:
    def __init__(self, numerator, denominator=1):
        if isinstance(numerator, RationalNumber):
            self.num = int(numerator.num)
            self.den = int(numerator.den)
            return
        self.num = numerator
        self.den = denominator
        self.toSimple()

    def toSimple(self):
        if self.den < 0:
            self.num *= -1
            self.den *= -1
        if not self.num:
            self.den = 1
            return
        coe = 2
        while coe <= abs(min(self.num, self.den)):
            if self.num % coe == 0 and self.den % coe == 0:
                self.num //= coe
                self.den //= coe
            else:
                coe += 1

    def bothMul(self, other):
        self.num *= other
        self.den *= other

    def copy(self):
        return RationalNumber(self.num, self.den)

    def __float__(self):
        return (self.num / self.den)

    def __lt__(self, other):
        return float(self) < float(other)

    def __bool__(self):
        return bool(self.num)

    def __imul__(self, other):
        other = RationalNumber(other)
        self.num *= other.num
        self.den *= other.den
        self.toSimple()
        return self

    def __mul__(self, other):
        reNum = self.copy()
        reNum *= other
        return reNum

    def __rmul__(self, other):
        return (self * other)

    def __invert__(self):
        reNum = self.copy()
        if reNum.num:
            reNum.num, reNum.den = reNum.den, reNum.num
        else:
            raise ZeroDivisionError
        return reNum

    def __itruediv__(self, other):
        if other:
            self *= ~other
        else:
            raise ZeroDivisionError
        return self

    def __truediv__(self, other):
        reNum = self.copy()
        reNum /= other
        return reNum

    def __rtruediv__(self, other):
        return (RationalNumber(other) / self)

    def __iadd__(self, other):
        other = RationalNumber(other)
        self.bothMul(other.den)
        self.num += (other.num * (self.den // other.den))
        self.toSimple()
        return self

    def __add__(self, other):
        reNum = self.copy()
        reNum += other
        return reNum

    def __radd__(self, other):
        return (self + other)

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return ("%d/%d" % (self.num, self.den))

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    tr = RationalNumber(2, 2)
    tr.toSimple()
    print(tr)
