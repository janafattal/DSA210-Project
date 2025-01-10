# DSA210-Project


## Project Idea

The idea of my project is to focus on analyzing the performance and engagement metrics of my TikTok account (@studylabaii) that I manage as part of a social media marketing campaign. By studying content trends, audience behavior, and engagement patterns, the project aims to provide more insights to help me identify the influence of posting day and time on key performance metrics to improve marketing strategies and maximize the account's reach.

**Null Hypothesis:** The day of the week has no significant effect on my video performance metrics (views, likes, shares, comments)

**Alternate Hypothesis:** The day of the week has a significant effect on my video performance metrics

---

### **Data Processing**

#### **Data Collection**
- **Source**: TikTok Studio Analytics  
- **Dataset**: `Overview(2024_11_02-2025_01_06).csv` file containing performance metrics: video views, likes, comments, shares, and posting dates  
- **Objective**: Prepare and process raw data for exploratory and statistical analysis.

#### **Data Processing**
- **Loading Data:** The raw dataset was imported into a structured DataFrame using Pandas. Directory management ensured compatibility across different environments.   
- **Data Transformation**: `Date` was converted into a datetime format for extracting day-specific insights and a new column `DayOfWeek` was added to categorize the date.   
- **Metric Aggregation**: The data was grouped by `DayOfWeek` and calculated daily averages for metrics like views, likes, comments, and shares. Comprehensive visualizations were created to show trends.

#### **Outputs**
- **Data Outputs**: A cleaned and structured DataFrame summarizing daily performance metrics.  
- **Visualizations**:
   - **Boxplots**: Show metrics distributions (`video_views_boxplot.png`, `likes_boxplot.png`,`comments_boxplot.png`,`shares_boxplot.png`)  
   - **Bar Charts**: Highlight daily averages (`avg_video_views_barplot.png`, `avg_likes_barplot.png`,`avg_comments_barplot.png`, `avg_shares_barplot.png`)

#### **Key Findings**  
**Day-Specific Trends**:
   - **Weekends**: Higher engagement observed for likes and comments, indicating increased user activity.
   - **Tuesdays**: Consistently high video views, potentially linked to audience behavior.

---

### **Hypothesis Testing**

#### **Statistical Methods**
- **Chi-Square Test**: Used to evaluate associations between day of the week and performance categories
- **T-Test**: Compared weekday and weekend averages to identify significant differences in performance.

#### **Chi-Square Analysis**
**Approach**:
  1. Metrics were categorized into three groups (Low, Medium, High) using percentile thresholds with the `categorize_metric` function in `chi_square_analysis.py`.
  2. Contingency tables were created using `pandas.crosstab`.
  3. Chi-square tests were performed using `scipy.stats.chi2_contingency`.
  4. Heatmaps were generated using `Seaborn.heatmap` to visualize contingency tables.

**Results**:
   - **Video Views:** No significant association observed (p-value: 0.8199 > 0.05).
   - **Likes:** Slight trends but not statistically significant (p-value: 0.1695)
   - **Comments:** Insufficient evidence of dependence (p-value: 0.6229)
   - **Shares:** Weak association detected but not significant (p-value: 0.6478)
  
**Outputs**: Heatmaps visualizing contingency tables (`chi_square_video_views_heatmap.png`, `chi_square_video_views_heatmap.png`, `chi_square_comments_heatmap.png`, `chi_square_likes_heatmap.png`,`chi_square_shares_heatmap.png`)

**Conclusion:** The p-values indicate no statistically significant relationship between the day of the week and engagement categories

#### **T-Test Analysis**  
**Approach**:
  1. Data was split into weekdays and weekends using `t_test.py`.
  2. T-tests were performed using `scipy.stats.ttest_ind` to compare means.
  3. Visualizations were generated using `Seaborn` and saved as box plots and violin plots.

**Results**:
   - **Video Views:** Weekday Mean: 2843.7, Weekend Mean: 3125.1, t-statistic: -1.03, p-value: 0.3001 (> 0.05)
   - **Likes:** Weekday Mean: 125.4, Weekend Mean: 146.7, p-value: 0.2217
   - **Comments:** Weekday Mean: 3.2, Weekend Mean: 4.1, p-value: 0.1568
   - **Shares:** Weekday Mean: 8.9, Weekend Mean: 9.6, p-value: 0.4552

**Outputs**: Boxplots and violin plots comparing weekday vs. weekend metrics (`t_test_video_views_boxplot.png`, `t_test_comments_boxplot.png`, `t_test_likes_boxplot.png`, `t_test_shares_boxplot.png`, `t_test_video_views_violin.png`, `t_test_comments_violin.png`, `t_test_shares_violin.png`, `t_test_likes_violin.png`).

---

### **Key Findings and Insights**

#### **Insights from Chi-Square Tests:**  
No strong associations were found between the day of the week and performance metrics. This indicates that other variables (e.g., content type) likely play a more significant role.

#### **Insights from T-Tests:**
- Weekends showed slightly higher average metrics but without statistical significance. Differences between weekday and weekend performance metrics are minimal, so posting day alone is not a critical factor.

#### **Future Work Recommendations**   
- **Content Optimization**: Leverage insights about high-performing days (e.g., Tuesdays) for strategic posting.
- **Future Analysis**: Include variables like audience demographics, video duration, and hashtag usage to refine results.
- **Strategic Planning**: Conduct A/B testing on different content types to validate trends.

The findings underscore the importance of exploring other variables, such as content type, hashtags, and audience demographics, to optimize posting strategies. Future work should focus on incorporating these variables and conducting A/B testing to validate trends and refine marketing approaches. By leveraging these insights, I can develop more targeted strategies to maximize my account's reach and engagement.

---

### **Conclusion**  
In conclusion, I fail to reject the null hypothesis that the day of the week has no significant effect on my video performance metrics. The analysis does not show the influence of posting days on my TikTok's performance metrics. While there were observable trends, such as higher engagement on weekends and consistently high video views on Tuesdays, the statistical tests revealed no significant differences. This suggests that the day of the week alone is not a critical factor in driving engagement.
