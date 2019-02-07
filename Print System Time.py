import time

while True:
    time.sleep(1)
    from time import gmtime, strftime
    print("_" *19)
    print(strftime("%d-%m-%Y %H:%M:%S", gmtime()))
    print("_" *19)
    
