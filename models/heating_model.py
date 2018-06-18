class Heating_Model:

    """
    Heating model
    Parameters: P_nom
    Input: Heating_ON_OFF
    Output: P_heating
    """
    def __init__(self,P_nom):
        self.P_nom = P_nom
        self.Heating_ON_OFF = 0
        self.P_heating = 0

    def step(self):
        self.P_heating = self.P_nom * self.Heating_ON_OFF