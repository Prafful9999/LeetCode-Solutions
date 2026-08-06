class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        mon = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        week = ["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"]

        def count_leap(y):
            return y//4 - y//100 + y//400

        diff = year - 1971
        leap = count_leap(year-1) - count_leap(1970)
        edays = diff + leap
        ind_edays = edays % 7

        cydays = 0
        for i in range(1, month):
            if i == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    cydays += 29
                else:
                    cydays += 28
            else:
                cydays += mon[i]

        cydays += day
        ind_cydays = (cydays - 1) % 7

        return week[(ind_edays + ind_cydays) % 7]
