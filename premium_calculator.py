# premium_calculator.py

def extractData(data, key):
    return data.get(key)


def lookupValue(table, key, valueKey):
    return table.get(key).get(valueKey)


def applyFormula(baseRate, riskMultiplier, coverage):
    return baseRate * riskMultiplier * coverage * 0.01


def premiumCalculator(userProfile, ratesTable, riskTable):
    age = extractData(userProfile, "age")
    location = extractData(userProfile, "location")
    coverage = extractData(userProfile, "coverage")

    baseRate = lookupValue(ratesTable, location, "baseRate")
    riskMultiplier = lookupValue(riskTable, age, "riskMultiplier")

    premium = applyFormula(baseRate, riskMultiplier, coverage)
    return premium


# Sample execution
if __name__ == "__main__":
    userProfile = {
        "age": 30,
        "location": "Bangalore",
        "coverage": 500000
    }

    ratesTable = {
        "Bangalore": {"baseRate": 3.5},
        "Mumbai": {"baseRate": 4.0}
    }

    riskTable = {
        30: {"riskMultiplier": 1.2},
        45: {"riskMultiplier": 1.5}
    }

    result = premiumCalculator(userProfile, ratesTable, riskTable)
    print("Calculated Premium:", result)
