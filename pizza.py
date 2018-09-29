pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra_cheese'],
}

print('You ordered a '+pizza['crust']+'-crust pizza'+'with following toppings:')

for topping in pizza['toppings']:
	print('\t'+ topping)
