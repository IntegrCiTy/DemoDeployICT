class Control_Model:

    """
    Controller model
    Parameters: T_set, deltaT
    Input: T_int
    Output: Heating_ON_OFF
    """
    def __init__(self,T_set, deltaT):
        self.T_set = T_set
        self.deltaT = deltaT
        self.T_int = None
        self.Heating_ON_OFF = 0

    def step(self):
        if self.T_int < self.T_set - self.deltaT:
            if self.Heating_ON_OFF==0:
                self.Heating_ON_OFF = 1
        if self.T_int > self.T_set + self.deltaT:
            if self.Heating_ON_OFF == 1:
                self.Heating_ON_OFF = 0


