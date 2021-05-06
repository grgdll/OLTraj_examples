# OLTraj examples
These are two practical examples written as jupyter notebooks to help new users familiarise with the OLTraj product.

To work with these examples you first need to clone this repository (e.g., click here https://github.com/grgdll/OLTraj_examples/archive/refs/heads/main.zip).

Unzipping this file should create on your computer the following directory structure:
<pre>
OLTraj_examples-main/              
├── 1_Plot_traj             
│   ├── Input               
│   │   └── cruise_track.csv   
│   └── Source            
│       └── OLTraj_eg_1.ipynb 
├── 2_Plot_traj              
│   ├── Input                 
│   └── Source             
│       └── OLTraj_eg_2.ipynb
├── environment.yml          
└── README.md                
</pre>

The file `environment.yml` allows you to recreate the `conda` environment needed for the notebooks to work. To create this environment use the command `conda env create -f environment.yml`. Then the newly created conda environment needs to be activated using `conda activate OLTraj_env`.

You then need to download the data relative to each example (see which files exactly below) from here https://data.ceda.ac.uk/neodc/oltraj/data/v1.0.

If you prefer using the FTP service, you will need to register as a CEDA user: https://services.ceda.ac.uk/cedasite/register/info/.

## Example 1: Extracting and plotting Lagrangian trajectories over cruise track
The first example demonstrates how to extract and plot Lagrangian trajectories along a cruise track.

To run this example you will need to download the files below and save them in the directory `./1_Plot_traj/Input`:

* 20171021_oltraj_030_uv_global.nc  
* 20171024_oltraj_030_uv_global.nc  
* 20171028_oltraj_030_uv_global.nc
* 20171022_oltraj_030_uv_global.nc
* 20171026_oltraj_030_uv_global.nc
* 20171030_oltraj_030_uv_global.nc 

Finally, to start the jupyter notebook type this command from the top directory of the cloned repository (i.e., OLTraj_examples-main): `jupyter notebook 1_Plot_traj/Source/OLTraj_eg_1.ipynb`.
You will then be able to run the jupyter notebook and see the plotted Lagrangian trajectories along the cruise track.

To minimise the number of OLTraj files you need to download, we have kept the length of the cruise track short. However, you can also generate your own cruise-track file, download the relative OLTraj files, and plot all the Lagrangian trajectories that you want.


