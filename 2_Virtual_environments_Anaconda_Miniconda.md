# Virtual environments, Anaconda and Miniconda

## Virtual environments

When working as a Data Analyst your projects will require more than only Python. Most of the time it will also involve a bunch of different packages and modules, which exist in different versions as well. You might work on project A which uses version 1.0 of a particular package and on the same time on project B which requires version 2.0 of the same package. The solution for avoiding a conflict and fulfilling both requirements is using virtual environments. It basically works like a magician pulling a rabbit out of a hat. When you no longer need the virtual environment - your rabbit - you put it back into the hat and conjure up a new, different environment.

![Abracadabra!](https://media4.giphy.com/media/l41lPv1RcGVE1q5mo/giphy.gif)


A virtual environment is a self-contained directory tree containing a Python installation of the version of your choice and a number of additional packages, which are all isolated from other environments.  
If you open the terminal and run the command `python --version` you will see that Python is already installed as part of the operating system. The default Python version installed on your Mac is 2.7.   
However, since the world has moved on, Data Analytics nowadays usually require the use of Python 3 so that you need to specify a newer Python version within your virtual environment (for the bootcamp we will use Python 3.8.5.).  
So each project you are working on should have its own virtual environment. Another advantage of using virtual environments is that if you want to share your project with someone else, they can install an identical copy of your environment to make sure everything will work.   

There are different approaches on how to manage various virtual environments. We will introduce only one way of creating those environments at this point.

### Creating virtual environments with miniconda

Maybe you have heard of **Anaconda**, a distribution of Python and R. We will not download the whole Anaconda distribution since it contains a lot of stuff we will not use. Instead, we will download **Miniconda**, the slimmed-down distribution version of Anaconda. Follow the steps in your terminal (without the $-signs):

1. In terminal:
```BASH 
$ brew install --cask miniconda
```

2. Close and then re-open your terminal window

3. For testing: 
```BASH
$ conda list
```

You now have two options to create and install a new environment. You can either install it from an `environment.yml` file or by installing single packages step by step. Since we want you to be able to set up your own environment in the future, you should create the base environment for our bootcamp from scratch. 

In order to create an environment from scratch you can use this general workflow:
```BASH 
# Create new environment
$ conda create --name <env_name>
# Activate environment 
$ conda activate <env_name>
# Installing packages 
$ conda install <package_name>
# Deactivate environment
$ conda deactivate 
```
Let's create a base environment called *nf_base* with specific packages by running the following lines of code in your terminal:


```BASH 
# Create new environment called nf_base with Python version 3.8.5
$ conda create --name nf_base python=3.8.5
# Activate nf_base environment 
$ conda activate nf_base
# Installing packages inside nf_base environment
$ conda install pip
$ conda install matplotlib
$ conda install numpy
$ conda install pandas
$ conda install scipy
$ conda install seaborn
$ conda install statsmodels
$ conda install scikit-learn
$ conda install nb_conda_kernels
```
In order to activate or deactivate virtual environments run:
```BASH 
$ conda activate nf_base
$ conda deactivate
```
While the nf_base environment is active you should see the name of the environment (nf_base) in your terminal. 

You can export your environment to a YAML file, which other programmers can use to install the same environment. Let's do that now! With your conda environment activated, run the following command: 
```BASH 
$ conda env export > nf_base_environment.yml
```
This YAML file contains a list of the dependencies needed to be installed for a certain project. For installing an environment from a yml file, you need the following command in the future (you don't need to do this now, since you have already created your environment):

```BASH 
$ conda env create --file environment.yml
 ```



