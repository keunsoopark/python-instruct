ref: https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#local

Create the environment  
`conda create -n myenv python=3.6.5`

Activate environment  
`conda activate myenv`

Enable environment-specific IPython kernel  
This will ensure expected kernel and package import behavior when working with Jupyter Notebooks within Anaconda environments.  
`conda install notebook ipykernel`

Create the kernel  
`ipython kernel install --user --name myenv --display-name "Python (myenv)"`


