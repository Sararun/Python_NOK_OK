import mmap


#Класс парсер
class TimeParser:

    def __init__(self, input_file):
        self.file = input_file
        self.d = dict()

#   Парсинг и заполнение словаря
    def parse(self, mode="min"):
        self.d = dict()
        with open(self.file, mode="r+b") as f:
            mm = mmap.mmap(f.fileno(), 0)

            if mode == "min":
                j = 17
            elif mode == "hour":
                j = 14
            elif mode == "day":
                j = 11
            elif mode == "month":
                j = 8
            elif mode == "year":
                j = 5
            else:
                print("ERROR")
                return
            while True:
                line = mm.readline().decode()
                date = line[1:j]
                if date not in self.d.keys():
                    self.d[date] = 0
                if line[-5:-2] == "NOK":
                    self.d[date] += 1
                if not line:
                    break

#   Вывод словаря
    def print_d(self):
        if len(self.d) == 0:
            print("Пусто")
            return
        for i in self.d:
            if i and i != " ":
                print("[{0}] => {1} NOK".format(i, self.d[i]))


if __name__ == '__main__':

    filepath = "events.txt"
    tp = TimeParser(filepath)

    tp.parse("min")
   # tp.parse("hour")
   # tp.parse("day")
    #tp.parse("month")
   # tp.parse("year")
    tp.print_d()
