import json
import re
from pprint import pprint

# def write(data,filename):
# 	data = json.dumps(data)
# 	data = json.loads(str(data))
# 	with open(filename, 'w', encoding = 'utf-8') as file:
# 		json.dump(data, file, indent = 4)

def read(filename):
	with open(filename, 'r', encoding = 'utf-8') as file:
		return json.load(file)

n_data = json.load((open('JSON sample.json')))
# a = n_data['sections'][1]

# b = n_data['sections'][0]['items'][22]
# pprint(b)

# class Func:

	# Section #1
def slovar_1(o):
	o = 0
	while  o <= 22:
		b = n_data['sections'][0]['items'][o]['stimulusText']
		f = b.replace(("<p style='display: inline-block; margin-left: 60px; text-indent: -20px;'>"), '')
		g = f.replace('<p>', '')
		g = g.replace('</p>', '')
		g = g.replace('<em style="font-style: italic;">', '')
		konec_1 = g.replace('</em>', '')
		print(konec_1)
		with open('beg.txt', 'a') as txt:
			txt.write(konec_1 + '\n')
			txt.close()



	# # Section #2
	#
		b = n_data['sections'][0]['items'][o]['stemText']
		g = b.replace('<p>','')
		g = g.replace('</p>','')
		g = g.replace('<em style="font-style: italic;">','')
		konec_2 = g.replace('</em>','')
		print(konec_2)
		with open('beg.txt', 'a') as txt:
			txt.write(konec_2 + '\n')
			txt.close()
	#
	#
	# # Section #3
		c = n_data['sections'][0]['items'][o]['options']
		m = 0

		while m<=4:
			a = c[m]
			r = a.get('optionContent')
			b = a.get('optionLetter')
			g = r.replace('<p>', '')
			g = g.replace('</p>','')
			g = g.replace('<em style="font-style: italic;">', '')
			g = g.replace('</em>', '')
			konec_3 = b + ' - ' + g
			print(konec_3)
			with open('beg.txt', 'a') as txt:
				txt.write(konec_3 + '\n')
				txt.close()
			m += 1
			continue

		o += 1
		continue



# call func
slovar_1(1)
