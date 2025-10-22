import pandas as pd

frutas_data = {
    "Fruta": ["Maçã", "Banana", "Laranja", "Uva", "Maçã", "Abacaxi",
              "Morango", "Melancia", "Maçã", "Laranja"],
    "Mercado": ["Mercado A", "Mercado B", "Mercado C", "Mercado A",
                "Mercado B", "Mercado C", "Mercado A", "Mercado B",
                "Mercado C", "Mercado A"],
    "Quantidade": [10, 15, 8, 12, 20, 14, 18, 25, 9, 11]
}
df_frutas = pd.DataFrame(frutas_data)
Mercados_total = df_frutas.groupby('Mercado')['Quantidade'].sum()
print(Mercados_total)