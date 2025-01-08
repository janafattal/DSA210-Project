import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Load and process data
def load_data():
    # Get the current directory and construct the correct path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    file_path = os.path.join(parent_dir, 'Overview(2024_11_02-2025_01_06).csv')
    
    # Load the Overview data
    df = pd.read_csv(file_path)
    
    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')
    
    # Add day of week
    df['DayOfWeek'] = df['Date'].dt.day_name()
    
    # Ensure proper day order
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['DayOfWeek'] = pd.Categorical(df['DayOfWeek'], categories=day_order, ordered=True)
    
    return df

def calculate_daily_metrics(df):
    # Group by day of week and calculate means
    daily_metrics = df.groupby('DayOfWeek', observed=True).agg({
        'Video views': 'mean',
        'Likes': 'mean',
        'Comments': 'mean',
        'Shares': 'mean'
    }).round(2)
    
    return daily_metrics

def create_performance_plots(df):
    # Set style for better visualization
    sns.set_theme(style="whitegrid")
    
    metrics = ['Video views', 'Likes', 'Comments', 'Shares']
    
    # 1. Box plots for each metric
    for metric in metrics:
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='DayOfWeek', y=metric, data=df)
        plt.title(f'{metric} Distribution by Day of Week')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{metric.lower().replace(" ", "_")}_boxplot.png')
        plt.close()
    
    # 2. Bar plot of average metrics
    daily_avg = calculate_daily_metrics(df)
    
    for metric in metrics:
        plt.figure(figsize=(12, 6))
        ax = daily_avg[metric].plot(kind='bar', color='skyblue')
        plt.title(f'Average {metric} by Day of Week')
        plt.xlabel('Day of Week')
        plt.ylabel(metric)
        plt.xticks(rotation=45)
        
        # Add value labels on top of each bar
        for i, v in enumerate(daily_avg[metric]):
            ax.text(i, v, f'{v:.1f}', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.savefig(f'avg_{metric.lower().replace(" ", "_")}_barplot.png')
        plt.close()

def main():
    # Load and process data
    df = load_data()
    
    # Calculate daily metrics
    daily_metrics = calculate_daily_metrics(df)
    print("\nDaily Metrics Summary:")
    print(daily_metrics)
    
    # Create visualizations
    create_performance_plots(df)
    print("\nPlots have been saved in the current directory.")

if __name__ == "__main__":
    main() 
