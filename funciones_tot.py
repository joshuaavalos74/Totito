def get_ganador(lista):
	sumas=[]
	for fila in lista:
		sumas.append(sum(t1f))
	print (sumas)
	
	for i in range (3):
		sumas.append(lista[0][i]+ lista[1][i] + lista[2][i])
	print sumas
	sumad1=0
	sumad2=0
	for i in range (3):
		sumad1+= lista[i][i]
		sumad2+= lista[i][i-2]
	sumas.append(sumad1)
	sumas.append(sumad2)
	print (sumas)

def print_tot (lista):
	resultado=""
	for i in range (3):
		for j in range (3):
			celda= lista[i][j]
			if celda==1:
				resultado+= "X"
			elif celda ==-1:
				resultado+="O"
			else:
			resultado+= chr(3*i+j+65)		

	