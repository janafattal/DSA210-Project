import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import os
from data_processor import load_data

def categorize_metric(series):
    """Categorize metrics into Low, Medium, High based on percentiles"""
    low = series.quantile(0.33)
    high = series.quantile(0.66)
    
    conditions = [
        (series < low),
        (series >= low) & (series < high),
        (series >= high)
    ]
    choices = ['Low', 'Medium', 'High']
    return pd.Series(np.select(conditions, choices), index=series.index)

def perform_chi_square_test(df, metric):
    """Perform chi-square test and create visualization for a metric"""
    # Categorize the metric
    df[f'{metric}_Category'] = categorize_metric(df[metric])
    
    # Create contingency table
    contingency_table = pd.crosstab(df['DayOfWeek'], df[f'{metric}_Category'])
    
    # Perform chi-square test
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    
    # Create heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(contingency_table, annot=True, fmt='d', cmap='YlOrRd')
    plt.title(f'Chi-Square Test Heatmap: {metric} vs Day of Week\np-value: {p_value:.4f}')
    plt.tight_layout()
    plt.savefig(f'chi_square_{metric.lower().replace(" ", "_")}_heatmap.png')
    plt.close()
    
    return {
        'metric': metric,
        'chi2': chi2,
        'p_value': p_value,
        'dof': dof,
        'contingency_table': contingency_table
    }

def main():
    # Load data
    df = load_data()
    
    # Metrics to analyze
    metrics = ['Video views', 'Likes', 'Comments', 'Shares']
    
    # Perform chi-square tests and create visualizations
    results = []
    for metric in metrics:
        result = perform_chi_square_test(df, metric)
        results.append(result)
        
        # Print results
        print(f"\nChi-Square Test Results for {metric}:")
        print(f"Chi-square statistic: {result['chi2']:.2f}")
        print(f"p-value: {result['p_value']:.4f}")
        print(f"Degrees of freedom: {result['dof']}")
        print("\nContingency Table:")
        print(result['contingency_table'])
        print("\n" + "="*50)

if __name__ == "__main__":
    main() 
