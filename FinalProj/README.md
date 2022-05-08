This zip package contains all the components relating to the system project.

Files:
-PJojy_SystemProject.ipynb: The System project Jupyter Notebook containing the 6Ds

-Dockerfile: Used to build the docker image.

-Grocer_Model.h5: The trained grocery store forecasting RNN model file

-grocer_model.py: The file script to create the GUI

-inpscale.sav: The input scaler save file to be used in grocer_model.py

-items.csv: The data file containing the item names 

-outscale.sav: The output scaler save file to be used in grocer_model.py

-requirements.txt: The file defining additional python packages to install in docker container

-train.csv: The training data.

-docker-image.yml: The github->docker pipeline script.

Refer to the jupyter notebook for instructions on how to run the docker image/activate the GUI. The github->dockerhub pipeline is defined at https://github.com/paulmjojy/705.603/blob/master/.github/workflows/docker-image.yml and also explained in the jupyter notebook.