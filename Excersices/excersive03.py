import pandas as pd
import matplotlib.pyplot as plt
df_total = pd.read_excel("komtopp50_2020.xlsx", header = 6, usecols="A:F", sheet_name="Totalt")
df_male = pd.read_excel("komtopp50_2020.xlsx", header = 6, usecols="A:F", sheet_name="Män")
df_female = pd.read_excel("komtopp50_2020.xlsx", header = 6, usecols="A:F", sheet_name="Kvinnor")

df_total = df_total.rename(columns={2020: "Rang 2020",2019: "Rang 2019", "Unnamed: 2": "Kommun",'2020.1': "Folkmängd 2020",'2019.1': "Folkmängd 2019",'%': "Förändring"})
df_male = df_male.rename(columns={2020: "Rang 2020",2019: "Rang 2019", "Unnamed: 2": "Kommun",'2020.1': "Folkmängd 2020",'2019.1': "Folkmängd 2019",'%': "Förändring"})
df_female = df_female.rename(columns={2020: "Rang 2020",2019: "Rang 2019", "Unnamed: 2": "Kommun",'2020.1': "Folkmängd 2020",'2019.1': "Folkmängd 2019",'%': "Förändring"})

df_male["Kön"] = "Man"
df_female["Kön"] = "Kvinna"


df_all = pd.concat([df_male, df_female], ignore_index=True)

for col in ["Folkmängd 2020", "Folkmängd 2019", "Förändring"]:
    df_all[col] = pd.to_numeric(df_all[col], errors="coerce")

df_all_pivot = df_all.pivot_table(
    index="Kommun",
    columns="Kön",
    values=["Folkmängd 2020", "Folkmängd 2019", "Förändring"],
    aggfunc="sum"
).reset_index()

df_all_pivot.columns = [f"{col[1]} {col[0]}" if col[1] else col[0] for col in df_all_pivot.columns]

df_all_pivot["Total Pop 2020"] = df_all_pivot["Man Folkmängd 2020"] + df_all_pivot["Kvinna Folkmängd 2020"]
df_all_pivot["Total Pop 2019"] = df_all_pivot["Man Folkmängd 2019"] + df_all_pivot["Kvinna Folkmängd 2019"]

df_all_pivot["Total förändring"] = ((df_all_pivot["Total Pop 2020"] - df_all_pivot ["Total Pop 2019"]) / df_all_pivot["Total Pop 2019"] * 100)
df_total_summary = df_all_pivot[["Kommun", "Total Pop 2020", "Total Pop 2019", "Total förändring"]]

df_merged = df_all.merge(
    df_total_summary,
    on="Kommun",
    how="left"
)

df_merged = df_merged[
    [
        "Kommun",
        "Folkmängd 2020",
        "Folkmängd 2019",
        "Förändring",
        "Kön",
        "Total Pop 2020",
        "Total Pop 2019",
        "Total förändring"
    ]
]

df_merged = df_merged.sort_values("Total Pop 2020", ascending=False)

print(df_merged.head())