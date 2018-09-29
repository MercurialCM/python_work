favorite_languages={
	'jen':['pyhton','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['pyhton','haskell'],
}
for name,languages in favorite_languages.items():
	print('\n'+name.title()+"'s favourite languages are:")
	for language in languages:
		print(language.title())