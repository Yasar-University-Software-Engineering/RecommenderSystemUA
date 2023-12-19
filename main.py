import warnings

warnings.filterwarnings('ignore')

# from IPython import get_ipython
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plotly.graph_objects as go
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors as mcolors
from scipy.stats import linregress
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.cluster import KMeans
from tabulate import tabulate
from collections import Counter

get_ipython().run_line_magic('matplotlib', 'inline')

from plotly.offline import init_notebook_mode

init_notebook_mode(connected=True)

sns.set(rc={'axes.facecolor': '#fcf0dc'}, style='darkgrid')

df = pd.read_csv('data.csv', encoding="ISO-8859-1")

# Analyzing dataset

## df.info()
## df.decsribe().T
## df.describe(include = 'object').T

# DATA CLEANING AND TRANSFORMATION

missingData = df.isnull().sum()
missingPercentage = (missingData[missingData > 0] / df.shape[0]) * 100
missingPercentage.sort_values(ascending=True, inplace=True)

fig, ax = plt.subplots(figsize=(15, 4))
ax.barh(missingPercentage.index, missingPercentage, color='red')

for i, (value, name) in enumerate(zip(missingPercentage, missingPercentage.index)):
    ax.text(value + 0.5, i, f"{value:.2f}%", ha='left', va='center', fontweight='bold', fontsize=18, color='black')

ax.set_xlim([0, 40])

plt.title("Percentage of Missing Values", fontweight='bold', fontsize=22)
plt.xlabel('Percentages (%)', fontsize=16)
plt.show()

df[df['CustomerID'].isnull() | df['Description'].isnull()].head()

df = df.dropna(subset=['CustomerID', 'Description'])

duplicateRows = df[df.duplicated(keep=False)]
duplicateRowsSorted = duplicateRows.sort_values(by=['InvoiceNo', 'StockCode', 'Description', 'CustomerID', 'Quantity'])

df.shape[0]

df['Transaction_Status'] = np.where(df['InvoiceNo'].astype(str).str.startswith('C'), 'Cancelled', 'Completed')

cancelledTransactions = df[df['Transaction_Status'] == 'Cancelled']
cancelledTransactions.describe().drop('CustomerID', axis=1)

df.drop_duplicates(inplace=True)

cancelledPercentage = (cancelledTransactions.shape[0] / df.shape[0]) * 100
# %2.21

unique_stock_codes = df['StockCode'].nunique()  #3684

top10StockCodes = df['StockCode'].value_counts(normalize=True).head(10) * 100

plt.figure(figsize=(12, 5))
top10StockCodes.plot(kind='barh', color='darkblue')

for index, value in enumerate(top10StockCodes):
    plt.text(value, index + 0.25, f'{value:.2f}%', fontsize=10)

plt.title('Top 10 Stock Codes')
plt.xlabel('Percentage Frequency (%)')
plt.ylabel('Stock Codes')
plt.gca().invert_yaxis()
plt.show()

uniqueStockCodes = df['StockCode'].unique()
uniqueNumericCharCount = pd.Series(uniqueStockCodes).apply(lambda x: sum(c.isdigit() for c in str(x))).value_counts()

print("Value counts of numeric character frequencies in unique stock codes:")
print("-" * 70)
print(uniqueNumericCharCount)

anomalousStockCodes = [code for code in uniqueStockCodes if sum(c.isdigit() for c in str(code)) in (0, 1)]

print("Anomalous stock codes:")
print("-" * 22)
for code in anomalousStockCodes:
    print(code)

percentageAnomalous = (df['StockCode'].isin(anomalousStockCodes).sum() / len(df)) * 100
# %0.48


df = df[~df['StockCode'].isin(anomalousStockCodes)]
df.shape[0]

descriptionCounts = df['Description'].value_counts()

top30Descriptions = descriptionCounts[:30]

plt.figure(figsize=(12, 8))
plt.barh(top30Descriptions.index[::-1], top30Descriptions.values[::-1], color='#ff6200')

plt.xlabel('Number of Occurrences')
plt.ylabel('Description')
plt.title('Top 30 Most Frequent Descriptions')
plt.show()

serviceRelatedDescriptions = ["Next Day Carriage", "High Resolution Image"]
serviceRelatedPercentage = df[df['Description'].isin(serviceRelatedDescriptions)].shape[0] / df.shape[0] * 100
# %0.02
df = df[~df['Description'].isin(serviceRelatedDescriptions)]

df['Description'] = df['Description'].str.upper()

df.shape[0]

df[df['UnitPrice'] == 0].describe()[['Quantity']]

df = df[df['UnitPrice'] > 0]

df.reset_index(drop=True, inplace=True)
df.shape[0]

# DATA FEATURES

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['InvoiceDay'] = df['InvoiceDate'].dt.date

customerData = df.groupby('CustomerID')['InvoiceDay'].max().reset_index()

mostRecentDate = df['InvoiceDay'].max()

customerData['InvoiceDay'] = pd.to_datetime(customerData['InvoiceDay'])
mostRecentDate = pd.to_datetime(mostRecentDate)

