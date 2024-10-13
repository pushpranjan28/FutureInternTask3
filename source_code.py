import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\LENOVO\Desktop\FI Internship\DA_03\Iris.csv")
print(df.head())
plt.figure(figsize=(12, 8))
# 1. Sepal Length
plt.subplot(2, 2, 1)
plt.hist(df['SepalLengthCm'], bins=10, color='blue', edgecolor='black')
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
# 2. Sepal Width
plt.subplot(2, 2, 2)
plt.hist(df['SepalWidthCm'], bins=10, color='green', edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
# 3. Petal Length
plt.subplot(2, 2, 3)
plt.hist(df['PetalLengthCm'], bins=10, color='red', edgecolor='black')
plt.title('Histogram of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
# 4. Petal Width
plt.subplot(2, 2, 4)
plt.hist(df['PetalWidthCm'], bins=10, color='purple', edgecolor='black')
plt.title('Histogram of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()