class Date:

    def __init__(self, d, m=1, y=1):
        self.day = d
        self.month = m 
        self.year = y

    def __del__(self):
        print(f"Деструктор даты: {self}")

    def __add__(self, days):
        new_date = Date(self.day, self.month, self.year)
        new_date.day += days
        
        while new_date.day > 31:
            new_date.day -= 31
            new_date.month += 1
            
        while new_date.day < 1:
            new_date.day += 31
            new_date.month -= 1
            
        while new_date.month > 12:
            new_date.month -= 12
            new_date.year += 1
            
        while new_date.month < 1:
            new_date.month += 12
            new_date.year -= 1
            
        return new_date

    def __iadd__(self, days):
        self.day += days
        
        while self.day > 31:
            self.day -= 31
            self.month += 1
            
        while self.month > 12:
            self.month -= 12
            self.year += 1
            
        return self

    def __sub__(self, days):
        return self + (-days)

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
        
    def subtract_dates(self, date2):
        days1 = self.day + self.month*31 + self.year*365
        days2 = date2.day + date2.month*31 + date2.year*365
        
        if days2 > days1:
            raise Exception("Вторая дата больше первой")
            
        return days1 - days2

    def set_date(self, d, m, y):
        if d < 1 or d > 31:
            raise Exception("Некорректный день")
            
        if m < 1 or m > 12:
            raise Exception("Некорректный месяц")
            
        if y < 1:
            raise Exception("Некорректный год")
            
        self.day = d
        self.month = m
        self.year = y
        
now = Date(9, 1, 2024)
later = Date(10, 12, 2023)

print(f"now: {now}")
print(f"later: {later}")

print(f"now - later: {now.subtract_dates(later)}")
print(f"now == later? -> {now == later}")
print(f"now + 31 days = {now + 31}") 
print(f"later - 100 days = {later - 100}")
