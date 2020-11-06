def number_str(x):
    """
    la fonction utilisée dans Quaternion.__repr__
    pour la mise en forme des nombres
    """
    if isinstance(x, int):
        return f"{x}"
    elif isinstance(x, float):
        return f"{x:.1f}"

class Quaternion:
    def __init__(self, a, b, c, d):
        pass
