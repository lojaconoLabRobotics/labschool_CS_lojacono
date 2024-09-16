#code is designed to extract a piece of information from a string

#using two string functions today: split() and replace()
sunocoPrice = "Sunoco gas price: $3.39"
mirabitoPrice = "Mirabito gas price: $3.79"

#extract and isolate the prices
priceOfSunoco = sunocoPrice.split(" ")
priceOfMirabito = mirabitoPrice.split(" ")
print(priceOfSunoco[3])
print(priceOfMirabito[3])

#what kind of type of data are these?
print(type(priceOfSunoco))
print(type(priceOfMirabito))