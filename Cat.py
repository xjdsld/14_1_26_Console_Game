def intro_cat():
  with open("cat.txt", 'r') as file:
    cat_image = file.read()
    print(cat_image)
