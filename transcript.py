import math

alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

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

def shift(our_str, shift_len):
	temp = our_str
	for Index in range(len(temp)):
		our_str[Index]=alphabet[math.fabs(alphabet.find(temp[Index])-shift)]
	return our_str

our_cipher_text=""
file=open('ct.txt', encoding='utf-8')
our_cipher_text = file.read()
our_cipher_text = our_cipher_text.replace(" ","")
our_cipher_text = our_cipher_text.replace("\n","")

Flag = True
i = 1
while Flag:
	if(search_index_matching(our_cipher_text,i)>=0.0553):
		Flag=False
	else:
		#print(search_index_matching(our_cipher_text,i),i)
		i+=1
		'''
for i in range(2,40):
	print(search_index_matching(our_cipher_text,i),i)
'''
print('Our key length:{}'.format(str(i)))

#blocking
block_dictionary={}

for j in range(i):
	block_dictionary[j]=""

for j in range(len(our_cipher_text)):
	block_dictionary[j%i]+=our_cipher_text[j]

frequency_dictionary={}
#search the most frequent in each block
shift_dict = {}
for j in range(0,i):
	for Index in alphabet:
		frequency_dictionary[Index]=0
	for temp_i in block_dictionary[j]:
		frequency_dictionary[temp_i]+=1

	temp_arr=list(alphabet)
	temp_Arr = []
	for Index in temp_arr:
		temp_Arr+=[frequency_dictionary[Index]]
	Flag = True
	while Flag:
 		Flag = False
 		for Index in range(len(temp_Arr)-1):
 			if temp_Arr[Index]<temp_Arr[Index+1]:
 				temp_Arr[Index],temp_Arr[Index+1]=temp_Arr[Index+1],temp_Arr[Index]
 				temp_arr[Index],temp_arr[Index+1]=temp_arr[Index+1],temp_arr[Index]
 				Flag = True
	for Index in temp_arr:
		Temp_string = "---"+Index+"---: "+str(frequency_dictionary[Index])
		
	shift_dict[j]=temp_arr[0]+temp_arr[1]+temp_arr[2]
'''
for j in range(0,i):
	print(shift_dict[j])
	'''
for j in range(0,i):
	temp_str=[shift_dict[j][0],shift_dict[j][1],shift_dict[j][2]]
	temp_str[0]=alphabet[(alphabet.find(temp_str[0])-alphabet.find('о'))%32]
	temp_str[1]=alphabet[(alphabet.find(temp_str[1])-alphabet.find('о'))%32]
	temp_str[2]=alphabet[(alphabet.find(temp_str[2])-alphabet.find('о'))%32]
	print(temp_str)
	
key = ""
for j in range(0,i):
	key+=alphabet[(alphabet.find(shift_dict[j][0])-alphabet.find('о'))%32]
print("Our key:{}".format(key))
temp_str=""
for j in range(len(our_cipher_text)):
	Index = alphabet.find(key[j%len(key)])
	Index_j=alphabet.find(our_cipher_text[j])
	temp_str+=alphabet[(Index_j-Index)%32]

print(temp_str)

file.close()