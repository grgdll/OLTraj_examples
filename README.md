# OLTraj examples
These are two practical examples written ad jupyter notebooks to help new users understand how to use the OLTraj product.

To work with these examples you first need to clone this repository (e.g., click here https://github.com/grgdll/OLTraj_examples/archive/refs/heads/main.zip).

Unzipping this file should create on your computer the following directory structure:

``OLTraj_examples-main/``              <br/>
``├── 1_Plot_traj``               <br/>
``│   ├── Input          ``       <br/>
``│   │   └── amt27_track.csv``   <br/>
``│   └── Source             ``   <br/>
``│       ├── OLTraj_eg_1.ipynb`` <br/>
``├── 2_Plot_traj ``              <br/>
``│   ├── Input ``                <br/>
``│   └── Source ``               <br/>
``│       └── OLTraj_eg_2.ipynb ``<br/>
``├── environment.yml ``          <br/>
``└── README.md  ``               <br/>


You then need to download the data relative to each example (see which files exactly below) from here https://data.ceda.ac.uk/neodc/oltraj/data/v1.0

If you prefer using the FTP service, you will need to register as a CEDA user: https://services.ceda.ac.uk/cedasite/register/info/

## Example 1: Extracting and plotting Lagrangian trajectories over cruise track
The first example demonstrates how to extract and plot Lagrangian trajectories along a cruise track.

To run this example you will need to download the files below and save them in the directory `./1_Plot_traj/Input`:

* 20171021_oltraj_uv_global.nc  
* 20171024_oltraj_uv_global.nc  
* 20171028_oltraj_uv_global.nc
* 20171022_oltraj_uv_global.nc
* 20171026_oltraj_uv_global.nc
* 20171030_oltraj_uv_global.nc 

Finally, to run the jupyter notebook type this command from the top directory of the cloned repository (i.e., OLTraj_examples-main): `jupyter notebook 1_Plot_traj/Source/OLTraj_eg_1.ipynb`



