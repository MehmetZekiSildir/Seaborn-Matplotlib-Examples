import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("diamonds")
sns.catplot(x="cut",y="price",data=df)
plt.show()


sns.barplot(x="cut",y="price",hue="color",data=df)
plt.show()