import matplotlib.pyplot as plt

counts=[111,120,222,300,200,150]
members=["students","beginers","seniors","bussiness owners","teachers","others"]
colors=["red","green","blue","lightblue","cyan","pink"]
plt.pie(counts,labels=members,
            autopct="%1.2f%%",
            colors=colors,
            explode=[0,0.2,0,0,0,0.2],
            shadow=True)
plt.title("Student details")
plt.show()
