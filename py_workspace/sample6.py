elapsedDays = 0
caveHeight = 100
currentHeight = 0
slippedHeight = 5
heightPerDay = 20

while currentHeight < caveHeight :
    elapsedDays = elapsedDays + 1
    currentHeight = currentHeight + heightPerDay
    currentHeight = currentHeight - slippedHeight
    
print(elapsedDays)


