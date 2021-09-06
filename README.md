# OLTraj examples
These are two practical examples written as jupyter notebooks to help new users familiarise with the OLTraj product.

To work with these examples you first need to clone this repository (e.g., click here https://github.com/grgdll/OLTraj_examples/archive/refs/heads/main.zip).

Unzipping this file should create on your computer the following directory structure:
<pre>
OLTraj_examples-main/              
├── Example_1              
│   └── Source             
│       └──_OLTraj_eg1_.ipynb
├── Example_2             
│   ├── Input               
│   │   └── cruise_track.csv   
│   └── Source            
│       └── OLTraj_eg_2.ipynb 
├── Example_3              
│   └── Source             
│       └── OLTraj_eg_3.ipynb
├── environment.yml          
└── README.md                
</pre>

The file `environment.yml` allows you to recreate the `conda` environment needed for the notebooks to work. If you do not have `conda` installed, follow the instructions here: https://docs.conda.io/projects/conda/en/latest/user-guide/install/.

To create the `OLTraj_env` environment use the command `conda env create -f environment.yml`. Then the newly created conda environment needs to be activated using `conda activate OLTraj_env`.

The examples are made so that you do not need to download the OLTraj files onto your computer: the script will read and subset them from the CEDA THREDDS server.

If you need to code to run faster, you may want to download the data onto your computer (careful: each file is about 850 Mb) . You can find the files here: https://data.ceda.ac.uk/neodc/oltraj/data/v2.2.

If you prefer using the FTP service, you will need to register as a CEDA user: https://services.ceda.ac.uk/cedasite/register/info/.

## Example 1: Plotting trajectories around a fixed-point station
In this example we show how to extract and plot Lagrangian trajectories around a fixed-point monitoring station. These trajectories should allow one to understand where the water masses sampled at the fixed-point station were coming from at the time of sampling. It also demonstrates how the direction of the water masses might change during the year.

Start the jupyter notebook by typing this command from the top directory of the cloned repository (i.e., OLTraj    _examples-main): `jupyter notebook Example_1/Source/OLTraj_eg_1.ipynb`.

## Example 2: Plotting Lagrangian trajectories along a cruise track
This example demonstrates how to extract and plot Lagrangian trajectories along a cruise track.

Start the jupyter notebook by typing this command from the top directory of the cloned repository (i.e., OLTraj_examples-main): `jupyter notebook Example_2/Source/OLTraj_eg_2.ipynb`.
You will then be able to run the jupyter notebook and see the plotted Lagrangian trajectories along the cruise track.

You can modify the time and location of the track by changing the input file `./Example_2/Input/cruise_track.csv` (it is important to maintain the same format in the file).

## Example 3: Lagrangian evolution of a chlorophyll patch
Let us assume you have noticed in a satellite image at a given time (`t0`) a specific patch of surface water with an interesting feature in the cholorophyll-a concentration (chl). You now want to understand how the chl in this patch of water has been evolving before you sampled it and how it has evolved since you have sampled it. 

To achive this, one may select the region sampled at time `t0` and extract from this region a time series of chl values. This is known as an "Eulerian" analysis, in which we are implicitly assuming that surface water does not move. 
This assumption may be justified if the ratio of the spatial to temporal scales of study is large with respect to the speed of the currents in this region. 
However, when the ratio of the spatial to temporal scales of the processes we want to investigate is small relative to the speed of the currents, then it may be better to use a "Lagrangian" approach: this is when we track the movement of the water mass under exam.

In our example, we will demonstrate how to follow the dynamics of chl in a water mass as the latter moves in time. 

Start the jupyter notebook by typing this command from the top directory of the cloned repository (i.e., OLTraj_examples-main): `jupyter notebook Example_3/Source/OLTraj_eg_3.ipynb`.

