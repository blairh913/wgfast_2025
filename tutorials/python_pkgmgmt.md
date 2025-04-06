# Package managers and environments  

## Python packages  

Python can be described as charged with batteries, to say that it already comes packed with a number of modules (functions and classes) to get you started. Still in every day use of Python, you will need additional external functionality which in Python is commonly imported through packages. Packages are the equivalent to libraries in R and can be compared to toolboxes in Matlab.  

A Python package contains one or more modules. A module is a *.py* file that contains reusable code, typically functions or models.  
Packages can be seen as analoguous to libraries in R and very similar to toolboxes in Matlab.  

```{note}
**What are dependency issues?**  
Dependency issues occur when multiple packages depend on different version of the same package. Only one single version of package is allowed to be installed in a Python environment. FInding a solution to this issue can be complicated.  
For example package A might have been written based on version 1.2 of package B. Now package B releases an update where a function that was called ```wave_number()``` is now kalled ```k()```. If package A is not updated and you only install the new version of package B, package A won't work properly anymore. If you also need package C that was written using the k() function form package B, you can't simply downgrade package B, otherwise package C won't work anymore.  
```  

## Python environments

### What are environments and why should we use them?

A Python environment can be seen as a separate workspace where you can run Python programs without interfering with other projects. It helps keeping things organized by managing different versions of Python and packages needed for each project. For example, if one project needs Python 3.8 and another needs Python 3.10, you can create separate environments for each, so they don’t mix and cause problems. Tools like [virtualenv](https://virtualenv.pypa.io/en/latest/), [venv](https://docs.python.org/3/library/venv.html), and [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) or [mamba](https://mamba.readthedocs.io/en/latest/) help create and manage these environments easily.  

Uisng environments has a number of benefits:

- **Avoiding Dependency Conflicts**  
Different projects may require different versions of libraries. A Python environment ensures that each project uses the correct versions without conflicts.  
- **Keeping Projects Organized**
Each environment acts as a separate workspace, so your global Python installation remains clean and uncluttered.
- **Working with Different Python Versions**  
You can create environments with different Python versions, which is useful if one project needs Python <3.8 while another needs Python >3.10.
- **Easier Collaboration**  
When sharing projects, you can provide a list of dependencies (requirements.txt for pip or environment.yml for conda or mamba), allowing others to recreate the exact environment.
- **Experimenting Without Risk**  
You can safely test new libraries or code changes in a separate environment without affecting your main setup.
- **Better Reproducibility**  
If you revisit a project months later, having an isolated environment ensures it still runs as expected without issues caused by updated or missing dependencies.
- **Security Benefits**  
Running code in a virtual environment can prevent accidental modifications to system-wide files and protect your system from potential risks.  

```{important}  
Here we will focus on the use of mamba. ```conda```probably remains the most popular package manager but there are several benefits that ```mamba``` has compared to ```conda```: 
- Much faster than Conda (especially for package resolution)
- Uses parallel downloads, making installations and updates quicker
- Fully compatible with Conda environments and packages.
```

```{hint}
**R**  
In R is is common practice to start new *Projects* for each project. R Projects are a great way to magae paths and file dependencies, but they lack package management.  
Virtual environments like they are commonly used in Python exist in R as well, through [renv](https://posit.co/blog/renv-project-environments-for-r/). ```renv``` manages package versions and dependencies separately for each project. This ensures that the code will work even after a long period of time and enhance compatibility with the systems of colleagues.  

```

### Using environmnents  

If you decide to use ```conda``` instead of ```mamba```, you can replace ```mamba``` by ```conda``` in all commands listed here.

1) Creating a new environment  

    To create a new environment called ´my_env´ from a yml called ´my_env.yml´ file we use:  

    ´´´bash
    mamba env create -n my_env -f my_env.yml
    ´´´
    or we can create an environment from scratch:  

    To create a new environment (called ```my_env```) with a specific Python version (here 3.12) we use:  

    ```bash
    mamba create --name my_env python=3.12
    ```

    If we don't specifiy the python version the environment will use the default version (currently 3.9).  
    We can install specific packages while creating the environment (note more packages can be installed at a later stage):  

    ```bash
    mamba create --name my_env python=3.12 numpy pandas xarray
    ```  

    Packages are simply added to the end of the command, separated by spaces.  
    ```mamba``` will make sure that all dependencies of the different packages are installed and are compatible. If for example a package in the list or a dependecy would not be compatible with the wanted Python verison, an error message would be the result and the environment would not be created.  

2) Activating an environment  

   To start using an environment we use ```activate```:  

   ```bash
   mamba activate my_env
   ```  

