"""
Data preprocessing utilities for Studio-NoteBookIPYNB
"""

import pandas as pd
import numpy as np
from typing import Tuple, List, Optional


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from CSV file
    
    Args:
        file_path: Path to CSV file
        
    Returns:
        Pandas DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows from {file_path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean data by removing duplicates and handling missing values
    
    Args:
        df: Input DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    if df is None:
        return None
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Fill missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    categorical_cols = df.select_dtypes(include=['object']).columns
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
    
    print(f"Data cleaned. Shape: {df.shape}")
    return df


def normalize_data(df: pd.DataFrame, columns: List[str] = None) -> pd.DataFrame:
    """
    Normalize numeric columns to 0-1 range
    
    Args:
        df: Input DataFrame
        columns: List of columns to normalize. If None, normalize all numeric columns
        
    Returns:
        DataFrame with normalized columns
    """
    if df is None:
        return None
    
    df_copy = df.copy()
    
    if columns is None:
        columns = df_copy.select_dtypes(include=[np.number]).columns
    
    for col in columns:
        if col in df_copy.columns:
            min_val = df_copy[col].min()
            max_val = df_copy[col].max()
            if max_val > min_val:
                df_copy[col] = (df_copy[col] - min_val) / (max_val - min_val)
    
    return df_copy


def get_statistics(df: pd.DataFrame) -> dict:
    """
    Get statistical summary of the data
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary with statistics
    """
    if df is None:
        return {}
    
    stats = {
        'rows': len(df),
        'columns': len(df.columns),
        'column_names': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'numeric_summary': df.describe().to_dict()
    }
    
    return stats


def split_data(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data into train and test sets
    
    Args:
        df: Input DataFrame
        test_size: Proportion of test data (0-1)
        random_state: Random seed for reproducibility
        
    Returns:
        Tuple of (train_df, test_df)
    """
    if df is None:
        return None, None
    
    from sklearn.model_selection import train_test_split
    
    train, test = train_test_split(df, test_size=test_size, random_state=random_state)
    print(f"Data split: {len(train)} train, {len(test)} test")
    return train, test


def aggregate_by_group(df: pd.DataFrame, group_by: str, agg_dict: dict = None) -> pd.DataFrame:
    """
    Aggregate data by grouping column
    
    Args:
        df: Input DataFrame
        group_by: Column to group by
        agg_dict: Dictionary of aggregation functions
        
    Returns:
        Aggregated DataFrame
    """
    if df is None or group_by not in df.columns:
        return None
    
    if agg_dict is None:
        # Default aggregation for numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        agg_dict = {col: 'sum' for col in numeric_cols}
    
    return df.groupby(group_by).agg(agg_dict).reset_index()
