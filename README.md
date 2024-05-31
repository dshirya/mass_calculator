# mass_calculator
Universal tool for calculating the mass of each element from a known substance formula

**Overview**
This project is a Python script that calculates the masses of elements in chemical formulas. It supports multiple input methods and batch processing, outputting results to an Excel file. The script can handle input from direct user entry, pasted text, .txt files, and .xlsx files.

**Usage**

**Running the Script**
Run the main.py script.

**Input Methods**
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

**After Processing**
After processing, you will be asked if you want to finish the calculation. Type 'Y' to finish or 'N' to return to the input method selection menu.


