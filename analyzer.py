import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


print(*[filename.removesuffix(".json") for filename in os.listdir("./opinions")], sep="\n")

product_code = input("Podaj kod produktu: ")

opinions = pd.read_json(f"opinions/{product_code}.json")
opinions.score = opinions.score.map(lambda x: x.split("/")[0].replace(",",".")).astype(float)
stats = {
    "opinions_count": opinions.shape[0],
    "pros_count":opinions.pros.astype(bool).sum(),
    "cons_count":opinions.cons.astype(bool).sum(),
    "average_score":opinions.score.mean()

}

if not os.path.exists("./plots"):
    os.mkdir("./plots")
    
stars = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
stars.plot.bar()
plt.savefig(f"./plots/{product_code}_stars.png")
plt.show()


print(f"""Dla produktu o kodzie {product_code}
pobranych zostało {stats["opinions_count"]} opinii.
Dla {stats["pros_count"]} opinii podana została lista zalet produktu,
a dla {stats["cons_count"]} opinii podana została lista wad produktu.
Średnia ocena produktu wynosi {stats["average_score"]:.2f}.""")

#dodatkowe punkty: 1. drugi wykres kołowy dla ilu opinii jest polecam dla ilu nie polecam i dla ilu none drop an a do value counts nie pomija none??
#zapis do pliku katalog plots i zapisywac je brak indeksowania w repo
recommendations = opinions.recommendation.value_counts(dropna=False)
print(recommendations)
recommendations.plot.pie(
    label="",
    labels = ["Recommended", "Not-recommended", "Neutral"],
    colors = ["limegreen", "red","navy"],
    autopct="%1.1f%%",
)
plt.title("Recommendations")
plt.savefig(f"./plots/{product_code}_pie.png")
plt.close()



