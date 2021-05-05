# OLTraj examples
These are two practical examples to help new user understand how to use the OLTraj product.

To work with these examples you first download the data, which requires you to register to CEDA if you want to use the FTP. You can register here: https://services.ceda.ac.uk/cedasite/register/info/
You can also download data from CEDA without registering, if you use the http service. You can download OLTraj data for these examples from here https://data.ceda.ac.uk/neodc/oltraj/data/v2.0

## Example 1: Extracting and plotting Lagrangian trajectories over cruise track
The first example demonstrates how to extract and plot Lagrangian trajectories along a cruise track.

To run this example on a jupyter notebook, first you will need to clone the GitHub repository onto your computer.

This should create on your computer the following directory structure:

``OLTraj_examples/``              <br/>
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



Then you will need to download and save in the `./Input` directory the following OLTraj files:

* 20171021_oltraj_uv_global.nc  
* 20171024_oltraj_uv_global.nc  
* 20171028_oltraj_uv_global.nc
* 20171022_oltraj_uv_global.nc
* 20171026_oltraj_uv_global.nc
* 20171030_oltraj_uv_global.nc 

Finally, to run the jupyter notebook tyoe this command from the top directory of the cloned repository (i.e., OLTraj_examples-main): `jupyter notebook 1_Plot_traj/Source/OLTraj_eg_1.ipynb`



