"""A simple Matplotlib script to plot a sine wave."""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# ----------------------------------------------


# Line Chart (Line Graph) Jab time ke sath data change ho raha ho (growth, trend)
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [10, 20, 15, 30, 25]

plt.plot(days, sales)
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Daily Sales Report")
plt.show()

# Multiple Lines on Same Graph Comparison ke liye (different products ka sales)

months = np.arange(1, 13)
product_a = [45, 52, 48, 61, 70, 75, 82, 88, 85, 90, 95, 102]
product_b = [30, 35, 40, 45, 55, 60, 58, 62, 68, 72, 78, 85]
product_c = [20, 22, 25, 28, 32, 35, 40, 42, 45, 48, 50, 55]

plt.figure(figsize=(12, 6))

plt.plot(months, product_a, 'o-', label='Product A', color='#E74C3C', linewidth=2)
plt.plot(months, product_b, 's--', label='Product B', color='#3498DB', linewidth=2)
plt.plot(months, product_c, '^:', label='Product C', color='#27AE60', linewidth=2)

plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Product Sales Comparison')
plt.legend(loc='upper left')
plt.xticks(months)
plt.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()

# ----------------------------------------------

# Bar Chart (Bar Graph) Comparison ke liye use hota hai (students marks, product sales)


students = ["Ali", "Ahmed", "Sara", "Ayesha"]
marks = [85, 90, 78, 88]

plt.bar(students, marks)
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# more advanced bar chart with multiple bars

# Data
categories = ['Engineering', 'Marketing', 'Sales', 'Support', 'HR']
q1 = [120, 80, 95, 60, 40]
q2 = [135, 90, 110, 65, 45]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(x - width/2, q1, width, label='Q1', color='#3498DB')
bars2 = ax.bar(x + width/2, q2, width, label='Q2', color='#E74C3C')

# Add value labels on bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

add_labels(bars1)
add_labels(bars2)

ax.set_ylabel('Budget ($K)')
ax.set_title('Department Budgets by Quarter')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

plt.tight_layout()
plt.show()


# ----------------------------------------------

# Pie Chart Percentage ya proportion show karne ke liye

languages = ["Python", "JavaScript", "C++", "Java"]
usage = [40, 30, 15, 15]

plt.pie(usage, labels=languages, autopct="%1.0f%%")
plt.title("Programming Language Usage")
plt.show()

# ----------------------------------------------

# Scatter Plot Relationship dikhane ke liye (2 values ke darmiyan)

hours = [1, 2, 3, 4, 5]
marks = [40, 50, 65, 70, 85]

plt.scatter(hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study vs Marks")
plt.show()

# ----------------------------------------------
