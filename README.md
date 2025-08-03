# 📊 Marketing Campaign Analysis Dashboard

![Banner](banner.jpeg)

## 🧠 Overview

The **Marketing Campaign Analysis Dashboard** is a Python-based analytics solution that processes marketing campaign data to extract actionable insights. It calculates performance metrics and generates visualizations to support decision-making in campaign strategy.

---

## 📂 Dataset Details

You need the following `.csv` files in your project directory:

### 1. `train.csv`
Contains data on ad impressions and clicks.

| Column           | Description                      |
|------------------|----------------------------------|
| `impression_id`  | Unique ID of impression          |
| `impression_time`| Timestamp of impression          |
| `user_id`        | Unique user ID                   |
| `app_code`       | App code where ad was served     |
| `os_version`     | OS version of device             |
| `is_4G`          | Whether device used 4G network   |
| `is_click`       | 1 if clicked, 0 if not           |

### 2. `item_data.csv`
Details about advertised items.

| Column         | Description                         |
|----------------|-------------------------------------|
| `item_id`      | Unique ID of the item               |
| `item_price`   | Price of the item                   |
| `category_1`   | Primary category                    |
| `category_2`   | Secondary category                  |
| `category_3`   | Tertiary category                   |
| `product_type` | Type of product                     |

### 3. `view_log.csv`
Log of user item views.

| Column         | Description                         |
|----------------|-------------------------------------|
| `serve_time`   | Timestamp of view                   |
| `device_type`  | Type of device (e.g., mobile, tablet)|
| `session_id`   | Session ID                          |
| `user_id`      | User ID                             |
| `item_id`      | ID of the viewed item               |

---

## 📐 Click-Through Rate (CTR)

CTR measures how effective your campaign is in generating clicks.

**Formula:**

\[
\text{CTR (\%)} = \left( \frac{\text{Total Clicks}}{\text{Total Impressions}} \right) \times 100
\]

Where:
- `Total Clicks` = Number of records where `is_click == 1`
- `Total Impressions` = Total records in `train.csv`

---

## 📊 Output Visualizations (Auto-Saved)

After running the script, the following charts are saved as `.png`:

| File Name                    | Description                            |
|-----------------------------|----------------------------------------|
| `clicks_by_app_code.png`    | Bar chart of clicks grouped by app     |
| `device_type_distribution.png` | Pie chart showing device usage     |
| `views_over_time.png`       | Line chart showing views over days     |

Each plot is saved automatically — no display window is shown.

---

## 🚀 How to Run the Project

### 1. Clone this Repo or Download Files

Make sure the following are in the same folder:
- `marketing_campaign_analysis.py`
- `train.csv`, `item_data.csv`, `view_log.csv`
- `banner.jpeg` (optional for display)
- This `README.md`

### 2. Install Required Libraries

```bash
pip install pandas matplotlib
```

### 3. Run the Script

```bash
python marketing_campaign_analysis.py
```

---

## 🖥 Requirements 

```text
pandas
matplotlib
```

---

## 📦 Files You Should See After Execution

| File Name                        | Purpose                             |
|----------------------------------|-------------------------------------|
| `marketing_campaign_analysis.py` | Main analysis code                  |
| `clicks_by_app_code.png`         | Saved chart for app click analysis  |
| `device_type_distribution.png`   | Saved chart for device distribution |
| `views_over_time.png`            | Saved time series view chart        |
| `banner.jpeg`                    | Project banner (used in README)     |
| `README.md`                      | This documentation                  |

---

## 🧠 Insights You Can Derive

-Which apps generated the most clicks
-Device preferences of users
-Viewing behavior over time
-Overall ad engagement rate (CTR)

---

## 👩‍💻 Author

Seelam Harika Devi
B.Tech CSE | Curious about Analytics & Visualization

📌 "Turning raw data into real insights, one visualization at a time."

---

## 🔗 License

This project is open-source and intended for learning, academic, and personal project use. Feel free to fork and build upon it.

---
