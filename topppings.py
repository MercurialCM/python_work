'''
requested_toppings=["mushrooms",'extra cheese']

if 'mushrooms' in requested_toppings:
	print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
	print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
	print('Adding extra cheese.')

print('Your pizza is ready!')
'''

requested_toppings = ['mushrooms','green peppers','extra_cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print('Sorry,we are out of green peppers.')
	else:
		print('Adding '+requested_topping +'.')
print('\nFinished making your pizza!')