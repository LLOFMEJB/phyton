learn = (input("Write what you look for...: ")).lower()
car = {
 "brand": "ford",
 "situation": "bel altı boya, çıtır hasarlı",
 "model": "mustang",
 "year": "1964",
 "price": "en son 35 bin olur"
}
key_list = list(car.keys())
val_list = list(car.values())
if learn in key_list:
    print(f"The value you're looking for is: {val_list[key_list.index(learn)]}")
elif learn in val_list:
    print(f"The key you're looking for is: {key_list[val_list.index(learn)]}")
else:
    print("We aint got anything for you man!")