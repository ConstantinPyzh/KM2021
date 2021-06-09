import random
import sys

def gen_file(size, symbols="latin", line=(10,50), word=(5,9), outname="gen_file.txt"): 
	size_of_file=size*(1024**2)
	print("If you want break process, enter 'stop'. If you want to find out current status, enter f")
	asking=input("Enter option")
	with open(f"{outname}", 'w') as gener_file:
		while cur_size <= size_of_file:
			#Генерация строки
			if type(line)==tuple:
				lin_len=random.randrange(line[0], line[1]+1)
			else:
				lin_len=line
			str_gen=[]
			for i in lin_len:
				# Начало генерации строки по словам
				if type(word)==tuple:
					word_len=random.randrange(word[0], word[1]+1)
				else:
					word_len=word
				word_gen=[]
				for j in word_len:
					#Начало генерации слова по буквам
					if symbols == "latin":
						word_let=random.randrange(97,123)
					elif symbols == "cyrillic":
						word_let=random.randrange(1072, 1106)
					else:
						word_let=random.randrange(48, 58)
					word_gen.append(chr(word_let))
					cur_size += getsizeof(chr(word_let))
					# Отслеживание размера файла
				gw=''.join(word_gen)
				str_gen.append(gw)
				# Создание нового слова и добавление его в будущую строку
			sg=" ".join(str_gen)
			gener_file.write(gw + "\n")
			stat_of_proc=(cur_size/size_of_file)*100
			if asking == "stop":
				break
			if asking == 'f':
				print("Current process is on " + stat_of_proc + " per cent complete")
			# Способ прервать процесс или отобразить его состояние


if len(sys.argv) > 1:
	sise=int(sys.argv[1])
	symb=sys.argv[2]
	wor=sys.argv[4]
	lin=sys.argv[3]
	fname=sys.argv[5]
else: 
	sise=input("Enter size of file: ")
	symb=input("Enter type of data: ")
	lin=input("Enter size of line: ")
	wor=input("Enter size of word: ")
	fname=lin=input("Enter name of file: ")
gen_file(sise, symb, lin, wor, fname)