customerData['Days_Since_Last_Purchase'] = (mostRecentDate - customerData['InvoiceDay']).dt.days

customerData.drop(columns=['InvoiceDay'], inplace=True)
customerData.head()

total_transactions = df.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()
total_transactions.rename(columns={'InvoiceNo': 'Total_Transactions'}, inplace=True)

total_purchased_products = df.groupby('CustomerID')['Quantity'].sum().reset_index()
total_purchased_products.rename(columns={'Quantity': 'Total_Products_Purchased'}, inplace=True)

customerData = pd.merge(customerData, total_transactions, on='CustomerID')
customerData = pd.merge(customerData, total_purchased_products, on='CustomerID')

customerData.head()

df['Total_Spend'] = df['UnitPrice'] * df['Quantity']
total_spend = df.groupby('CustomerID')['Total_Spend'].sum().reset_index()

average_transaction_value = total_spend.merge(total_transactions, on='CustomerID')
average_transaction_value['Average_Transaction_Value'] = average_transaction_value['Total_Spend'] / \
                                                         average_transaction_value['Total_Transactions']

customerData = pd.merge(customerData, total_spend, on='CustomerID')
customerData = pd.merge(customerData, average_transaction_value[['CustomerID', 'Average_Transaction_Value']],
                        on='CustomerID')
customerData.head()

unique_products_purchased = df.groupby('CustomerID')['StockCode'].nunique().reset_index()
unique_products_purchased.rename(columns={'StockCode': 'Unique_Products_Purchased'}, inplace=True)

customerData = pd.merge(customerData, unique_products_purchased, on='CustomerID')
customerData.head()

df['Day_Of_Week'] = df['InvoiceDate'].dt.dayofweek
df['Hour'] = df['InvoiceDate'].dt.hour

days_between_purchases = df.groupby('CustomerID')['InvoiceDay'].apply(
    lambda x: (x.diff().dropna()).apply(lambda y: y.days))
average_days_between_purchases = days_between_purchases.groupby('CustomerID').mean().reset_index()
average_days_between_purchases.rename(columns={'InvoiceDay': 'Average_Days_Between_Purchases'}, inplace=True)

favorite_day_of_shopping = df.groupby(['CustomerID', 'Day_Of_Week']).size().reset_index(name='Count')
favorite_day_of_shopping = \
    favorite_day_of_shopping.loc[favorite_day_of_shopping.groupby('CustomerID')['Count'].idxmax()][
        ['CustomerID', 'Day_Of_Week']]

favorite_hour_of_shopping = df.groupby(['CustomerID', 'Hour']).size().reset_index(name='Count')
favorite_hour_of_shopping = \
    favorite_hour_of_shopping.loc[favorite_hour_of_shopping.groupby('CustomerID')['Count'].idxmax()][
        ['CustomerID', 'Hour']]

customerData = pd.merge(customerData, average_days_between_purchases, on='CustomerID')
customerData = pd.merge(customerData, favorite_day_of_shopping, on='CustomerID')
customerData = pd.merge(customerData, favorite_hour_of_shopping, on='CustomerID')
customerData.head()

customer_country = df.groupby(['CustomerID', 'Country']).size().reset_index(name='Number_of_Transactions')
customer_main_country = customer_country.sort_values('Number_of_Transactions', ascending=False).drop_duplicates(
    'CustomerID')

customer_main_country['Is_UK'] = customer_main_country['Country'].apply(lambda x: 1 if x == 'United Kingdom' else 0)

customerData = pd.merge(customerData, customer_main_country[['CustomerID', 'Is_UK']], on='CustomerID', how='left')

customerData.head()

customerData['Is_UK'].value_counts()

total_transactions = df.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()

cancelled_transactions = df[df['Transaction_Status'] == 'Cancelled']
cancellation_frequency = cancelled_transactions.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()
cancellation_frequency.rename(columns={'InvoiceNo': 'Cancellation_Frequency'}, inplace=True)

customerData = pd.merge(customerData, cancellation_frequency, on='CustomerID', how='left')

customerData['Cancellation_Frequency'].fillna(0, inplace=True)

customerData['Cancellation_Rate'] = customerData['Cancellation_Frequency'] / total_transactions['InvoiceNo']

customerData.head()

df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month

monthly_spending = df.groupby(['CustomerID', 'Year', 'Month'])['Total_Spend'].sum().reset_index()

seasonal_buying_patterns = monthly_spending.groupby('CustomerID')['Total_Spend'].agg(['mean', 'std']).reset_index()
seasonal_buying_patterns.rename(columns={'mean': 'Monthly_Spending_Mean', 'std': 'Monthly_Spending_Std'}, inplace=True)

seasonal_buying_patterns['Monthly_Spending_Std'].fillna(0, inplace=True)


def calculate_trend(spend_data):
    if len(spend_data) > 1:
        x = np.arange(len(spend_data))
        slope, _, _, _, _ = linregress(x, spend_data)
        return slope
    else:
        return 0


