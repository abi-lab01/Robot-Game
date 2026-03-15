def numero_cuadrado(lista):
	nueva=[]	
	i=0
	while i < len(lista):
		cuadrado=lista[i]**2
		nueva.append(cuadrado)
		i+=1
	return nueva


def main():
	lista=[1,2,3]
	resultado=numero_cuadrado(lista)
	print("numeros al cuadrado",resultado)
main()