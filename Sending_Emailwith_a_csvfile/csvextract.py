import csv

file = open('School of AI, Kochi Meetup #1 (Responses) - Form responses 1.csv')
fileread = csv.reader(file)

data = list(fileread)

name = []
email = []

# Getting email address from data

cnt =0
for i in range(1,len(data)):
    email.insert(cnt,data[i][1])
    cnt +=1

print(email)

for i in range(1,len(data)):
    name.insert(cnt,data[i][2])
    cnt +=1

print(name)

