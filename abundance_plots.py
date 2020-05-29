"""
Make plots from environmental and abundance data. Who knows what these will be
at this point...
"""

# imports
try:
    import os, sys
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import argparse
    import cartopy.crs as ccrs
    import directory, TARA
    # Import local modules
    sys.path.append(os.path.abspath('shared'))
except ImportError:
    print(ImportError)
    sys.exit()

# Directory management
main_dir = os.path.abspath('.').split('/')[-1]
output_dir = f"../{main_dir}_output/"
fig_dir = f"../{main_dir}_output/figures/"
directory.make_dir(fig_dir)

# request filename from user
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='alldata.csv', type=str,
    help="Name of environmental and adundance data file (csv)")
args = parser.parse_args()
filename = args.filename

# load  csv into DataFrame, if it exists and is accessible
try:
    df_all = pd.read_csv(output_dir + filename)
except FileNotFoundError:
    print(f"File: {args.filename} does not exist")
    sys.exit()
except IOError:
    print(f"File: {args.filename} is not accessible")
    sys.exit()

# now start the fun part
# isolate lat/lon of all data points
df_latlon=df_all[['latitude','longitude']].copy()

# pull information by taxonomic level
phy_list = [col for col in df_all.columns if 'Phylum' in col]
phy_str = [i.strip('Phylum_') for i in phy_list] # for labels later
df_phylum = df_all[phy_list].copy()

# PLOTTING
fs = 14 # primary fontsize
ms = 4 # primary markersize

# simple map of where we have data
fig1 = plt.figure(figsize=(10,7))
ax1 = fig1.add_subplot(1, 1, 1, projection=ccrs.Robinson(central_longitude = 0))
ax1.stock_img()
ax1.plot(df_latlon['longitude'], df_latlon['latitude'], linestyle='None',
    marker='o', ms=ms/2, mfc='firebrick', mec='firebrick',
    transform=ccrs.PlateCarree())

fig1.savefig(fig_dir + 'sample_map.png')
plt.close(fig1)

# simlar plot, scaled by abundance
fig2 = plt.figure(figsize=(10,7))
ax2 = fig2.add_subplot(1, 1, 1, projection=ccrs.Robinson(central_longitude = 0))
ax2.stock_img()
cmap = cm.get_cmap('Spectral')
count = 1
for col in df_phylum:
    norm_col = df_phylum[col] / max(df_phylum[col])
    mc = [list(cmap(count / len(phy_str)))]
    plt.scatter(df_latlon['longitude'], df_latlon['latitude'], s=100*norm_col,
        c=mc, marker='o', transform=ccrs.PlateCarree())
    count += 1
ax2.legend(phy_str)

fig2.savefig(fig_dir + 'Phylum' + '_abundance_map.png')
# plt.close(fig2)
