""" Meltdown Mitigation exercise """


def is_criticality_balanced(temperature, neutrons_emitted):
    
    return temperature < 800 and neutrons_emitted > 500 and neutrons_emitted * temperature < 500000
        


def reactor_efficiency(voltage, current, theoretical_max_power):
    

    generated_power = voltage * current
    efficiency = generated_power / theoretical_max_power * 100
    if efficiency >= 80:
        return "green"
    elif 80 > efficiency >= 60:
        return "orange"
    elif 60 > efficiency >= 30:
        return "red"
    elif 30 > efficiency:
        return "black"
    else: 
        return "error"
    


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    
    product = temperature * neutrons_produced_per_second
    if 1.1 >=product/threshold >= 0.9:
        return "NORMAL"
    elif  product/threshold < 0.9:
        return "LOW"
    else :
        return "DANGER"
