from re import findall

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
        if not self.url_check(pageName):
            print("Element {url} is not a URL")
        else:
            self._visitedPage.append(pageName)
            print("Currently view: ",pageName)

    def getCurrentVisitedPage(self):
        print(self._visitedPage)

    def url_check(pageName):
        url = findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        return True if len(url) != 0 else False
        
