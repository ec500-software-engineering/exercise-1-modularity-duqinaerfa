#copyright @ Gang Wei
class storage_thread():
    def __init__(self, bo, bp, pul):
        self.bo = bo
        self.bp = bp
        self.pul = pul
    def filter(self):
        return 0
        #for useful data
    # connection to the database
    # storage the data into the database
    # extract the data out of the database of the format
    def read(self,tp):
        if tp == "bo":
            return self.bo
        elif tp == "bp":
            return self.bp
        elif tp == "pul":
            return self.pul

    # for example: print(storage(3,4,5).read())
    # which is bo = 3,bp = 4,and pul = 5