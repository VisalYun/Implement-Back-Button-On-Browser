class Tab:
    def __init__(self):
        self._visitedPage = list()
        print("Welcome to the first page of tab")

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._visitedPage)

    def getCurrentPage(self):
        if self.isEmpty():
            return "Welcome to the first page of tab"
        else:
            return self._visitedPage[-1]

    def goBack(self):
        if self.isEmpty():
            print("Back from Browser")
            return False
        else:
            print("Back from: ", self._visitedPage.pop())
            return True

    def goForward(self, pageName):
        self._visitedPage.append(pageName)

    def getCurrentVisitedPage(self):
        print(self._visitedPage)
            
        
