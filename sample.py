duplicate = ["nidhin","nidheesh","nivin","nidhin","nidheesh"]

new_list = []

for i in duplicate:
    if i not in new_list:
        new_list.append(i)
print(new_list)