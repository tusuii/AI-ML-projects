# Import necessary libraries

```python
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns
```
# Load your CSV data
```python
df = pd.read_csv('your_data.csv')
```
# 1. Check Data Dimensions
```python
num_rows, num_columns = df.shape
```
# 2. View the First Few Rows
```python
df.head()
```

# 3. Data Types
```python
data_types = df.dtypes
```
# 4. Missing Values
```python
missing_values = df.isnull().sum()
```
# 5. Summary Statistics
```python
summary_stats = df.describe()
```
# 6. Unique Values
```python
unique_values = df['Category'].value_counts()
```
# 7. Data Distribution (Histogram)
```python
plt.hist(df['Age'], bins=20)
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.show()
```
# 8. Categorical Data (Bar Chart)
```python
sns.countplot(x='Category', data=df)
```
# 9. Correlation Matrix
```python
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
```
# 10. Outliers Detection (Box Plot)
```python
sns.boxplot(x='Salary', data=df)
```
# 11. Feature Relationships (Scatter Plot)
```python
plt.scatter(df['Age'], df['Income'])
plt.xlabel('Age')
plt.ylabel('Income')
```
# 12. Feature Engineering
```python
df['Total_Score'] = df['Math_Score'] + df['English_Score']
```
# 13. Time Series Analysis
```python
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df['Sales'].plot()
```

# 14. Geospatial Analysis (Sample: World Map)
```python
import geopandas as gpd
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot()
```
# 15. Hypothesis Testing (T-test)
```python
from scipy import stats
group1 = df[df['Group'] == 'A']['Value']
group2 = df[df['Group'] == 'B']['Value']
t_stat, p_value = stats.ttest_ind(group1, group2)
```
# 16. Data Visualization (Scatter Plot with Color)
```python
plt.scatter(df['X'], df['Y'], c=df['Category'])
plt.xlabel('X')
plt.ylabel('Y')
```
# 17. Grouping and Aggregation (Mean by Category)
```python
grouped = df.groupby('Category')['Value'].mean()
```
# 18. Data Transformation (Scaling)
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['Scaled_Value'] = scaler.fit_transform(df[['Value']])
```
# 19. Time Series Decomposition (Seasonal Decomposition)
```python
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['Sales'], model='additive')
result.plot()
```
# 20. Text Data Exploration (Word Cloud)
```python
from wordcloud import WordCloud
wordcloud = WordCloud().generate(' '.join(df['Text']))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
```
# 21. Handling Date-Time Data (Resampling)
```python
df.resample('M').mean()
```
# 22. Handling Categorical Data (Encoding)
```python
df_encoded = pd.get_dummies(df, columns=['Category'], drop_first=True)
```
# 23. Dimensionality Reduction (PCA)
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(df[['Feature1', 'Feature2']])
df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
```
# 24. Time Series Rolling Statistics
```python
rolling_mean = df['Sales'].rolling(window=30).mean()
```
# 25. Statistical Tests for Non-Normality (Shapiro-Wilk Test)
```python
from scipy.stats import shapiro
stat, p = shapiro(df['Value'])
```

# 26. Visualization of Distributions (Kernel Density Plot)
```python
sns.kdeplot(df['Age'], shade=True)
```

# 27. Handling Imbalanced Data (Resampling)
```python
from sklearn.utils import resample
df_minority = df[df['Class'] == 'Minority']
df_majority = df[df['Class'] == 'Majority']
df_minority_upsampled = resample(df_minority, replace=True, n_samples=len(df_majority))
```

# 28. Time Series Autocorrelation (ACF and PACF Plots)
```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_acf(df['Sales'])
plot_pacf(df['Sales'])
```

# 29. Bivariate Analysis (Two-Dimensional KDE Plot)
```python
sns.kdeplot(df['Age'], df['Income'], cmap='Blues', shade=True)
```
# 30. Handling Multicollinearity (VIF)
```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = pd.DataFrame()
vif["Variable"] = df.columns

vif["VIF"] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
```
