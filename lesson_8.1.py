class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-' : my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Correct'
                else:
                    return f'Error. Wrong year!'
            else:
                return f'Error. Wrong month!'
        else:
            return f'Error. Wrong day!'

    def __str__(self):
        return f'Current date {Data.extract(self.day_month_year)}'


today = Data('25 - 5 - 2021')
print(today)
print(Data.valid(32, 11, 2022))
print(today.valid(11, 43, 2011))
print(Data.extract('1 - 2 - 2003'))
print(today.extract('25 - 5 - 2021'))
print(Data.valid(1, 11, 2000))
