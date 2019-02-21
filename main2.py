mathscore = [10,1,20,52,63,58,74,16]
print(mathscore[0])
print(mathscore[1:5])
print(mathscore[3:6])
print(mathscore[-5])
print(mathscore[:7])
print(mathscore[4:])
print(mathscore[-4:-1])
s=sum(mathscore)
print(max(mathscore))
print(min(mathscore))
print(s/len(mathscore))
aa=[]
aa.append(5)
print(aa)
aa.insert(0,10)
print(aa)
aa.append(60)
print(aa)
mathscore = [10,1,10,52,74,58,74,74]
del mathscore[-1]
print(mathscore)
mathscore.remove(52)
print(mathscore)
mathscore[1]=50
print(mathscore)
print(74 in mathscore)
print(2 in mathscore)
print(mathscore.count(10))
bb=['a','d','hhh']
print(mathscore + bb)

cc=[[1,50,90],[99,88]]
print(cc[1][1],cc[0][2])
print(sorted(cc))

grades=[[5,14,7],[23,36,28],[88,80,92]]
print(grades[2])

s=sum(grades[0])
print(s/len(grades))

ss=sum(grades[1])
print(ss/len(grades))

sss=sum(grades[2])
print(sss/len(grades))

grades.append([94,90,96])
print(grades)
