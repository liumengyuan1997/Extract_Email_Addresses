fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From ") == True:
        lst = line.split()
        ad = lst[1]
        count = count + 1
        print(ad)
    else:
        continue

print("There were", count, "lines in the file with From as the first word")
