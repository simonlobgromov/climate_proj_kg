import plotly.express as px
import plotly.graph_objects as go
import  pandas as pd
import sqlite3
import boto3
import argparse
import matplotlib.pyplot as plt


# s3 = boto3.client(
#     's3',
#     aws_access_key_id='',
#     aws_secret_access_key='',
#     region_name='ap-northeast-1'
# )
# response = s3.list_buckets()
# buckets = [bucket['Name'] for bucket in response['Buckets']]

# def upload_file(file_key):
#   file_name = file_key.split('/')[-1]
#   local_file_path = f'./{file_name}'
#   s3.download_file(buckets[0], file_key, local_file_path)

# upload_file('visualization_data_sql/data_visualization_sql.db')
conn = sqlite3.connect('data_visualization_sql.db')

parser = argparse.ArgumentParser(description='Script description')
parser.add_argument('--year', type=int, help='Year value')
args = parser.parse_args()
year = args.year

query = f"SELECT * FROM NDSI_location_{year}"
NDSI_location = pd.read_sql_query(query, conn)
conn.close()

plt.ion()

fig = px.density_mapbox(NDSI_location, lat='lat', lon='lon', z='NDSI', radius=12, zoom=7, opacity=.7, color_continuous_scale='GnBu', center=dict(lat=41.931586, lon=74.582786), mapbox_style="open-street-map", animation_frame="month")
fig.update_layout(width=1600, height=1200)
fig.show()

input("Press Enter to continue...")
