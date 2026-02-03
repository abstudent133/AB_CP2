#AB 1st Reading Files Notes
import csv
while True:
    try:
        with open("notes/reading.txt","r") as file:
            for line in file:
                print(f"Hello {line.strip()}")
    except:
        print("That file can't be found")
        break
    else:
        print("Code ends")
        break


try:
    with open("notes\Class CSV sample - Sheet1.csv",mode ="r") as csv_file:
        content = csv.reader(csv_file)
        header = next(content)
        rows = {}
        rows.update({header[0]: line[0], header[1]: line[1]})
        for line in content:
            print(f"{line[0]} favorite color is {line[1]}")
except:
    print("this code doesn't work")
else:
    for line in rows:
        print(line)
    
