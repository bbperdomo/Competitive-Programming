
while True:

    try:
        print(str(input()))
    except EOFError:
        break


while True:
	try:
		n = input()
	except EOFError:
		break
	
	print(n)