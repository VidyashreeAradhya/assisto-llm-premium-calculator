# Assisto Technologies – LLM Assignment

## Task Selected  
**Premium Calculator**

## Description  
This project calculates an insurance premium using a modular, data-driven approach inspired by primitive LLM-style operations such as data extraction, value lookup, and formula application.

The focus is on clean logic separation, reusability, and clarity, without unnecessary over-engineering.

## Functions Used  

- **extract_data()** – Extracts required values from user input  
- **lookup_value()** – Fetches the base rate and risk multiplier from lookup tables  
- **apply_formula()** – Applies the premium calculation formula  
- **premium_calculator()** – Integrates all functions to compute the final premium  

## Premium Formula  

Premium = base_rate × risk_multiplier × coverage × 0.01

## Sample Input  

- Age: 30  
- Location: Bangalore  
- Coverage: 500000  

## Sample Output  

Calculated Premium: 21000


## How to Run (CLI Mode)  

python premium_calculator.py


## User Interface (GUI)

The project also includes a simple graphical user interface built using **Tkinter**.
This allows users to calculate the insurance premium by entering age and coverage values without using the command line.

The GUI interacts with the core calculation logic and displays the computed premium dynamically within the application window.


## How to Run (GUI Mode)

python premium_calculator_gui.py
