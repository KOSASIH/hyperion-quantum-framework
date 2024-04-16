# hyperion/test/gate.py

def and_gate(x, y):
    """Perform AND operation on two bits."""
    return x & y

def or_gate(x, y):
    """Perform OR operation on two bits."""
    return x | y

def not_gate(x):
    """Perform NOT operation on a bit."""
    return not x

def xor_gate(x, y):
    """Perform XOR operation on two bits."""
    return x ^ y

def nand_gate(x, y):
    """Perform NAND operation on two bits."""
    return not (x & y)

def nor_gate(x, y):
    """Perform NOR operation on two bits."""
    return not (x | y)

def xnor_gate(x, y):
    """Perform XNOR operation on two bits."""
    return not (x ^ y)
