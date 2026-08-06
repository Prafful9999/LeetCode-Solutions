class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        # Reference date: 1 Jan 1971 = Friday (index 5)
        total_days = 0
        
        # count days from 1971 to year-1
        for y in range(1971, year):
            if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
                total_days += 366
            else:
                total_days += 365
        
        # days in months
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # leap year check
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            month_days[1] = 29
        
        # add days of previous months
        for m in range(month - 1):
            total_days += month_days[m]
        
        # add current day
        total_days += day - 1
        
        return days[(total_days + 5) % 7]

        