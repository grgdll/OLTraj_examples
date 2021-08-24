#run in parallel using:
#find /data/datasets/Projects/OLTraj/From_AVISO/OLTraj/Processed/Lagrangian_traj/????/ -name "[1-2]*nc" | xargs -n1 -P1 sh -c 'sleep 2; echo $0' | xargs -n1 -P4 echo python3 shift_lon.py $1
import xarray as xr
import sys
import os

fn = sys.argv[1]
print(fn[-28:])

ds = xr.open_dataset(fn)
ds = ds.sortby("lon")

fntmp = fn[:-28]+'tmp_'+fn[-28:]
#print(fntmp)
ds.to_netcdf(fntmp)

ds.close()

fnnew = fn 

os.rename(fntmp, fnnew)



