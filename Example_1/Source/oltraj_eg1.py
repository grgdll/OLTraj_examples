import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import glob
import pandas as pd
from datetime import datetime
import sys


# read file with cruise track 
## this input file shoud look like this (it's important to keep the same exact names for the column labels):
## (Note also that the DateTime field is in UTC)
# DateTime_UTC,Latitude_degreesN,Longitude_degreesE
# 2017-09-23  17:46,50.06083333,-3.343666667
# 2017-09-24  11:21,48.92683333,-7.6235
# 2017-09-25  03:57,47.269,-11.01
# 2017-09-25  12:04,46.68633333,-12.00016667
# ...
track = pd.read_csv("../Input/cruise_track.csv")
track['DateTime_UTC'] = pd.to_datetime(track['DateTime_UTC']) 

# remove some of the stations to speed the example up
track = track.iloc[0::3,:]
track.reset_index(drop=True, inplace=True) # reset pandas index after dropping rows

# intialise arrays that will store the trajectories
trajlon = np.full((len(track), 59), np.nan)
trajlat = np.full((len(track), 59), np.nan)



### Extract OLTraj trajectories corresponding to cruise track
OLTraj_THREDDS_string = 'http://dap.ceda.ac.uk/thredds/dodsC/neodc/oltraj/data/v2.2/'

for ifn in range(len(track)):   
    fname = track['DateTime_UTC'].iloc[ifn].strftime('%Y')+'/'+track['DateTime_UTC'].iloc[ifn].strftime('%Y%m%d') + '_oltraj_uv_global.nc'
    fn = OLTraj_THREDDS_string + fname
   

    print("now =", datetime.now())  # these is for debugging
    print("Reading OLTraj file: " + fn + " .......")

    # open OLTraj file
    print("  opening file...", end="")
    sys.stdout.flush() # these is for debugging
    dsAV = xr.load_dataset(fn)
    print("  done" )
    print("now =", datetime.now())  # these is for debugging
    sys.stdout.flush() # these is for debugging
    
    # read and subset OLTraj trajectories corresponding to current location of the cruise track 
    print("  subsetting and reading file...", end="")
    tmp = dsAV.sel(lon=track['Longitude_degreesE'].iloc[ifn], lat=track['Latitude_degreesN'].iloc[ifn], method="nearest")
    print("  done" )
    
    print("done" )   
    
    # store trajectories for given date
    trajlon[ifn] = tmp['trajlon']
    trajlat[ifn] = tmp['trajlat']

    dsAV.close()
    del dsAV



 
