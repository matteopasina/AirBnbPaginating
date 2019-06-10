
class Paginating:
    def __init__(self, num, results):
        self.num = num
        self.results = results
        self.page = []
        self.pages = []
        self.appeared = set()

    def check_reset(self):
        if len(self.page) == num:
            self.appeared = set()
            self.pages.append(self.page)
            self.page = []
        
    def all_appeared(self):
        for result in self.results:
            record = result[0].split(',')
            if record[0] not in self.appeared:
                return False
        return True

    def search_not_appeared(self):
        for i in range(len(self.results)):

            record = self.results[i][0].split(',')

            if record[0] not in self.appeared:
                print('Record not in self.appeared {}'.format(record[0]))
                self.appeared.add(record[0])
                self.page.append(self.results[i])
                del self.results[i]
                self.check_reset()
                return

    def paginate(self):

        while self.results:
            record = self.results[0].split(',')

            if record[0] in self.appeared:
                if self.all_appeared():
                    while self.results:
                        self.page.append(self.results.pop(0))
                        self.check_reset()
                        break
                else:
                    self.search_not_appeared()

            else:
                print(record[0])
                self.appeared.add(record[0])
                self.page.append(self.results.pop(0))
    
            self.check_reset()

        self.pages.append(self.page)
        return self.pages


if __name__ == "__main__":
    num = 5
    results = [
        "1, a, 300.6, SF",
        "4, b, 209.1, SF",
        "20, c, 203.4, SF",
        "6, e, 202.9, SF",
        "6, f, 199.8, SF",
        "1, g, 190.5, SF",
        "6, h, 185.3, SF",
        "7, j, 180.0, SF",
        "6, v, 162.2, SF",
        "2, v, 161.7, SF",
        "2, v, 149.8, SF",
        "3, v, 146.7, SF",
        "2, v, 141.8, SF",
    ]
    p = Paginating(num, results)
    res = p.paginate()
    print('\n')
    print('Pages:\n')
    for page in res:
        for rec in page:
            print(rec)
        print('\n')