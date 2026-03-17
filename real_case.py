import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 70]
}

df = pd.DataFrame(data)

df.plot(x="Name", y="Marks", kind="bar", color="orange")
plt.title("Marks using Pandas")

plt.show()