treeheight = int(input("enter tree height : "))

spaces = treeheight - 1

hashes = 1

stumpspaces = treeheight - 1

while treeheight != 0 :

for i in range (spaces):
    print ('',end = "")

for i in range (hashes):
print("#", end = "")
