import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("komtopp50_2020.xlsx", header = 6, usecols="A:F", sheet_name="Totalt")

df = df.rename(columns={2020: "Rang 2020",2019: "Rang 2019", "Unnamed: 2": "Kommun",'2020.1': "Folkmängd 2020",'2019.1': "Folkmängd 2019",'%': "Förändring"})
sorted_df = df.sort_values(by='Folkmängd 2020', ascending=False, ignore_index=True)

colors = plt.cm.tab10.colors

storst5 = df.nlargest(5, "Folkmängd 2020").sort_values("Folkmängd 2020", ascending=False)
minst5 = df.nsmallest(5, "Folkmängd 2020").sort_values("Folkmängd 2020", ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(storst5["Kommun"], storst5["Folkmängd 2020"], color=colors[:5])
axes[0].set_title("Sveriges 5 största kommuner 2020")

axes[1].bar(minst5["Kommun"], minst5["Folkmängd 2020"], color=colors[:5])
axes[1].set_title("Sveriges 5 minsta kommuner 2020")

for ax in axes:
    ax.set_xlabel("Kommun")
    ax.set_ylabel("Folkmängd 2020")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()