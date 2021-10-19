import csv ,os

os.system('cls')

with open('MoviesA.csv',encoding='utf-8') as f1:
    r1 = csv.reader(f1)
    data1 = list(r1)
    allmovies = data1[1:]
    headers = data1[0]
    headers.append('imdb_link')

with open('movie_links.csv',encoding='utf-8') as f2:
    r2 = csv.reader(f2)
    data2 = list(r2)
    LinkList = data2[1:]



# with open("Final.csv", "r+",encoding='utf-8') as f:
#     w = csv.writer(f)
#     w.writerow(headers)
#     f.close()

final = []
final.append(headers)

for row in allmovies:
    for link in LinkList:
        if(row[8] == link[0]):
            row.append(link[1])
            if(len(row) == 29):
                final.append(row)

# with open("Final.csv", "r+",encoding='utf-8') as f:
#     w = csv.writer(f)
#     w.writerows(final)

