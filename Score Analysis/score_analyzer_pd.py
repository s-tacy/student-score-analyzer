import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("scores.csv")

print(len(df))
print(df)

df.columns = df.columns.str.strip()
print(df.columns)

print("\n Average Score:", df["Score"].mean)
print("\n Highest Score:", df["Score"].max())
print("\n Lowest Score:", df["Score"].min())

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Score"].apply(get_grade)
print(df)

pass_count = (df["Score"]>=50).sum()
fail_count = (df["Score"]<50).sum()

print("\n Summary")
print("Passing students", pass_count)
print("Failing students", fail_count)

#student scores graph
df.plot(x="Grade", y="Score", kind="bar", title="Student Scores")
plt.show()

#grade distribution graph
df["Grade"].value_counts().plot(kind="bar", title="Grade Distribution")
plt.show()