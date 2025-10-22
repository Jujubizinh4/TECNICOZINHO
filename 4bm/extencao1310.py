#exemplo

import pandas as pd
data = {
    "Aniversario": ["19/02/1969", "11/02/1980","08/03/2000"],
    "Aniversariantes": ["Elaine","David","David Lucas"],
    "Rotulos": ["Mãe","Pai","Irmao mais velho"]
}

df = pd.DataFrame(data)
print(df)
print("\n")