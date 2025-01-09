import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from data_processor import load_data

def categorize_weekday_weekend(df):
    """Add weekday/weekend category to dataframe"""
    df['is_weekend'] = df['DayOfWeek'].isin(['Saturday', 'Sunday'])
    df['day_category'] = df['is_weekend'].map({True: 'Weekend', False: 'Weekday'})
    return df

def perform_t_test(weekday_data, weekend_data, metric):
    """Perform t-test and return statistics"""
    t_stat, p_value = stats.ttest_ind(weekday_data, weekend_data)
    return {
        'metric': metric,
        't_statistic': t_stat,
        'p_value': p_value,
        'weekday_mean': weekday_data.mean(),
        'weekend_mean': weekend_data.mean(),
        'weekday_std': weekday_data.std(),
        'weekend_std': weekend_data.std()
    }

def create_comparison_plots(df, metric):
    """Create visualization for weekday vs weekend comparison"""
    # 1. Box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='day_category', y=metric, data=df)
    plt.title(f'{metric}: Weekday vs Weekend Distribution')
    plt.tight_layout()
    plt.savefig(f't_test_{metric.lower().replace(" ", "_")}_boxplot.png')
    plt.close()

    # 2. Violin plot with individual points
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='day_category', y=metric, data=df)
    sns.stripplot(x='day_category', y=metric, data=df, color='red', alpha=0.3, size=4)
    plt.title(f'{metric}: Weekday vs Weekend Distribution (with data points)')
    plt.tight_layout()
    plt.savefig(f't_test_{metric.lower().replace(" ", "_")}_violin.png')
    plt.close()

def main():
    # Load and process data
    df = load_data()
    df = categorize_weekday_weekend(df)
    
    # Metrics to analyze
    metrics = ['Video views', 'Likes', 'Comments', 'Shares']
    
    # Perform t-tests and create visualizations
    results = []
    for metric in metrics:
        weekday_data = df[~df['is_weekend']][metric]
        weekend_data = df[df['is_weekend']][metric]
        
        # Perform t-test
        result = perform_t_test(weekday_data, weekend_data, metric)
        results.append(result)
        
        # Create visualizations
        create_comparison_plots(df, metric)
        
        # Print results
        print(f"\nT-Test Results for {metric}:")
        print(f"t-statistic: {result['t_statistic']:.4f}")
        print(f"p-value: {result['p_value']:.4f}")
        print(f"Weekday mean: {result['weekday_mean']:.2f}")
        print(f"Weekend mean: {result['weekend_mean']:.2f}")
        print(f"Weekday std: {result['weekday_std']:.2f}")
        print(f"Weekend std: {result['weekend_std']:.2f}")
        print("\n" + "="*50)

if __name__ == "__main__":
    main() 
