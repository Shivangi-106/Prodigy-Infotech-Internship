import os

def ensure_directories():
    os.makedirs('output/charts', exist_ok=True)
    os.makedirs('output/maps', exist_ok=True)
    os.makedirs('output/logs', exist_ok=True)
