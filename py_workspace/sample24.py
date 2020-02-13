#for 문 

# Var자리의변수는 새로 선언되는 변수
# for Var in List 

scores = {99, 100, 88, 89, 77,88}

for (index, score) in enumerate(scores) : 
    print(index,  ":", score)
    pass

print("Done.")