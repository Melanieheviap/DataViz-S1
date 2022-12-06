import pandas as pd
import json

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

#Generar CSV con Puntos de Carga para 3 comunas
#Primero se hace un filtro
Filtro3Comunas = [
    DataFrame1[ DataFrame1["COMUNA"]=="RENCA" ],
    DataFrame1[ DataFrame1["COMUNA"]=="LA FLORIDA" ],
    DataFrame1[ DataFrame1["COMUNA"]=="ÑUÑOA" ]
]

#Unión de las 3 comunas filtradas
pd.concat(Filtro3Comunas).to_csv("Puntos_3_Comunas.csv", encoding= "utf-8")

