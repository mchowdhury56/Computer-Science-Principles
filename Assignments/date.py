DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
               self.day == d2.day

    def tomorrow(self):
        '''Changes the object to represent one day after it was
            originally represented.'''
        self.day += 1
        if self.month == 12 and self.day == 32:
            self.month = 1
            self.day = 1
            self.year += 1
        if self.isLeapYear() == True and self.month == 2 and self.day == 30:
            self.month = 3
            self.day = 1
        if self.isLeapYear() == False and self.month == 2 and self.day == 29:
            self.month = 3
            self.day = 1
        if self.month != 2:
            for monthnum in range(len(DAYS_IN_MONTH) - 1):
                if self.month == monthnum:
                    if self.day > DAYS_IN_MONTH[monthnum]:
                        self.month += 1
                        self.day = 1

    def yesterday(self):
        '''Changes the object to represent one day before it was
            originally represented.'''
        self.day -= 1
        if self.day == 0 and self.month == 1:
            self.month = 12
            self.day = 31
            self.year -= 1
        if self.isLeapYear() == True and self.month == 3 and self.day == 0:
            self.month = 2
            self.day = 29
        if self.isLeapYear() == False and self.month == 3 and self.day == 0:
            self.month = 2
            self.day = 28
        if self.month != 3:
            for monthnum in range(1,len(DAYS_IN_MONTH)):
                if self.day == 0:
                    self.month -= 1
                    self.day = DAYS_IN_MONTH[monthnum]
        

    def addNDays(self, N):
        '''Changes the object to represent N days after it was
            originally represented.'''
        print(self)
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        '''Changes the object to represent N days after it was
            originally represented.'''
        print(self)
        for i in range(N):
            self.yesterday()
            print(self)

    def isBefore(self, d2):
        '''Returns True if the object called is before the date d2 and
            False if it is after d2.'''
        if self.year < d2.year:
            return True
        if self.year == d2.year:
            if self.month < d2.month:
                return True
        if (self.year == d2.year) and (self.month == d2.month):
            if self.day < d2.day:
                return True
        else:
            return False

    def isAfter(self, d2):
        '''Returns True if the object called is after the date d2 and
            False if it is before d2.'''
        if self.year > d2.year:
            return True
        if self.year == d2.year:
            if self.month > d2.month:
                return True
        if (self.year == d2.year) and (self.month == d2.month):
            if self.day > d2.day:
                return True
        else:
            return False

    def diff(self, d2):
        '''Returns the number of days between the object called and
            a date d2.'''
        result = 0
        x = self.copy()
        y = d2.copy()
        while x.isBefore(y):
            x.tomorrow()
            result -= 1
        while x.isAfter(y):
            y.tomorrow()
            result += 1
        return result

    def dow(self):
        '''Returns a string indicating the day of the week the date
            object is.'''
        x = Date(11, 9, 2011)
        if self.diff(x) % 7 == 0:
            return 'Wednesday'
        if self.diff(x) % 7 == 1:
            return 'Thursday'
        if self.diff(x) % 7 == 2:
            return 'Friday'
        if self.diff(x) % 7 == 3:
            return 'Saturday'
        if self.diff(x) % 7 == 4:
            return 'Sunday'
        if self.diff(x) % 7 == 5:
            return 'Monday'
        if self.diff(x) % 7 == 6:
            return 'Tuesday'
