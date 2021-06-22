try:
    print(x)
except:
    print("something went wrong")
finally: # irrespective of error or not, finally will always execute
    print("The try except is finished")