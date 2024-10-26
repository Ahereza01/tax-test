# tax_calculator.py

def calculate_tax(earnings):
    if earnings < 12000:
        return 0
    elif 12000 <= earnings <= 36000:
        return (earnings - 12000) * 0.2
    return 0

