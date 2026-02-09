#AB 1st Writing notes

"""with open("notes\\reading.txt", "r+") as file:
    content = file.read()
    content += "\nI wrote on my file"
    file.write(content)


with open("notes\\writing.txt", "a") as file:
    file.write("This is more on my file")

print("code end")"""

import csv

with open("notes\Class CSV sample - Sheet1.csv","r+", newline='') as csvfile:
    fieldnames = ["username", "color"]
    
    reader = csv.reader(csvfile)
    for line in reader:
        print(f"{fieldnames[0]}{line[0]}")
    writer = csv.DictWriter(csvfile ,fieldnames= fieldnames)
    #writer.writeheader()
    writer.writerow({"username": "randomeusername","color": "pink"})
    writer.writerow({"username": "ran","color": "blue"})
    writer.writerow({"username": "ranername","color": "gold"})


print("code end")


