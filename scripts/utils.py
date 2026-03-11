"""
Utility functions for Studio-NoteBookIPYNB
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any


def load_config(config_path: str = 'config/settings.json') -> Dict[str, Any]:
    """
    Load configuration from settings.json
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Dictionary with configuration settings
    """
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {config_path}")
        return {}


def list_files(directory: str, extension: str = None) -> List[str]:
    """
    List files in a directory with optional extension filter
    
    Args:
        directory: Directory path
        extension: File extension to filter (e.g., '.ipynb')
        
    Returns:
        List of file names
    """
    if not os.path.exists(directory):
        return []
    
    files = os.listdir(directory)
    if extension:
        files = [f for f in files if f.endswith(extension)]
    
    return sorted(files)


def ensure_directory(directory: str) -> bool:
    """
    Create directory if it doesn't exist
    
    Args:
        directory: Directory path to create
        
    Returns:
        True if successful, False otherwise
    """
    try:
        Path(directory).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating directory {directory}: {e}")
        return False


def format_file_size(size_bytes: int) -> str:
    """
    Format file size to human readable format
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string (e.g., '1.5 MB')
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def get_file_info(file_path: str) -> Dict[str, Any]:
    """
    Get information about a file
    
    Args:
        file_path: Path to file
        
    Returns:
        Dictionary with file information
    """
    try:
        stat = os.stat(file_path)
        return {
            'name': os.path.basename(file_path),
            'size': stat.st_size,
            'size_formatted': format_file_size(stat.st_size),
            'modified': stat.st_mtime,
            'exists': True
        }
    except FileNotFoundError:
        return {'exists': False, 'error': 'File not found'}
