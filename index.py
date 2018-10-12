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

def search_index_matching(Our_string,key_length):
	temp_string = ""
	for i in range(0,len(Our_string),key_length):
		temp_string+=Our_string[i]
	temp_dict = {}
	for i in alphabet:
		temp_dict[i]=0
	for i in alphabet:
		for j in temp_string:
			if i == j:
				temp_dict[i]+=1
	index_matching = 0
	for i in temp_dict.keys():
		index_matching+=(temp_dict[i])*(temp_dict[i]-1)/(len(temp_string)*(len(temp_string)-1))
	return index_matching

create_table(vigenere_table)
#print_table(vigenere_table)
#creating keys
index_dict ={}

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
index_dict['open']=search_index_matching(base_str,1)

for i in keys.keys():
	cipher_text = open('cipher_texts/cipher_text[{}].txt'.format(str(i)), 'w')
	temp_str = ""		
	for Index in range(len(base_str)):
		temp_str += vigenere_table[base_str[Index]+keys[i][Index%len(keys[i])]]
	index_dict[str(i)]=search_index_matching(temp_str,i)
	cipher_text.write(temp_str)
	cipher_text.close()

print('<---match indices--->')
for i in index_dict.keys():
	print('[{}]:{}'.format(i,str(index_dict[i])))
file.close()		