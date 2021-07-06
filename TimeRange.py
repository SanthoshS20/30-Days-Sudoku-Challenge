lines = []
with open('Time.txt') as f:
    lines = f.readlines()
f.close()

total_lines = len(lines)

TimeTakenInDays = dict()
DifficultLevelInEachDays = dict()
day = 1
for index in range(total_lines):
    if(index!=0):
        difficultLevel, Time = lines[index].split(" ")
        TimeTakenInDays["Day "+str(day-1)] = int(Time)
        DifficultLevelInEachDays["Day "+str(day-1)] = difficultLevel
    day+=1


easyAverage = 0
# 20 minutes
easyMin = 1200
easyMax = 0
easyCount = 0

mediumAverage = 0
# 60 minutes
mediumMin = 3600
mediumMax = 0
mediumCount = 0

hardAverage = 0
# 2 hours
hardMin = 7200
hardMax = 0
hardCount = 0

for index in range(total_lines-1):
    key = "Day {}".format(index+1)
    if(DifficultLevelInEachDays[key]=="Easy"):
        easyAverage+=TimeTakenInDays[key]
        if(TimeTakenInDays[key]>easyMax):
            easyMax = TimeTakenInDays[key]
        if(TimeTakenInDays[key]<easyMin):
            easyMin = TimeTakenInDays[key]
        easyCount+=1
    elif(DifficultLevelInEachDays[key]=="Medium"):
        mediumAverage+=TimeTakenInDays[key]
        if(TimeTakenInDays[key]>mediumMax):
            mediumMax = TimeTakenInDays[key]
        if(TimeTakenInDays[key]<mediumMin):
            mediumMin = TimeTakenInDays[key]
        mediumCount+=1
    elif(DifficultLevelInEachDays[key]=="Hard"):
        hardAverage+=TimeTakenInDays[key]
        if(TimeTakenInDays[key]>hardMax):
            hardMax = TimeTakenInDays[key]
        if(TimeTakenInDays[key]<hardMin):
            hardMin = TimeTakenInDays[key]
        hardCount+=1
    
lines = []
with open("README.md", "r") as f:
    lines = f.readlines()
f.close()

del lines[8:len(lines)]

with open("README.md", "w") as f:
    for line in lines:
        f.write(line)
f.close()


with open("README.md", "a") as f:
    for index in range(total_lines-1):
        key = "Day {}".format(index+1)
        f.write("\n"+key+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
        f.write(DifficultLevelInEachDays[key]+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
        f.write(str(TimeTakenInDays[key]))
        f.write("<br />")
    
    f.write("<br /><br />")
    if(easyCount!=0):
        f.write("\nEasy Level\n")
        f.write("\nEasy Minimum Time Taken - "+str(easyMin))
        f.write("\n\nEasy Maximum Time Taken - "+str(easyMax))
        f.write("\n\nAverage Time Taken - "+str(easyAverage//easyCount))
    
    f.write("<br /><br />")

    if(mediumCount!=0):
        f.write("\n\nMedium Level\n")
        f.write("\nMedium Minimum Time Taken - "+str(mediumMin))
        f.write("\n\nMedium Maximum Time Taken - "+str(mediumMax))
        f.write("\n\nAverage Time Taken - "+str(mediumAverage//mediumCount))
    
    f.write("<br /><br />")

    if(hardCount!=0):
        f.write("\n\nHard Level\n")
        f.write("\n\nHard Minimum Time Taken - "+str(hardMin))
        f.write("\n\nHard Maximum Time Taken - "+str(hardMax))
        f.write("\n\nAverage Time Taken - "+str(hardAverage//hardCount))

f.close()

  