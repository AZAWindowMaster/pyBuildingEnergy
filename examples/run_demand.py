"""
Minimal ISO 52016-1 heating & cooling demand calculation with pyBuildingEnergy.

Only the building energy NEEDS are calculated (no emission/distribution/
generation systems). Put this file and my_building.py in the same folder
(e.g. the repo's examples/ folder) and run:

    python run_demand.py
"""
from pathlib import Path

import pybuildingenergy as pybui
from pybuildingenergy.source.check_input import sanitize_and_validate_BUI

from my_building import BUI

# ------------------------------------------------------------------
# Settings - change these
# ------------------------------------------------------------------
# Weather: use a local EPW file, or set WEATHER_FILE = None to download
# data from PVGIS using the latitude/longitude in my_building.py.
WEATHER_FILE = Path(__file__).resolve().parent / "DRY_2001-2010_epw.epw"

OUTPUT_DIR = Path(r"C:\Users\aza.dk\OneDrive - WindowMaster\2_Projects\Python_Energy_Calculator\Test")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Check the input and apply automatic fixes where possible
    bui, issues = sanitize_and_validate_BUI(BUI, fix=True)
    errors = [i for i in issues if i["level"] == "ERROR"]
    for i in issues:
        print(f"[{i['level']}] {i['path']}: {i['msg']}")
    if errors:
        raise ValueError("Invalid building input - fix the errors listed above.")

    # 2) Run the ISO 52016-1 hourly calculation
    if WEATHER_FILE is not None:
        hourly, annual = pybui.ISO52016.Temperature_and_Energy_needs_calculation(
            bui, weather_source="epw", path_weather_file=str(WEATHER_FILE)
        )
    else:
        hourly, annual = pybui.ISO52016.Temperature_and_Energy_needs_calculation(
            bui, weather_source="pvgis"
        )

    # 3) Results
    area = BUI["building"]["net_floor_area"]
    r = annual.iloc[0]
    print("\n================ RESULTS ================")
    print(f"Building:         {BUI['building']['name']}  ({area} m2)")
    print(f"Heating demand:   {r['Q_H_annual_kWh']:10.0f} kWh  "
          f"({r['Q_H_annual_kWh_per_sqm']:.1f} kWh/m2)")
    print(f"Cooling demand:   {r['Q_C_annual_kWh']:10.0f} kWh  "
          f"({r['Q_C_annual_kWh_per_sqm']:.1f} kWh/m2)")
    print(f"Peak heating load: {hourly['Q_H'].max() / 1000:9.1f} kW")
    print(f"Peak cooling load: {hourly['Q_C'].max() / 1000:9.1f} kW")

    # Monthly demand in kWh (hourly values are in Wh per 1-h step)
    monthly = hourly[["Q_H", "Q_C"]].resample("MS").sum() / 1000
    monthly.index = monthly.index.strftime("%b")
    print("\nMonthly demand [kWh]:")
    print(monthly.round(0).to_string())

    # 4) Save
    hourly.to_csv(OUTPUT_DIR / "hourly_results.csv")
    annual.to_csv(OUTPUT_DIR / "annual_results.csv", index=False)
    monthly.to_csv(OUTPUT_DIR / "monthly_demand_kWh.csv")
    print(f"\nFiles saved in {OUTPUT_DIR}")
    return hourly, annual


if __name__ == "__main__":
    hourly, annual = main()
