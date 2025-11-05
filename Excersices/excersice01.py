import pandas as pd

data = {
    "Kommun": ["Malmö", "Stockholm", "Uppsala", "Göteborg"],
    "Population": [347949, 975551, 233839, 583056]
}

df = pd.DataFrame(data)
print(df)

row = df[df["Kommun"] == "Göteborg"]
print(row)

sorted_df = df.sort_values(by="Population", ascending=False).reset_index(drop=True)
print(sorted_df)

total_population = 10379295

df["Population(%)"] = df["Population"] / total_population * 100
df["Population(%)"] = df["Population(%)"].round(2)
print(df)    