# OLTraj examples
These are two practical examples to help new user understand how to use the OLTraj product.

To work with these examples you first need to download the data from here https://data.ceda.ac.uk/neodc/oltraj/data/v1.0

If you want to use the FTP service, you need to register to CEDA. You can register here: https://services.ceda.ac.uk/cedasite/register/info/

## Example 1: Extracting and plotting Lagrangian trajectories over cruise track
The first example demonstrates how to extract and plot Lagrangian trajectories along a cruise track.

To run this example on a jupyter notebook, first you will need to clone the GitHub repository onto your computer.

This should create on your computer the following directory structure:

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

The file `environment.yml` contains all the dependencies needed to run these examples. To install the same `conda` environment, type this command: `conda env create --name OLTraj_examples -f environment.yml`. When the environment is intalled, activate it with `conda activate OLTraj_examples`.


Then you will need to download directory the files below and save them in the `./1_Plot_traj/Input` directory:

* 20171021_oltraj_030_uv_global.nc  
* 20171024_oltraj_030_uv_global.nc  
* 20171028_oltraj_030_uv_global.nc
* 20171022_oltraj_030_uv_global.nc
* 20171026_oltraj_030_uv_global.nc
* 20171030_oltraj_030_uv_global.nc 

Finally, to run the jupyter notebook type this command from the top directory of the cloned repository (i.e., OLTraj_examples-main): `jupyter notebook 1_Plot_traj/Source/OLTraj_eg_1.ipynb`



