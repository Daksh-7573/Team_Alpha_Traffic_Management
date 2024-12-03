# Import libraries
import matplotlib.pyplot as plt
import pandas as pd

# Take .csv file as input
Trafficdata = pd.read_csv(r"FILE PATH")
print(Trafficdata)

# --- GRAPH 1 ---
# Group data together
group_data1 = Trafficdata.groupby(['Year', 'Transportation'])['Total'].sum().unstack()

# Make graph
group_data1.plot(kind='bar', figsize=(10,5), colormap='viridis')

# Formating the bar chart
plt.title('Type of Vehical accidents per year')
plt.xlabel('Year')
plt.ylabel('No. of acccidents')
plt.grid(True)
plt.xticks(rotation=0, ha='right')

# Output graph
plt.show()

# --- GRAPH 2 ---

# Scatter plot to show transportation method and accident injuries type
plt.scatter(Trafficdata['Year and Transportation'], Trafficdata["Fatal"], color='black', marker="x")
plt.scatter(Trafficdata['Year and Transportation'], Trafficdata["Hospitalisation"], color='red', marker='x')
plt.scatter(Trafficdata['Year and Transportation'], Trafficdata["No Hospitalisation"], color='orange', marker='x' )
plt.scatter(Trafficdata['Year and Transportation'], Trafficdata["No Injury"], color='green', marker='x' )

# Format of scatter plot
plt.title('Transportation - Injury Graph')
plt.xlabel('Transportation mode')
plt.ylabel('Year of Injury')
plt.grid(True)

# Rotate labels by 45 deg to prevent label overlap
plt.xticks(rotation=45, ha='right')
plt.show()
