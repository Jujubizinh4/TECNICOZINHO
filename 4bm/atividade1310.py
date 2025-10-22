import pandas as pd

vendas = pd.DataFrame(
    {
        "Data": [
            "2024-05-01","2024-05-02","2024-05-03","2024-05-04","2024-05-05",
            "2024-05-06","2024-05-07","2024-05-08","2024-05-09","2024-05-10"
        ], 
        "Quantidade vendida": [48,38,24,17,30,48,28,32,20,20],
        "Sabor": ["Baunilha","Creme","Creme","Creme","Baunilha",
                "Baunilha","Baunilha","Morango","Baunilha","Baunilha"]
    }
)

vendas_novas = pd.DataFrame(
    {
        "Data": ["2024-05-11","2024-05-12","2024-05-13","2024-05-14","2024-05-15",
                 "2024-05-16","2024-05-17","2024-05-18","2024-05-19","2024-05-20",],
        "Quantidade vendida": [33,45,49,33,31,11,33,39,47,54],
        "Sabor": ["Baunilha","Morango","Baunilha","Creme","Baunilha",
                  "Creme","Creme","Creme","Morango","Morango"],

    }
)

vendas_completas = pd.concat([vendas, vendas_novas], ignore_index = True)
print(vendas)