class StorageController:
    def __init__(self):
        self.storedCases = []

    def saveOne(self, case):
        index = self.__get_index(case.identificator())
        if index != -1:
            print('Duplicated identificator, not saved!')
            return
        self.storedCases.append(case)

    def getCases(self):
        return self.storedCases

    def getOne(self, identificator):
        index = self.__get_index(identificator)
        if index == -1:
            return
        return self.storedCases[index]

    def removeCase(self, identificator):
        index = self.__get_index(identificator)
        if index == -1:
            return
        self.storedCases.pop(index)

    def __get_index(self, identificator):
        i = 0
        for i in range(self.storedCases.__len__()):
            if self.storedCases[i].identificator() == identificator:
                return i
        return -1
