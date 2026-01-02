# Assisto Technologies – LLM Assignment

## Task Selected
Premium Calculator

## Description
This task calculates an insurance premium using primitive LLM-style functions such as data extraction, lookup, and formula application.

## Functions Used
- extractData(): Extracts required values from user input
- lookupValue(): Fetches base rate and risk multiplier
- applyFormula(): Applies premium calculation formula
- premiumCalculator(): Combines all functions to compute final premium

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
