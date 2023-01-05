
import os
import imageio

file_list = sorted(os.listdir("imggg"))
print(file_list)

images = []

for file_name in file_list:
    file_path = "imggg/" + file_name
    image = imageio.v2.imread(file_path)
    images.append(image)

imageio.mimsave("my_GIF.gif", images)
