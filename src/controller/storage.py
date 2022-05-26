class StorageController:
    def __init__(self):
        self.storedCases = []

    def saveOne(self, case):
        self.storedCases.append(case)

    def getCases(self):
        return self.storedCases
