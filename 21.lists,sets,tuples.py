#collection=single "variable" used to store multiple values
# List= [] ordered and changeable. Duplicates OK
# Set= {} unordered and immutable, but ADD/REMOVE OK. No duplicates
#Tuple= () ordered and unchangeable. Duplicates Ok. Faster

#fruits = ["banana", "orange","cherry","strawberry"]

#print(fruits[0::2])

#for x in fruits:
 #   print(x)


 #print(dir(fruits))  çalışmıyor ama sonra açıklıcakmış
 #print(help(fruits))  çalışmıyor
 #print(len(fruits))   çalışmıyor aq

#print("pineapple" in fruits)   #Returns boolean     # in i kullanarak içinde olup olmadığını bulabiliriz
#fruits[1]="pineapple"
#fruits.append("pineapple") #adds at the and of the list
#fruits.remove("banana") #deletes what is inside written

#fruits.insert(0,"pineaplle")

#fruits.sort()  #alfabetik sıraya koyuyor

#fruits.reverse()#yazdığımız sırayı reverseliyor

#fruits.clear() output[]

#print(fruits.index("orange"))  #gives the index of the written value  #if not in the lsit error

#print(fruits.count("banana"))  #listteki valueların sayısını verir

#for fruit in fruits:
 #   print(fruit)


#print(fruits)

#-----SETS----

#fruits = {"banana", "orange","cherry","strawberry","orange"}

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))  4
#print("pineapple" in fruits)

#print(fruits[0]) #error verir çünkü unordered set ler

#fruits.add("apple")

#fruits.remove("orange")

#fruits.pop()#removes first element randomly

#fruits.clear()   #output set()

#print(fruits)   #unordered olduğu için her printlendiğinde farklı sıra vercek
# output {'orange', 'strawberry', 'banana', 'cherry'} no duplicates


#----TUPLES----

fruits = ("banana", "orange","cherry","strawberry","orange","orange")

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)

#print(fruits.index("orange"))  #value nun nerde olduğunu söylüyor

print(fruits.count("orange"))

for fruit in fruits:
    print(fruit)
