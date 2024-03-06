# NDSI Visualization

In this repository, there is an example of visualizing the Snow Cover Index (NDSI) for the years 2005, 2006, 2007, and 2008 using the `Plotly` library. The prepared data is stored in the form of an SQL database. To run the visualization script, execute:

```
git clone https://github.com/simonlobgromov/climate_proj_kg
cd climate_proj_kg
pip install -r requirements.txt
wget 'https://www.dropbox.com/scl/fi/28dh2cicu7eljzu626elf/data_visualization_sql.db?rlkey=f8mckpdevjkg327g48as40kos&dl=0' -O data_visualization_sql.db
python NDSI_vis_year_map.py --year 2005
```

Or you can open the project from the file `NDSI_vis_year_map.ipynb`
