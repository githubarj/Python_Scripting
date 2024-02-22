# Python Scripting

### Task 

Write a Python script that scrapes data from https://kmpdc.go.ke/Registers/General_Practitioners.php and writes it into an Excel file.  

## Set up

Ensure that python iscorrectly set up in your system,  

```
python --version
```

If not kindly refer to the [Python Documentation](https://www.python.org/downloads/)

## Dependencies  

- BeautifulSoup
- pandas
- openpyxl
- requests

```
pip install requests beautifulsoup4 pandas openpyxl
```
install any more required depenencies.  

## Usage

Clone this repository.  
```
git clone https://github.com/githubarj/Python_Scripting.git
```

Make sure you are in the right directory.  
```
cd Python_Scripting
```

Run the script and the excel file will be saved in that same directory.  
```
python pythonScripting
```
or if you are using the terminal for wsl2 in vscode use : 
```
python3 pythonScripting
```