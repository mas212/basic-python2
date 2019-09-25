#simple dict

car = {
    'name' : 'scopy',
    'merk'  : 'honda',
    'price' : 10.000.000
}
print(car)

#using constructor

cars = dict({
    name = 'scopy',
    merk = 'honda',
    price = 20.000.000
})
print(cars)

#access value
print(car.get('price'))

#get keys 
print(cars.keys())
#get value
print(cars.items())