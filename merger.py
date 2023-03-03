import pandas as pd

planet_df_1 = pd.read_csv("/content/PRO-NASA-Exoplanet-Scraped-Data/updated_scraped_data.csv")
new_planet_df_1 = pd.read_csv("/content/PRO-NASA-Exoplanet-Scraped-Data/new_scraped_data.csv")

new_planet_df_1.drop(
    columns=["discovery_date","mass","detection_method"],
    inplace=True
)
new_planet_df_1.head()
headers = [
    "name", 
    "light_years_from_earth", 
    "planet_mass", 
    "stellar_magnitude", 
    "discovery_date", 
    "hyperlink", 
    "planet_type",
    "discovery_date", 
    "mass",
    "planet_radius", 
    "orbital_radius", 
    "orbital_period", 
    "eccentricity", 
    "detection_method"
]

final_planet_df_1 = pd.DataFrame(columns=headers)
final_planet_df_1 = pd.merge(planet_df_1, new_planet_df_1)
final_planet_df_1.to_csv("final_database.csv")

new_web_df = pd.read_csv('/content/PRO-NASA-Exoplanet-Scraped-Data/PSCompPars.csv')
new_web_df["pl_name"] = new_web_df["pl_name"].str.lower()
new_web_df = new_web_df.sort_values("pl_name")

merge_planets_df = pd.merge(final_planet_df_1, new_web_df, on = "id")
merge_planets_df.columns
merge_planets_df.to_csv("final_merged_planet_database.csv")
