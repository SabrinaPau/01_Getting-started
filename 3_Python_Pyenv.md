# Python, pyenv and the wonderful world of virtual environments

- [Pyenv](#install-pyenv)
- [Python](#install-python-versions)
- [Virtual environments](#install-your-first-virtual-environment)


If you open the terminal and run the command `python --version` you will see that Python is already installed as part of the operating system. The default Python version installed on your Mac is 2.7. 
But the world has moved on and working in Data Science nowadays usually requires the use of Python 3. 
Actually you might want (or have) to use different Python 3 version for different projects. There are several tools available to help you with this task. During the bootcamp we will use pyenv and virtual environments to install, organize and manage different versions of Python (and other libraries) on your computer.

You can think of this as if you were planning on going biking: for biking in the city you need a city bike maybe with a bike basket and a fluffy seat. For going mountain biking you will need a mountain bike with mud flaps, no bike basket and you might also need a proper helmet with professional glasses. This is similar to working on different data science projects... for some you will need basic python libraries... for others you will need more advanced ones and sometimes they will only work with specific versions (if you wear a bike helmet in the city it will be a different one you need for mountain biking)


# Install pyenv

[Pyenv](https://github.com/pyenv/pyenv) is a simple Python version management tool you can download for free using homebrew. 

```
$ brew update
$ brew install pyenv
```


There are several advantages for using a tool like pyenv. It allows you to easily download or switch between Python versions with a single command. You can also set the Python version of your choice as the global one. 
It even makes it possible to switch Python versions by changing the directory. This proves to be particularly useful when you have different directories for projects which require different versions of Python. 

# Install Python versions

After you installed pyenv you can easily install different Python versions. If you want to see a list of all available versions and flavors you can use the following command:

```
pyenv install --list
```

For the bootcamp we will use Python 3.8.5. You can install it with:

```
pyenv install 3.8.5     
```

To set a specific version as the local (inside a directory) or global (everywhere) Python version you can use:

```
$ pyenv local 3.8.5
$ pyenv global 3.8.5
```


# Install your first [virtual environment](https://docs.python.org/3/tutorial/venv.html)

Working on a Data Science project does not only require Python. Most of the time it will also involve a bunch of different packages and modules, which exist in different versions as well. You might work on project A which uses version 1.0 of a particular package and on the same time on project B which requires version 2.0 of the same package. The solution for avoiding a conflict and fulfilling both requirements is using virtual environments. It basically works like a magician pulling a rabbit out of a hat. When you no longer need the virtual environment - your rabbit - you put it back into the hat and conjure up a new, different environment.

![Abracadabra!](https://media4.giphy.com/media/l41lPv1RcGVE1q5mo/giphy.gif)


A virtual environment is a self-contained directory tree containing a Python installation of the version of your choice and a number of additional packages, which are all isolated from other environments. So each project you are working on should have its own virtual environment. Another advantage of using virtual environments is that if you want to share your project with someone else they can install an identical copy of your environment to make sure everything will work.   


There are different approaches on how to manage various virtual environments. We will use the module venv for that. First of all move to the directory for which you want to create the virtual environment. Make sure you use the desired Python version either locally in this directory or globally. In the directory run the following command:

```
$ python -m venv .venv
```

This command will create a new virtual environment in the directory and store the necessary files in a new hidden folder called `.venv`. You could also replace .venv with a whole path where you want to save your environment. But we want to create our virtual environments inside our project folders. 
You can now activate the environment with: 

```
$ source .venv/bin/activate
```

If you want to deactivate it run:

```
$ deactivate
```

In order to use the real power of virtual environments we need to know how to install packages inside a specific environment. We can use a package installer for Python packages called Pip. The good news is: its already installed. We can simply run the command 

```
$ pip install <package_name>
```

and Pip will look for the latest version of the package in the Python Package Index (PyPI), calculate the dependencies and install all of them to ensure the new package will work flawlessly.

> You may wonder what the difference is between using `brew` and `pip`. They are both package installers, but brew, which is based on Ruby and Git, can be used to install all kinds of software packages, while pip, which is written in Python, can only be used to install Python packages. The main difference, however, is that brew installs packages globally and it cannot be used to install something only in a specific virtual environment. To install a package only locally in an environment you have to use pip!