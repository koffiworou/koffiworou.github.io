from pathlib import Path
import requests

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent

FIG_DIR = ROOT_DIR / "images" / "downloaded_figures"

headers = {
    "User-Agent": "Mozilla/5.0"
}

files = {
    "gfs_world-wt_sstanom_d1.png":
        "https://climatereanalyzer.org/wx/todays-weather/maps/gfs_world-wt_sstanom_d1.png",
    "gfs_world-wt_prcp-mslp_d1.png":
        "https://climatereanalyzer.org/wx/todays-weather/maps/gfs_world-wt_prcp-mslp_d1.png",
    "gfs_world-wt_ws10_d1.png":
        "https://climatereanalyzer.org/wx/todays-weather/maps/gfs_world-wt_ws10_d1.png",
    "gfs_world-wt_mslp-anomsd_d1.png":
        "https://climatereanalyzer.org/wx/todays-weather/maps/gfs_world-wt_mslp-anomsd_d1.png",
    "gfs_world-wt_gph500-anomsd_d1.png":
        "https://climatereanalyzer.org/wx/todays-weather/maps/gfs_world-wt_gph500-anomsd_d1.png",
    "gfs_world-wt_ws250-mslp_d1.png":
        "https://climatereanalyzer.org/wx/todays-weather/maps/gfs_world-wt_ws250-mslp_d1.png",
    "gfs_world-wt_ws500-gph_d1.png":
        "https://climatereanalyzer.org/wx/todays-weather/maps/gfs_world-wt_ws500-gph_d1.png",
    "gfs_world-wt_t2anom-sst_d1.png":
            "https://climatereanalyzer.org/wx/todays-weather/maps/gfs_world-wt_t2anom-sst_d1.png",
}

def main():

    FIG_DIR.mkdir(parents=True, exist_ok=True)

    for filename, url in files.items():
        try:
            print(f"Downloading {filename}")

            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()

            (FIG_DIR / filename).write_bytes(response.content)
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

    print("Done.")

if __name__ == "__main__":
    main()