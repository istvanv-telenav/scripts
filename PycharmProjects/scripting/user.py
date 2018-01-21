import time

print("Welcome to the keepright error filter")
workDir = input("insert the path where keepright_errors.txt can be found:")
print(workDir)
username = input("Enter the username ")
timestr = time.strftime("%Y%m%d-%H%M%S")
input_file = str(workDir) + '/keepright_errors.txt'
output_file = str(workDir) + "/results" +timestr+ ".txt"

with open(input_file, encoding="latin-1") as f, open(output_file, "w") as o:
    next(f, None)
    for row in f:
        try:
            row = row.replace("\n", ",")
            row = row.split("\t")
            row[11] = int(row[11]) / (10 ** 7)  # transforming lat/long from integer to float
            row[12] = int(row[12]) / (10 ** 7)
            lat = row[11]
            long = row[12]
            if row[10] == username:
                print(row[0], ",", row[2], ",", row[3], ",", row[10], ",", row[11], ",", row[12], file=o)
        except:
            continue