import pandas as pd
carga = pd.read_excel("carga-bip.xlsx", header=9)

print("carga en terminal",carga)
comuna = carga[ carga["MAIPU"]=="RENCA" ]
print(comuna)
variable1,variable2 = comuna.to_numpy().shape
renca = {"RENCA": variable1}
print(renca) 

