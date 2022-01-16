import hashlib

file1 = open("D:\\Devlopment\\Python3\\BlockChain Dev\\funcoin\\funcoin\\my_img.png", "rb")
img_hash1 = hashlib.sha256(file1.read()).hexdigest()
file1.close()


file2 = open("D:\\Devlopment\\Python3\\BlockChain Dev\\funcoin\\funcoin\\my_image.jpg", "rb")
img_hash2 = hashlib.sha256(file2.read()).hexdigest()
file2.close()

print(img_hash1)
print(img_hash2)