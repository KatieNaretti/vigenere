import random
vigenere_table = {}

alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя"

def create_table(vigenere_table):
	for i in alphabet:
		for j in alphabet:
			vigenere_table[i+j]=alphabet[(alphabet.find(j)+alphabet.find(i))-31]

def print_table(vigenere_table):
	temp_arr = {}
	temp_arr[0]=list(" "+alphabet)
	for i in range(0,31):
		temp_arr[i+1]=[alphabet[i]]
	for i in alphabet:
		for j in alphabet:
			temp_arr[alphabet.find(i)+1]+=[vigenere_table[i+j]]
	temp_str = ""
	for i in range(0,32):
		for j in range(0,32):
			temp_str+=temp_arr[i][j]+" "
		temp_str+="\n"
	print(temp_str)

def check(first,second):
	for i in first:
		for j in second:
			if i == j:
				return True
	return False

create_table(vigenere_table)
print_table(vigenere_table)
#creating keys
keys = {}
for i in [2,3,4,5,10,11,12,13,14,15,16,17,18,19,20]:
	keys[i]=""
	temp_char = random.choice(alphabet)
	for j in range(0,i):
		if len(keys[i])>0:

			while check(keys,temp_char):
				temp_char = random.choice(alphabet)
		keys[i]+=temp_char
		temp_char = random.choice(alphabet)
		
file = open('our-text.txt', encoding='utf-8')
base_str = file.read()


for i in keys.keys():
	cipher_text = open('cipher_texts/cipher_text['+str(i)+'].txt', 'w')
	temp_str = ""		
	for Index in range(len(base_str)):
		temp_str += vigenere_table[base_str[Index]+keys[i][Index%len(keys[i])]]
	cipher_text.write(temp_str)
	cipher_text.close()

file.close()		