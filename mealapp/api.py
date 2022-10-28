import requests

FOOD_API=f'https://Kubatbek.pythonanywhere.com/api/v1/Clothes'
res=requests.get(FOOD_API)
jeyson=res.json()
run = len(jeyson)
i = 0
ii = []
while i < run:
  i+=1
  ii.append(i)
ii.insert(0,0)
ii.pop()
employee_id = []
employee_title = []
employee_description = []
employee_image = []
employee_price = []
employee_size = []
employee_brand_of_clothes = []
employee_gender_of_clothes = []
for i in ii:
    employee_id.append(jeyson[i]['id'])
    employee_title.append(jeyson[i]['clothes_name'])
    employee_description.append(jeyson[i]['description'])
    employee_image.append(jeyson[i]['image'])
    employee_price.append(jeyson[i]['price'])
    employee_size.append(jeyson[i]['size'])
    employee_brand_of_clothes.append(jeyson[i]['brand_of_clothes'])
    employee_gender_of_clothes.append(jeyson[i]['gender_of_clothes'])
zipped_val = zip(
employee_id,
employee_title,
employee_description,
employee_image,
employee_price,
employee_size,
employee_brand_of_clothes,
employee_gender_of_clothes
)
zipped_lst = list(zipped_val)