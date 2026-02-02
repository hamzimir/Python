import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

sns.lineplot(x=x, y=y)
plt.title("Seaborn Line Plot")
plt.show()

# Seaborn Bar Plot

names = ["Ali", "Ahmed", "Sara"]
scores = [80, 90, 85]

sns.barplot(x=names, y=scores)
plt.title("Seaborn Bar Chart")
plt.show()

# Monthly Expenses Visualization
import matplotlib.pyplot as plt

categories = ["Rent", "Food", "Transport", "Shopping"]
expenses = [20000, 10000, 5000, 7000]

plt.bar(categories, expenses)
plt.title("Monthly Expenses")
plt.ylabel("Amount (PKR)")
plt.show()
