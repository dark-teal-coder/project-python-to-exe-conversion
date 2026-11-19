<!-- README file for projects-->

# Python Program to Executable Conversion

## Metadata

- <ins>Project Owner</ins>: [@dark-teal-coder](github.com/dark-teal-coder)
- <ins>First Published Date</ins>: 2026-11-19

## Project

- **Title**: *Python Program to Executable Conversion*
- **Difficulty**:
  - [ ] Beginner
  - [ ] Intermediate
  - [x] Advanced
- **Scale**:
  - [x] Small
  - [ ] Medium
  - [ ] Large

## Repository Description 

This project converts a Python script that adds passwords to a batch of PDF files into a standalone executable (`.exe`). Follow the steps below to build one yourself.

Before you begin: Set up a clean virtual environment and install only the necessary dependencies so PyInstaller does not bundle unneeded packages from your global Python installation.

<u>Steps</u>:
1. Open your terminal and navigate to the project directory.
2. Activate the virtual environment where your script and its dependencies are installed.
3. Install PyInstaller: pip install pyinstaller
4. Build the executable: pyinstaller --onefile {your_program}.py

After running Step 4, PyInstaller generates a few new files and folders in your project directory. You can find your .exe inside the dist folder, and safely delete the temporary build folder and .spec file afterward.

## Installation 

### Python Development Tools

- Python 3
  - [Download and install Python 3 from python.org](https://www.python.org/downloads). 
- Python Package Installer/Manager `pip`
  - If you installed Python from [python.org](https://www.python.org), you should already have `pip`. If it is not installed, you can use the command `py -m ensurepip --default-pip` to bootstrap it from the standard library. If you are using Linux, you will have to [install the package manager separately](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/). You can find out more about the `pip` tool [here](https://pip.pypa.io/en/stable/getting-started/). 
- Text Editor and Integrated Development Environment (IDE)
  - [Download and install the text editor Notepad++](https://notepad-plus-plus.org/downloads). 
  - [Download and install the IDE Visual Studio Code (VS Code)](https://code.visualstudio.com/download). 
  - [Install the web-based app Jupyter Notebook with pip](https://jupyter.org/install#jupyter-notebook)
  - [Install the web-based IDE JupyterLab with pip](https://jupyter.org/install#jupyterlab)
  - [Install Anaconda to get Jupyter Notebook](https://docs.jupyter.org/en/latest/install/notebook-classic.html#installing-jupyter-using-anaconda-and-conda)
- Command-line interface (CLI) 
  - You can [install the open-source PowerShell on Windows, Linux and macOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) if you do not have or want to use a pre-installed CLI on your local machine. 

### Python Libraries

Check if you have Python installed using the command `python --version`, or simply, `python version`, in the CLI. [Git-clone the project repository from Github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to the local machine. Use the command `py -m pip install package_name` to install the necessary Python libraries. Check out [pip documentation](https://pip.pypa.io/en/stable/cli/pip_install/) to learn more about `pip install`. Check the top part of the `.py` script file for the list of libraries required. For example, you may need `requests` and `beautifulsoup4` libraries if you see the following lines in the top part of the script file: 
```
import requests
from bs4 import BeautifulSoup
```
If `pip` fails to locate the relevant packages, you may find it at [Python Package Index (PyPI)](https://pypi.org/). Use `python file_name.py` to run the script in a CLI. Or, use an IDE, such as VS Code, to run the script. There will usually be a [Run] button in the top right corner of the opened script file. 

## Credits 

### Contributors 

- [@dark-teal-coder](github.com/dark-teal-coder)

### References 

- [PyInstaller documentation](https://pyinstaller.org/en/stable/)

&nbsp;

*1st Completion Date: Nov 19, 2026*&emsp;
