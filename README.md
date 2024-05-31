# Mass calculator


## **Overview**
This project is a Python script that calculates the masses of elements in chemical formulas. For example, you want to calculate how much of each element you need to take to synthesize a compound with a known ratio of substances.
```
We have to make 0.2g of GdOsIn
So this script will calculate how much of each element you should take:

Element masses:
Gd: 0.0680 g
Os: 0.0823 g
In: 0.0497 g
Total mass: 0.2 g
```
It supports multiple input methods and batch processing, outputting results to an Excel file. The script can handle input from direct user entry, pasted text, .txt files, and .xlsx files.

## **Usage**

**Running the Script** : run the `main.py` script.

### **Input Methods**
1. Enter the chemical formula
You will be prompted to enter a chemical formula and the total mass of the mixture.
The script will calculate and display the masses of each element.
2. Paste column of text with formulas
You will be prompted to paste a column of formulas and type 'done' when finished.
The script will process these formulas and generate an Excel file with the results.
3. Read from txt file with formulas
The script will list all .txt files in the current directory.
Choose a file by its number.
The script will process the formulas from the file and generate an Excel file with the results.
4. Read from Excel file with formulas
The script will list all .xlsx files in the current directory.
Choose a file by its number.
The script will process the formulas from the file and generate an Excel file with the results.

### **Output adjustment**
By default as an output for the options 2-4 it calculates the masses for the mixtures of 0.1g, 0.15g, 0.2g, 0.25g, 0.3g, 0,4g, 0,5g

If you want to change it you can do so in the `unil/batch_processing.py` by changing the numbers in the 7th string:
```
def process_formulas(formulas, filename, total_masses=[0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]):  # change total mass here if needed
```


### **After Processing**
After processing, you will be asked if you want to finish the calculation. Type 'Y' to finish or 'N' to return to the input method selection menu.


