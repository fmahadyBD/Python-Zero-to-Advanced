try:
    f=open("daemo.txt")
    print(f.read())
    try:
        f.write("lorem")
    except:
        print("wrong in wrating problem")
    finally:
        f.close()

except:
    print("Oping problem")