try:
    f = open("Demofile.txt")
    f.write("verify")
except:
    print("something went wrong when writing to the file")
finally:
    f.close()
