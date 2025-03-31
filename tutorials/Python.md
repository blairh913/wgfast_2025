# Python - and the machine that goes ping

## The life of Python  

Funny anecdotes from Jack...to be filled later this week or next  
Devloped originally at CWI - Centrum Wiskunde & Informatica, in Amsterdam, the Netherlands by Guido van Rossum with first implementation in 1989. Guido was the lead developper until 2018. In 2018 Guido announced that he will go on permanent vacation from his responsibilities as benevolant dictator for life (BDFL). He remained president of the Python Software Foundation until 2023. Since 2023 Dawn Gibson Wages is the new president of the foundation.  

First Python for Mac by Jack Jansen...

Python named after the Monty Python Flying Circus (not the snake, dispute with Riley Books over cover showing a python snake)

Python uses IDLE - Integrated Development and Learning Environment, but really named after Eric Idle from Monty Python etc...

Python is currently one of the most popular programming languages, particularly within the machine learning community. Python  

### Zen of Python by Tim Peters  

Tim Peters is a major contributor to the Python programming language, notably he wrote the original CPYthon implementation.  

The Zen of Python by Tim Peters can be accessed in Python through ```import this```  
||||||
|-|-|----|-|-|
|1|Beautiful is better than ugly|  |11|Unless explicitly silenced|
|2|Explicit is better than implicit|  |12|In the fase of ambiguity refuse the temptation to guess|
|3|Simple is better than complex||12|There should be one -- and preferably one -- obvious way to do it|
|4|Complex is better than complicated||14|Although that may never be obvious at first unless you are Dutch|
|5|Flat is better than nested||15|Now is better than never|
|6|Sparse is better than dense||16|Although never is often better than "right" now|
|7|Readibility counts||17|If the implementation is hard to explain, it's a bad idea|
|8|Special cases aren't special enough to break the rules||18| If the implementation is easy to explain it may be a good idea|
|9|Although practicality beats purity||19|Namespaces are one honking great idea -- Let's do more of those!|
|10|Errors should never pass silently||20|"some bizarre Tim Peters in-joke"|

## Python vs R vs Matlab  

## How are we using Python?  

## Install Python, conda, mamba, echopype - Miniforge

The very easiest way to get a minimal install of [Conda]("https://conda.io/"), [Mamba]("https://github.com/mamba-org/mamba") and Python, with conda-forge as default channel is to install (Miniforge)["https://github.com/conda-forge/miniforge"].  
Once Miniforge is installed, you should be able to use ```conda``` and ```mamba``` in your terminal.  

The very easiest way to install Miniforge is to download and run a provided installer for your OS  from [https://conda-forge.org/download/]("https://conda-forge.org/download/")  

**Mac & Linux**: Download the installer and run ```bash Miniforge3-$(uname)-$(uname -m).sh```
**Windows**: download and run the Windows installer.  

**Note for Windows users:**  
By default the commands are not added to the path environment (making them available in the default Windows Command Prompt (CMD)). This is a precautious step, to avoid chances of software conflicts.  
*Solutions:*  

* Option 1 (easiest, safest): Use *Anaconda Prompt*, like the freshly installed *Miniforge Prompt*
* Option 2: Initialise conda in the *Anaconda Prompt* by typing ```conda init```. Close your propmpt window and open it again. Now the commands should be available
* Option 3: [Manually add]("https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14)#to-add-a-path-to-the-path-environment-variable") ```C:\Users\myusername\miniforge3\condabin``` to the path environment. This will allow you to use the commands from any prompt, with limited risk of conflicts with other software.  
  
## Everyday differences Python, R, Matlab  

### Which language should I use?  

### Very essential syntax  

### Marking code blocks

#### Python - indentation

A key difference of Python compared to most other programming languages is that in Python indentation matters (the spaces at the beginning of every line of code). Python uses indentation to deliminate blocks of code. The number of spaces you use is up to you but you need to be consistent.  
*Example:*  

```python
print("This is the first line of the code") 
a = 10 
print("Here we add an if statement")
if a > 5:
    print(a)
else:
    print("a is < 5")
```

If you were to skip the indentation, Python will throw an error:  

```IndentationError: expected an indented block```  
This might feel like a nuissance at first, but after a while it will feel natural and keep your code organised.

#### R - {}  

In R, a consistent use of indentation will make code much easier to read but is not strictly necessary. Functions, loops and statemtent are delimited by ```{}```.  
*Example:*  

```r
print("This is the first line of the code") 
a = 10 
print("Here we add an if statement")
if (a > 5){
    print(a)
}else{
    print("a is < 5")
}
```

#### Matlab - end  

In Matlab, a consistent use of indentation will make code much easier to read but is not strictly necessary. Ending each line with ```;``` will prevent printing the result to the console. Functions loops and statements are closed by ```end```.  
**Example**  

```matlab
disp("This is the first line of the code");
a = 10;
disp("Here we add an if statement");
if a > 5;
    disp(a);
else
    disp("a is < 5");
end
```

### For / while loops and  if else statements  

### Defining functions  

### Using specialised functions  

#### Overview  

|      | Python | R | Matlab |
| ---- | ------ | - | ------ |
|| import packages | load libraries | Use toolboxes |
| *Example*| ```import packagename``` or with an alias ```import packagename as pkg```, to import specific functions from a package we can use ```from packagename import function``` <br><br>**Specific examples:**<br>```import numpy as np``` <br>This imports the numpy package and all numpy functions can be called through the alias ```np``` using ```np.function()``` <br><br> ```import echopype as ep``` this imports the echopype package awith the alias ```ep``` <br> ```from echopype import open_raw``` this imports only the ```open_raw()```function from ```echopype```|```library(packagename)``` <br> In R libraries need to be loaded to allow usage of specialised functions. Typically in R you import entire libraries, but since R 4.0 you can also import specific functions through ```library(packagename, include.only=c("function1", function2"))``` similarly, to avoid conflicts between different libraries funcitons can be exluded through ```library(packagename, exclude= c("function3", "function4"))```<br> <br> **Specific examples**<br><br> ```library(ggplot2)``` this imports one of the most popular graphics libraries in R. Functions from the library can be used by just calling the function (for example ```ggplot()``` or by specifying the package and the function ```ggplot2::ggplot()```<br><br> ```library(dplyr, include.only=c("filter", "select"))``` imports only the ```filter``` and ```select```functions from the ```dplyr```package. ```` library(dplyr, exclude=c("mutate", "lag"))```imports all functions from the ```dplyr```package except for the ```mutate```and ```lag``` functions||

#### Python  

#### R

In R functions that are not incluedd in the base verison of R, are included in libraries (the equivalent to packages in Python). Typically libraries are stored in a folder specific to a given version of R (```.libPaths()```, this path can be modified in the ```.RProfile```) 

### Installing specialised tools  

### Working environments  

### Jupyter and JupyterLab  

### Writing a package  

#### Structure  

#### Commenting  

#### Pushing to GitHub

#### Pushing to conda

#### Pushing to pypi  

## Interactive plotting