3) Deavtivating an environment  

   To stop using an environment, we use ```deactivate``` (no need to add the environment name at the end):  

   ```bash
   mamba deactivate
   ```

4) Listing all available environments  

   ```bash
   mamba env list
   ```

    or  

    ```bash
    mamba info --envs
    ```

5) Installing packages in an environmnent  

    If the environment in which the package should be installed is activated:  

    ```bash
    mamba install echopype
    ```

    alternatively, the specific environmnent can be defined:  

    ```bash
    mamba install --name my_env echopype
    ```

6) Removing a Package from an Environment  

   To remove a package we use the ```remove```command (here we remove the numpy package):  

   ```bash
   mamba remove numpy
   ```  

7) Deleting an environment  

    To completely remove an environment and all its packages:

    ```bash 
    mamba env remove --name my_env
    ```

8) Exporting an environment (for Sharing)  

    To save all installed packages into a file:

    ```bash
    mamba env export > environment.yml
    ```

    This file can be shared with others to recreate the environment.

9) Recreating an environment from a File  

    To create an exact copy of an environment from an environment.yml file:

    ```bash
    mamba env create --file environment.yml
    ```

## Installing new packages and other useful mamba commands

### Installing, updating, removing packages  

|mamba|Description|-|
|-----|-----------|-|
|mamba install package_name| Installs a package||
|mamba remove package_name| Removes a package |
|mamba update package_name| Update a package| 
|mamba update --all| update all packages in the active environment|
|mamba list| list all installed packages|
|mamba list --name my_env| list all packages in a specific environmnent|

### Cleaning up packages  

|mamba|Description|-|
|-----|-----------|-|
|mamba clean --all| Remove unneccessary package files|
|mamba clean --packages| Remove unsused package versions|
|mamba clean --tarballs| Remove temporary package files|

### Checking mamba configuration  

View mamba settings:  

```bash
mamba config --show
```

add channel for package retrieval (example adds the conda-forge channel):  

```bash
mamba config --add channels conda-forge
```  

## Loading packages in Python

Once packages are installed in an environment, they can be imported in a Python script with the ```import``` command. We will use the ```math``` package in the examples below. Functions from within the package can be accesses with dot ```.```notation:  

```python
import math
math.pi  #output: 3.14159....
```

we can give packages an alias usign ```as``` (here ```m```)

```python
import math as m
m.pi #output: 3.14159....
```

```{tip}
It is common practice to import some package using an alias, popular examples include (these aliases are not required but consistent with industry standards and imporve readibility):

|Package name| alias|
|----|-|
|numpy|np|
|pandas|pd|
|xarray|xr|
|matplotlib.pyplot|plt|
|seaborn|sns|
|scikit-learn|sklearn|
|echopype|ep|
|datetime|dt|
|statistics|stats|
|BeautifulSoup|bs4|
|itertools|it|
|collections|col|
```

We can import specific functions:  

```python
from math import sqrt, pi
sqrt(64) #output: 8.0
```

When importing specific functions, we do not use the dot notations anymore but can call the functions directly.

we can also load all funcitons from one packake using ```*```, it is considered good practice to only import what you need though:

```python
from math import *
sqrt(64)  #output: 8.0
```

```{hint}
**Comparing loading packages in R and Python**  

| Python | R |
| ------ | - |
| import packages | load libraries |
| ```import packagename``` or with an alias ```import packagename as pkg```, to import specific functions from a package we can use ```from packagename import function```    |```library(packagename)``` <br> In R libraries need to be loaded to allow usage of specialised functions. Typically in R you import entire libraries, but since R 4.0 you can also import specific functions through ```library(packagename, include.only=c("function1", function2"))``` similarly, to avoid conflicts between different libraries funcitons can be exluded through ```library(packagename, exclude= c("function3", "function4"))```|
|__Specific examples:__||  
|```import numpy as np``` <br>This imports the numpy package and all numpy functions can be called through the alias ```np``` using ```np.function()``` <br><br> ```import echopype as ep``` this imports the echopype package awith the alias ```ep``` <br> ```from echopype import open_raw``` this imports only the ```open_raw()```function from ```echopype```|<br> <br> ```library(ggplot2)``` this imports one of the most popular graphics libraries in R. Functions from the library can be used by just calling the function (for example ```ggplot()``` or by specifying the package and the function ```ggplot2::ggplot()``` <br><br> ```library(dplyr, include.only=c("filter", "select"))``` imports only the ```filter``` and ```select```functions from the ```dplyr```package. ```library(dplyr, exclude=c("mutate", "lag"))```imports all functions from the```dplyr```package except for the```mutate```and```lag``` functions|
```
