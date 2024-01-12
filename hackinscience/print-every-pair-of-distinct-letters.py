for i in range(ord('a'),ord('z')+1):
    for j in range(ord('a'),ord('z')+1):
        if (chr(i)==chr(j)):
            continue
        print(chr(i)+chr(j))