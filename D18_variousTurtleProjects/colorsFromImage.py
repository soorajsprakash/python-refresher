import colorgram

colorData = colorgram.extract('image.jpg', 30)
print(len(colorData))
colorsInRGB = []
for i in range(10):
    color = tuple(colorData[i].rgb)
    colorsInRGB.append(color)
print(colorsInRGB)
