import subprocess
import string

f = '''
kome kome dori negga saibu kiku negga dori kome gorenya dori negga nya kiku saibu kome kome kiku nya negga kome gorenya dyadyaaan kome kome gorenya negga kome nya kiku kiku kiku kome kome dori kome gorenya kiku kome dyadyaaan kome negga dori kome nya gorenya negga kiku kome saibu saibu kiku dyadyaaan kiku saibu negga gorenya saibu nya kome nya gorenya saibu saibu dori dyadyaaan negga dyadyaaan nya gorenya negga dori gorenya saibu negga dyadyaaan dori gorenya negga saibu kome negga dori kiku dyadyaaan kiku saibu dori gorenya saibu nya negga saibu kiku kiku gorenya gorenya saibu dori negga saibu kiku dyadyaaan kiku
'''
f = f.strip()
f = f.split(' ')

blocks = [f[i:i+8] for i in range(0, len(f), 8)]

flag = 'mireactf{'
for block in blocks[3:]:
	seq = ''
	sec = []
	for i in range(3):
		for p in string.printable[:-6]:
			if i == 2:
				for s in sec:
					tmp = seq + s + p

					with open('tmp.txt', 'w') as f:
						f.write(tmp + '\n')
					rec = subprocess.check_output('bash test.sh')
					rec = rec.strip().decode().split(':')[2][1:].split(' ')
					print(flag + tmp, rec)
					
					if rec[5:] == block[5:]:
						seq = tmp
						print(seq)
						break
				else:
					continue
				break

			tmp = seq + p

			with open('tmp.txt', 'w') as f:
				f.write(tmp + '\n')
			rec = subprocess.check_output('bash test.sh')
			rec = rec.strip().decode().split(':')[2][1:].split(' ')
			print(flag + tmp, rec)
			
			if i == 0:
				if rec[:3] == block[:3]:
					seq = tmp
					print(seq)
					break
			
			elif i == 1:
				#print(rec[3:5], block[3:5])
				if rec[3:5] == block[3:5]:
					sec.append(p)
					print(tmp)
			
			# elif i == 2:
			# 	if rec[6:] == block[6:]:
			# 		seq = tmp
			# 		print(seq)
			# 		break
	#break
	flag += seq

print(flag)
