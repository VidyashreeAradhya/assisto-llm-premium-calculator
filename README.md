# Assisto Technologies – LLM Assignment

## Task Selected
Premium Calculator

## Description
This project calculates an insurance premium using a modular, data-driven approach inspired by primitive LLM-style operations such as data extraction, lookup, and formula application.

The focus is on clean logic separation, reusability, and clarity rather than over-engineering.


## Functions Used
- **extractData()** – Extracts required values from user input  
- **lookupValue()** – Fetches base rate and risk multiplier from lookup tables  
- **applyFormula()** – Applies the premium calculation formula  
- **premiumCalculator()** – Combines all functions to compute the final premium  


## Premium Formula
Premium = baseRate × riskMultiplier × coverage × 0.01

## Sample Input
Age: 30  
Location: Bangalore  
Coverage: 500000  

## Sample Output
Calculated Premium: 21000

## How to Run
```bash
python premium_calculator.py



## User Interface (GUI)
The project also includes a simple graphical user interface built using **Tkinter**.  
This allows users to calculate the insurance premium by entering age and coverage values without using the command line.

The GUI interacts with the calculation logic and displays the computed premium dynamically within the application window.


##How to Run (GUI Mode)

python premium_calculator_gui.py


