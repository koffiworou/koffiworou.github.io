#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

scripts = [
    "download_weather_maps.py",
    #"download_hurricane_products.py",
    #"download_cpc_products.py",
    #"update_enso.py",
    #"update_atlantic_nino.py",
    #"update_wam.py",
]

for script in scripts:

    print("=" * 60)
    print(f"Running {script}")
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, SCRIPT_DIR / script],
        cwd=SCRIPT_DIR,
    )

    if result.returncode != 0:
        raise RuntimeError(f"{script} failed.")

print("\nEverything completed successfully.")