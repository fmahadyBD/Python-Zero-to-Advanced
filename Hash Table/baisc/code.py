#create
hash_table={}
#insert
hash_table['Mahady']=10
hash_table['Hasan']=100
hash_table['Fahim']=1000

#print
print("Print the value of Mahady",hash_table['Mahady'])
#Update
hash_table['Mahady']+=3
print("Print the update value of Mahady",hash_table['Mahady'])
# delettion
del hash_table['Mahady']

#iteration
for key,value in hash_table.items():
    print(f"{key}: {value}")
