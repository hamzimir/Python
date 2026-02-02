""""
Python Data Visualization kya hoti hai?

Data Visualization ka matlab hai data ko graphs / charts ki form mein dikhana, taake:

Data asaani se samajh aaye

Patterns, trends, comparison nazar aaye

Decision lena easy ho jaye

Jaise:
Numbers ki list dekhna mushkil hota hai, lekin graph dekh kar turant idea mil jata hai 📊

🔹 Python mein Data Visualization kyun use hoti hai?

Data analysis ke liye

Reports aur dashboards ke liye

Machine Learning se pehle data samajhne ke liye

Business decisions ke liye

🔹 Python ki popular visualization libraries

Python mein mostly yeh libraries use hoti hain:

1 Matplotlib (basic & powerful)
2 Seaborn (beautiful & statistical graphs)
3 Plotly (interactive graphs)
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)  # line plot
plt.xlabel("Days") # represent x-axis label
plt.ylabel("Sales") # represent y-axis label
plt.title("Daily Sales Report") # represent title
plt.plot(x, y, label="Sales") # represent legend (label name)
plt.legend()
plt.grid(True) # show grid
plt.xlim(0, 6) # set x-axis limits
plt.ylim(0, 40) # set y-axis limits
plt.xticks([1, 2, 3, 4, 5]) # set x-axis ticks
plt.yticks([0, 10, 20, 30, 40]) # set y-axis ticks
# plt.figure(figsize=(5, 9)) # set figure size
# plt.style.use("ggplot") # set style
plt.plot(x, y, color="red", linestyle="--", linewidth=2, marker="o") # customize line
plt.bar(x, y, color="green", width=0.5) # bar plot
plt.scatter(x, y, color="blue", s=100) # scatter plot
plt.text(3, 25, "Peak Sales") # add text annotation
plt.annotate( 
    "Highest Sale",
    xy=(4, 30),
    xytext=(2, 35),
    arrowprops=dict(arrowstyle="->", color="blue"),
) # add arrow annotation
plt.tight_layout() # adjust layout
plt.savefig("sales.png") # save plot as image
plt.show() # show plot
