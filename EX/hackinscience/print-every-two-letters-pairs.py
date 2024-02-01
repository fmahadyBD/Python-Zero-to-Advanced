# This script uses the ord function to get the ASCII value of 'a' and 'z', and then it iterates through the range of ASCII values, converting them back to characters using the chr function. It prints all possible pairs of two lowercase letters, ordered alphabetically.
for i in range(ord('a'),ord('z')+1):
    for j in range(ord('a'),ord('z')+1):
        print(chr(i)+chr(j))
        
    
    