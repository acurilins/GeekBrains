class DivisionByNull:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @staticmethod
    def div_by_zero(first, second):
        try:
            return (first / second)
        except:
            return (f"Can't divide by zero")


div = DivisionByNull(30, 300)
print(DivisionByNull.div_by_zero(23, 0))
print(DivisionByNull.div_by_zero(105, 0.1))
print(div.div_by_zero(83, 0))
