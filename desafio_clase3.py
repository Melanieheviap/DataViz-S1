import pandas as pd
import json
import matplotlib.pyplot as plt

#Leer excel desde la fila 9
DataFrame1 = pd.read_excel("carga-bip.xlsx", header=9, index_col=0)
print("Puntos BIP: ",DataFrame1)

#Corrección nombre de columna Maipu por Comuna
DataFrame1.rename(columns={"MAIPU": "COMUNA", "CERRO BLANCO 625": "DIRECCIÓN"}, inplace=True)
print("Puntos BIP corregido: ",DataFrame1)

#Filtro comuna Huechuraba
FiltroComuna = DataFrame1[ DataFrame1["COMUNA"]=="HUECHURABA" ]
print(FiltroComuna)

#Obtención de Filas y Columnas de los datos con Numpy y función "shape"
FiltroComuna_filas, FiltroComuna_columnas = FiltroComuna.to_numpy().shape

#Contador de filas en nuestro Diccionario
ContadorPC_Huechuraba = {
    "HUECHURABA": FiltroComuna_filas
}

#Guardar usando librería JSON. Indicar codificación correcta. Indentación de 2 caracteres.
with open("PuntosCarga_Huechuraba.json", "w", encoding="utf-8") as j:
    j.write( json.dumps(ContadorPC_Huechuraba, indent=2) )

#####Generar CSV con Puntos de Carga para 3 comunas
#Primero se hace un filtro para tres comunas
Filtro3Comunas = [
    DataFrame1[ DataFrame1["COMUNA"]=="RENCA" ],
    DataFrame1[ DataFrame1["COMUNA"]=="LA FLORIDA" ],
    DataFrame1[ DataFrame1["COMUNA"]=="ÑUÑOA" ]
]

#Unión de las 3 comunas filtradas
pd.concat(Filtro3Comunas).to_csv("Puntos_3_Comunas.csv", encoding= "utf-8")

#####Generación de valores ficticios para Horario Referencial
#Se utiliza como referencia la columna CODIGO (index) para crear la misma cantidad de horarios de las filas
Horario = DataFrame1.index
Horarios = []
#a los codigos de index PAR se les asigna un rango horario, y a los IMPAR, otro rango
for h in Horario:
    # h vendría siendo una representación de CODIGO, entonces se evalúa la condición
    if (h % 2 == 0):
        Horarios.append("09:00 - 13:00, 14:00 - 19:00")
    else:
        Horarios.append("08:30 - 12:30, 13:30 - 18:30")

#Reemplaza la columna de HORARIO REFERENCIAL por los horarios creados "Horarios"
DataFrame1["HORARIO REFERENCIAL"] = Horarios
DataFrame1.to_excel("Puntos_con_Horarios.xlsx")
print(DataFrame1)

#####Creación de gráfico que indique la cantidad de puntos de carga para cada horario
#Agrupar los Horarios creados
Horarios_agrup = DataFrame1.groupby(["HORARIO REFERENCIAL"])
#Conteo de elementos que hay en HORARIO REFERENCIAL
Horario_agrupado = Horarios_agrup["HORARIO REFERENCIAL"].count()

#Se hace el gráfico, primero cerrando todo gráfico previo abierto
plt.close("all")
#Generación de espacio donde se creará el nuevo gráfico
plt.figure()
#"Ploteo" de los datos previamente agrupados y contados
Horario_agrupado.plot()
#Muestra del gráfico
plt.show()
print(Horario_agrupado)
