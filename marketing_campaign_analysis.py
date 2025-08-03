import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
train_df = pd.read_csv('data/train.csv')
item_data_df = pd.read_csv('data/item_data.csv')
view_log_df = pd.read_csv('data/view_log.csv')

# -------------------------
# CTR Analysis
# -------------------------
total_clicks = train_df['is_click'].sum()
total_impressions = train_df.shape[0]
ctr = (total_clicks / total_impressions) * 100
print(f"Overall Click-Through Rate (CTR): {ctr:.2f}%")

# -------------------------
# Clicks by App Code - Bar Chart
# -------------------------
clicks_by_app = train_df[train_df['is_click'] == 1]['app_code'].value_counts()
plt.figure(figsize=(10, 6))
clicks_by_app.plot(kind='bar', color='skyblue')
plt.title('Number of Clicks by App Code')
plt.xlabel('App Code')
plt.ylabel('Clicks')
plt.tight_layout()
plt.savefig("clicks_by_app_code.png")
plt.close()
print("Saved: clicks_by_app_code.png")

# -------------------------
# Device Type Distribution - Pie Chart
# -------------------------
device_counts = view_log_df['device_type'].value_counts()
plt.figure(figsize=(8, 8))
device_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Device Type Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig("device_type_distribution.png")
plt.close()
print("Saved: device_type_distribution.png")

# -------------------------
# Views Over Time - Line Plot
# -------------------------
view_log_df['server_time'] = pd.to_datetime(view_log_df['server_time'])
view_log_df['date'] = view_log_df['server_time'].dt.date
views_over_time = view_log_df['date'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
views_over_time.plot(kind='line', marker='o')
plt.title('Number of Views Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Views')
plt.grid(True)
plt.tight_layout()
plt.savefig("views_over_time.png")
plt.close()
print("Saved: views_over_time.png")

# -------------------------
# Finish
# -------------------------
print("\n✅ All visualizations saved successfully!")
