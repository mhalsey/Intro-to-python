first = input("What is your first bat?")

second = input("What is your second bat?")

third = input("What is your third bat?")
#User inputs for all three bats

genus1 = first[0:3]
#Takes first 3 letters of genus

species1 = first[7:10]
#Take first 3 letters of specifi epithet

cat1= genus1+species1
#Concatenates the two

bat1 = cat1.upper()
#Makes them uppercase

genus2 = [0:3]

species2 = [7:10]

cat2 = genus2+species2

bat2 = cat2.upper()

species3 = third[0:3]

genus3 = third[10:13]

cat3 = genus3+species3

bat3 = cat3.upper()

print("There are three species of bats: \n"bat1" \n"bat2" \n"bat3")
#This likely does not work, but is supposed to print out the above statement with newline characters. 