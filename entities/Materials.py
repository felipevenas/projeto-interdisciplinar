class Materials:
    def __init__(self):
        self.plastic = 0.50  # Valor por unidade de garrafa plástica
        self.aluminium = 0.80  # Valor por unidade de lata de alumínio
        self.paper = 0.20  # Valor por unidade de papel ou revista

    def get_plastic(self):
        return self.plastic

    def get_aluminium(self):
        return self.aluminium

    def get_paper(self):
        return self.paper