import random
import datetime


class WorkTime:
    def __init__(self, date: datetime.date):
        self.date = date
        self.in_time = None
        self.out_time = None

    @classmethod
    def __random_time(cls, start_n, end_n):
        # 不足两位补0
        # eg:  randomTime(0,60)
        # 优化迭代： 废弃
        result = random.randint(start_n, end_n)
        if result < 10:
            return "0" + str(result)
        else:
            return str(result)

    def log_time(self):
        in_time = datetime.time(random.randint(5, 5), random.randint(0, 10), random.randint(0, 59))
        out_time = datetime.time(random.randint(23, 23), random.randint(55, 59), random.randint(0, 59))
        self.in_time = datetime.datetime.combine(self.date, in_time)
        self.out_time = datetime.datetime.combine(self.date, out_time)

    def regular_time(self):
        in_time = datetime.time(random.randint(9, 9), random.randint(0, 29), random.randint(0, 59))
        out_time = datetime.time(random.randint(19, 21), random.randint(0, 59), random.randint(0, 59))
        self.in_time = datetime.datetime.combine(self.date, in_time)
        self.out_time = datetime.datetime.combine(self.date, out_time)

    def __str__(self):
        return '%s  %s  %s' % (str(self.date), str(self.in_time), str(self.out_time))


if "__main__" == __name__:
    worktime = WorkTime(datetime.date.today())
    worktime.log_time()
    print(worktime.__dict__)
    worktime.regular_time()
    print(worktime.__dict__)
