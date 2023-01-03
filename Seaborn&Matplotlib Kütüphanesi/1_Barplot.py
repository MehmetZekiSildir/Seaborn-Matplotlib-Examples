import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("diamonds")
print(df)
print("----------------------")
print(df["cut"].value_counts())#Frekansları verir.
print("----------------------")
df["cut"].value_counts().plot(kind='bar').set_title("Frekansların Barplot'u")
plt.show()
print("--------------------------------------------------------------------")
sns.barplot(x='cut',y=df.cut.index,data=df)
plt.show()