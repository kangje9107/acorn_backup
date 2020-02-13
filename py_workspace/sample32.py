#Variant Argument
def summation(*scores):
    print('-summation() invoked.')
    
    print('\t+ type(scores):',type(scores))
    print('\t+ scores:', scores)

    total=0
    for score in scores :
        total += score 
        pass # for
    return total
    pass

summation()
result = summation(1,2,3,4,5,6,7,9,10,11)
print(result)


def userprofile(**userinfo):
    print("- userprofile(() invoked.)")
    print("\t + type(userinfo):", type(userinfo))
    print("\t + userinfo:", userinfo)

    pass

userprofile(
    name="ys", age="24", tel='000-0000-0000', 
    name2="ys", age3="24", tel4='000-0000-0000'
    )


#여러 Argument 혼합할때는 , *와 **가 일반매개변수보다 뒤로 나와야됨
def func(pos1, pos2, *vargs, **kwargs): 
    print("\t+ pos1: ", pos1)
    print("\t+ pos2: ", pos2)
    print("\t+ vargs: ", vargs)
    print("\t+ kwargs: ", kwargs)
    pass

func(1, 2, 345, 678, name = "JH")

