def get_ganador(lista):
	sumas=[]
	for fila in lista:
		sumas.append(sum(fila))
	print (sumas)
	
	for i in range (3):
		sumas.append(lista[0][i]+ lista[1][i] + lista[2][i])
	print sumas
	sumad1=0
	sumad2=0
	for i in range (3):
		sumad1= lista[1][i]
		sumad2= lista[1][i-2]
	sumas.append(sumad1)
	sumas.append(sumad2)
	print (sumas)
		

	