spending_trends = monthly_spending.groupby('CustomerID')['Total_Spend'].apply(calculate_trend).reset_index()
spending_trends.rename(columns={'Total_Spend': 'Spending_Trend'}, inplace=True)

customerData = pd.merge(customerData, seasonal_buying_patterns, on='CustomerID')
customerData = pd.merge(customerData, spending_trends, on='CustomerID')

customerData.head()

customerData['CustomerID'] = customerData['CustomerID'].astype(str)
customerData = customerData.convert_dtypes()
customerData.head()

customerData.info()

# Dealing with Outliers

model = IsolationForest(contamination=0.05, random_state=0)
customerData['Outliers'] = model.fit_predict(customerData.iloc[:, 1:].to_numpy())
customerData['Is_Outlier'] = [1 if
                              x == -1
                              else
                              0
                              for x in customerData['Outliers']]
customerData.head()

outlierPercentage = customerData['Outliers'].value_counts(normalize=True) * 100
plt.figure(figsize=(12, 4))
outlierPercentage.plot(kind='barh', color='red')
for i, val in enumerate(outlierPercentage):
    plt.text(val, i, f'{val:.2f}%', fontsize=15)

    plt.title('Inliers and Outliers')
    plt.xticks(ticks=np.arange(0, 115, 5))
    plt.xlabel('Percentage')
    plt.ylabel('Is Outlier')
    plt.gca().invert_yaxis()
    plt.show()

outliersData = customerData[customerData['Is_Outlier'] == 1]

customerDataCleaned = customerData[customerData['Is_Outlier'] == 0]

customerDataCleaned = customerDataCleaned.drop(columns=['Outliers', 'Is_Outlier'])

customerDataCleaned.reset_index(drop=True, inplace=True)
# 4067


# Correlation Checking

sns.set_style('whitegrid')
corr = customerDataCleaned.drop(columns=['CustomerID']).corr()

colors = ['red', '#ffcaa8', 'white', '#ffcaa8', '#ff6200']
my_cmap = LinearSegmentedColormap.from_list('custom_map', colors, N=256)

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask, k=1)] = True

plt.figure(figsize=(12, 10))
sns.heatmap(corr, mask=mask, cmap=my_cmap, annot=True, center=0, fmt='.2f', linewidths=2)
plt.title('Correlation Matrix', fontsize=14)
plt.show()

# Feature Scaling

scaler = StandardScaler()

columnsToExclude = ['CustomerID', 'Is_UK', 'Day_Of_Week']

columnsToScale = customerDataCleaned.columns.difference(columnsToExclude)

customerDataScaled = customerDataCleaned.copy()

customerDataScaled[columnsToScale] = scaler.fit_transform(customerDataScaled[columnsToScale])

customerDataScaled.head()

# Dimensionality Reducing

customerDataScaled.set_index('CustomerID', inplace=True)

pca = PCA().fit(customerDataScaled)

explainedVarianceRatio = pca.explained_variance_ratio_
cumulativeExplainedVariance = np.cumsum(explainedVarianceRatio)

optimal_k = 6

sns.set(rc={'axes.facecolor': '#fcf0dc'}, style='darkgrid')

plt.figure(figsize=(20, 10))

barplot = sns.barplot(x=list(range(1, len(cumulativeExplainedVariance) + 1)),
                      y=explained_variance_ratio,
                      color='#fcc36d',
                      alpha=0.8)

lineplot, = plt.plot(range(0, len(cumulativeExplainedVariance)), cumulativeExplainedVariance,
                     marker='o', linestyle='--', color='#ff6200', linewidth=2)

optimal_k_line = plt.axvline(optimal_k - 1, color='red', linestyle='--', label=f'Optimal k value = {optimal_k}')

plt.xlabel('Number of Components', fontsize=14)
plt.ylabel('Explained Variance', fontsize=14)
plt.title('Cumulative Variance vs. Number of Components', fontsize=18)

plt.xticks(range(0, len(cumulativeExplainedVariance)))
plt.legend(handles=[barplot.patches[0], lineplot, optimal_k_line],
           labels=['Explained Variance of Each Component', 'Cumulative Explained Variance',
                   f'Optimal k value = {optimal_k}'],
           loc=(0.62, 0.1),
           frameon=True,
           framealpha=1.0,
           edgecolor='#ff6200')

x_offset = -0.3
y_offset = 0.01
for i, (ev_ratio, cum_ev_ratio) in enumerate(zip(explainedVarianceRatio, cumulativeExplainedVariance)):
    plt.text(i, ev_ratio, f"{ev_ratio:.2f}", ha="center", va="bottom", fontsize=10)
    if i > 0:
        plt.text(i + x_offset, cum_ev_ratio + y_offset, f"{cum_ev_ratio:.2f}", ha="center", va="bottom", fontsize=10)

plt.grid(axis='both')
plt.show()

pca = PCA(n_components=6)
customerDataPCA = pca.fit_transform(customerDataScaled)
customerDataPCA = pd.DataFrame(customerDataPCA, columns=['PC' + str(i + 1) for i in range(pca.n_components_)])

customerDataPCA.index = customerDataScaled.index
customerDataPCA.head()
