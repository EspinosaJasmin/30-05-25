Funcion areaCalculada <- AreaTriangulo (numa, numb)
    areaCalculada = (numa * numb) / 2
Fin Funcion
Funcion sumaCalculada <- Suma (numa, numb)
    sumaCalculada = numa + numb
Fin Funcion
Algoritmo Principal
    Escribir "Ingrese la base del triangulo:"
    Leer numa
    Escribir "Ingrese la altura del triangulo:"
    Leer numb
    resultadoArea = AreaTriangulo(numa, numb)
	resultadoSuma = Suma(numa,numb)
    Escribir "El area del triangulo es: ", resultadoArea
	Escribir "la suma es de : ", resultadoSuma
FinAlgoritmo