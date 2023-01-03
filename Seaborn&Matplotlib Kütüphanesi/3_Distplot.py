import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("diamonds")
print(df.head())

sns.distplot(df.price,bins=1000)#1000 adet histogram ayarlamış olduk.
plt.show()