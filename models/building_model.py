
import pandas as pd

class Building_Model:

    """
    Building model
    Parameters: U, C
    Input: P_heating
    Output: T_int
    """
    data = pd.Series([5,10,12,8]*7 + [5],index=pd.date_range('1/1/2011', periods=7*4+1, freq='6H'))

    def __init__(self, U, C, T_init=20.0):
        self.time = pd.to_datetime(self.data.index[0])
        self.U = U
        self.C = C
        self.T_ext = self.data.iloc[0]
        self.T_int = T_init
        self.P_heating = 0.0

    def step(self, Timestep, unit="seconds"):
        self.time += pd.DateOffset(**{unit:Timestep})
        self.T_ext = self.data.iloc[self.data.index.get_loc(self.time, method="nearest")]
        self.T_int = self.T_int + Timestep/self.C * (self.P_heating - self.U*(self.T_int - self.T_ext))

if __name__ == "__main__":
    b = Building_Model(200,50E6)
    b.P_heating = 20000
    b.step(3600)
    print(b.T_int)


