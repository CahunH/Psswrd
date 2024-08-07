# __init__.py

"""
Password Manager Package

This package provides functions for generating and managing passwords,
including key generation, password storage, and retrieval.
"""

# Optionally expose important functions for easier access
from .manager import generate_key, save_key, load_key, add_password, retrieve_password, list_passwords
