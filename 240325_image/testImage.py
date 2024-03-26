from PIL import Image

image_path = "샤모예드.jpg"
image = Image.open(image_path)
info = image.info
print(info)
info['meta'] = "metameta"
new_image_path = "C:\\Users\\301-04\\Desktop\\new_image.jpg"
image.save(new_image_path, format='jpeg', **info)