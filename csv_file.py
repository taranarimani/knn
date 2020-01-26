import csv
with open(r'/Users/tara/Desktop/quera/IR labeling - Sheet1.csv') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(','.join(row))
# with open(r'/Users/tara/Desktop/quera/vectors.csv') as csvfile2:
#     lines =csv.reader(csvfile2)
#     for row in lines:
#         print(','.join(row))
