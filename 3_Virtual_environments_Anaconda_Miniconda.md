# Virtual environments, Anaconda and Miniconda

- [Virtual environments](#Virtual-environment)
- [Creating virtual environments with miniconda](#Creating-virtual-environments-with-miniconda)


## Virtual environments

When working as a Data Analyst your projects will require more than only Python. Most of the time it will also involve a bunch of different packages and modules, which exist in different versions as well. You might work on project A which uses version 1.0 of a particular package and on the same time on project B which requires version 2.0 of the same package. The solution for avoiding a conflict and fulfilling both requirements is using virtual environments. It basically works like a magician pulling a rabbit out of a hat. When you no longer need the virtual environment - your rabbit - you put it back into the hat and conjure up a new, different environment.

![Abracadabra!](https://media4.giphy.com/media/l41lPv1RcGVE1q5mo/giphy.gif)


A virtual environment is a self-contained directory tree containing a Python installation of the version of your choice and a number of additional packages, which are all isolated from other environments.  
If you open the terminal and run the command `python --version` you will see that Python is already installed as part of the operating system. The default Python version installed on your Mac is 2.7.   
However, since the world has moved on, Data Analytics nowadays usually require the use of Python 3 so that you need to specify a newer Python version within your virtual environment (for the bootcamp we will use Python 3.8.5.).  
So each project you are working on should have its own virtual environment. Another advantage of using virtual environments is that if you want to share your project with someone else they can install an identical copy of your environment to make sure everything will work.   

There are different approaches on how to manage various virtual environments. We will introduce only way of creating those environments at this point.

### Creating virtual environments with miniconda

Maybe you have heard of **Anaconda** a distribution of Python and R. We will not download the whole Anaconda distribution since it contains a lot of stuff we will not use, but we will download **Miniconda**, the slimmed-down distribution version of Anaconda:

1. Download installer [here](https://docs.conda.io/en/latest/miniconda.html) (Python 3.7 Mac OS X 64-bit .pkg installer)
2. Once the download is complete, locate the installer file using Finder and run it
3. In terminal:
```BASH 
$ bash Miniconda3-latest-MacOSX-x86_64.sh
```
4. Follow the prompts on the installer screens
5. Close and then re-open your terminal window
6. For testing: 
```BASH
$ conda list
```

You now have to options to create and install a new environment. You can either install it from an `environment.yml` file or step by step. At the beginning we will use a environment.yml file which contains a list of all the packages we want to install in a specific format. You can find the file called [nf_base_environment.yml](nf_base_environment.yml) in this repo.


1. Move to neuefische/getting-started repo
2. ls (list files) and it should show nf_base_environment.yml
3. Now on terminal window type: 
```BASH 
$ conda env create --file nf_base_environment.yml
 ```
4. In order to activate or deactivate the virtual environment run:
```BASH 
$ conda activate nf_base
$ conda deactivate
```
While the environment is active you should see the name of the environment (nf_base) in your terminal. 


In order to create an environment from scratch you can use this workflow:

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
