a <- 1
#수행 : ctrl + Enter 

rm(a) #변수삭제

a <- 1
b <- 2
c <- 3

ls()

rm(a,b)

a+b+c
c() #combine 

var1 <- c(1,2,5,7,8)
var2 <- c(6:9)

vector1 <- c(1:100)

var3 = seq(1,10, by=2)
var4 <- seq(1,5)
var5 <- 1:5

var5 + 2 
var5 + vector1

str1 <- 'hello  hi'
str1 + 2 

mean(var1)
max(vector1)
str2 <- paste(str1)
str2

# package 설치 ------ ggplot2: 대표적 그래픽 시스템(lib)
#install.packages('ggplot2',dependencies = TRUE) #package 명 ''로 전달
library(ggplot2) #package 로딩

qplot(var4)

mpg # sample dataset 
qplot(data=mpg, x = hwy, y = drv, geom = 'line')
qplot(data=mpg, x = drv, y = hwy, geom = "boxplot")

