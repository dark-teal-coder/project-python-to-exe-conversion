Before building the executable, we should set up a clean environment so PyInstaller does not bundle unnecessary packages from the global Python installation. Here we use a virtual environment to install only the necessary libraries. 

### Steps:
1. In your terminal, navigate to the project directory. 
2. Activate your virtual environment where your script and its dependencies are installed
3. Install PyInstaller using this command: `pip install pyinstaller`
4. In your terminal, type the following command to build the EXE file: 
```
pyinstaller --onefile {your_program}.py
```

After step 4, PyInstaller creates a few new items in your project directory. The .exe file will be generated in "dist" folder. You can delete the temporary "build" folder and .spec file. 