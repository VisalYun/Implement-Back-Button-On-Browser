from Tab import Tab

print("============================")
print("\tWeb Browser ")
print("============================")

active = True

tab = Tab()
while(active):
    print("1. Forward")
    print("2. Backward")
    print("3. Reload")
    print("4. Show History")
    print("5. Exit")

    inp = int(input("Enter your choice: "))
    if inp == 1:
        pageName = input("Enter URL: ")
        tab.goForward(pageName)
        print("Currently view: ",pageName)
    elif inp == 2:
        active = tab.goBack()
    elif inp == 3:
        print(tab.getCurrentPage)
    elif inp == 4:
        tab.getCurrentVisitedPage()
    elif inp == 5:
        active=False
        print("Tab is clear!!!")
    else:
        print("Look at instruction, you idiot!!!")
    print("-----------------------------")
    
