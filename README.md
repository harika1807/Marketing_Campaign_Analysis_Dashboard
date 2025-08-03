# 📊 Marketing Campaign Analysis Dashboard

![Banner](banner.jpeg)

## Overview
This project provides a dashboard to analyze a marketing campaign's performance using data from user impressions, item data, and view logs. It calculates the overall Click-Through Rate (CTR), explores app usage patterns, device types, and viewing behavior over time.

## Features
- Calculates overall CTR from `train.csv`
- Visualizes clicks by app code
- Analyzes device type distribution
- Displays trends of item views over time

## Dataset Files
- `train.csv`: Contains impression data like `impression_id`, `impression_time`, `user_id`, `app_code`, `os_version`, `is_4G`, `is_click`.
- `item_data.csv`: Describes item metadata such as `item_id`, `item_price`, `category_1`, `category_2`, `category_3`, and `product_type`.
- `view_log.csv`: Logs user interaction with `serve_time`, `device_type`, `session_id`, `user_id`, `item_id`.

## Output Files
- `clicks_by_app_code.png`: Bar chart of click counts per app code
- `device_type_distribution.png`: Pie chart showing the device type breakdown
- `views_over_time.png`: Time series of views over days

## Technologies Used
- Python 🐍
- Pandas 🐼
- Matplotlib 📈

## How to Run
1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Place your CSV files in the same directory
4. Run: `python marketing_campaign_analysis.py`

✅ All visualizations will be saved as image files.

---
**Author**: Harika Devi  
**Project for Learning and Resume Building**

