foods_file = open('foods.txt')
f = foods_file.readlines()
modified_f = []
foods_file.close()

for element in f: 
    modified_f.append(element.strip())

modified_f = list(filter(None, modified_f))

for element in modified_f:
    if '2' in element:
        print(modified_f.index(element))
        print(element)        
        break
else:
    print("not found")


# ----------------------------------------------------------------

highfiber_file = open('highfiber.txt')
hf = highfiber_file.readlines()
modified_hf = []
highfiber_file.close()

for element in hf:
    modified_hf.append(element.strip())

modified_hf = list(filter(None, modified_hf))


# ----------------------------------------------------------------

low_glycemic_index_file = open('low-glycemic-index.txt')
lgi = low_glycemic_index_file.readlines()
modified_lgi = []
low_glycemic_index_file.close()

for element in lgi:
    modified_lgi.append(element.strip())

modified_lgi = list(filter(None,modified_lgi))



# ----------------------------------------------------------------

low_fat_file = open('lowfat.txt')
lf = low_fat_file.readlines()
modified_lf = []
low_fat_file.close()

for element in lf:
    modified_lf.append(element.strip())

modified_lf = list(filter(None,modified_lf))


all_files = [modified_f, modified_hf, modified_lgi, modified_lf]

all_files2 = [f,hf,lgi,lf]
newfiles = []

print(modified_f)

for list in all_files:
    print(list[14])
else:
    print("this did not work")
