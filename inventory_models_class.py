import math
import pandas as pd
import numpy as np

df = pd.read_csv('models_demand_costs.csv')

data = pd.DataFrame(df, columns=['product', 'demand'])


class Inventory(): 
        def __init__(self, demand, production_rate,fixed_cost, hold_cost ):
            self.demand = demand                       #Demand [Unit]
            self.p_rate = production_rate              #Production Capacity [Unit/Year]
            self.f_cost = fixed_cost                       # Production Setup Costs
            self.h_cost = hold_cost                       #Unit Holding/Inventory Cost [Unit/Year]
            self.data = []                                        # In case, storing data needed 
            self.work_days = 365                         #number of days in a year
        
        def get_epq(self):
                return  round(math.sqrt((2*self.demand*self.f_cost )/ (self.h_cost*(1- (self.demand/self.p_rate)))))    
        def get_total_cycle(self):
                return round((self.get_epq() / self.demand)*self.work_days)
        def get_production_cycle(self):
                return round((self.get_epq() / self.p_rate)*self.work_days)
        def get_depletion_cycle(self):
                return round(((self.get_epq()/self.demand) - (self.get_epq()/self.p_rate))*self.work_days)    
        def num_prodcution_runs(self):
                return round(self.demand / self.get_epq())
        def annual_setup_cost(self):
                return self.num_prodcution_runs() *self.f_cost
        def annual_holding_cost(self):
                return (self.get_epq()) * (1-(self.demand/self.p_rate))*self.h_cost
        def total_cost(self):
                return  round(self.annual_holding_cost() + self.annual_setup_cost())
        
        def get_data(self):
                return [self.get_epq(), self.get_total_cycle(), self.get_production_cycle(), 
                                self.get_depletion_cycle(),self.num_prodcution_runs(), self.annual_setup_cost(), 
                                self.annual_holding_cost(), self.total_cost()]
          

          

def generate_output(model, demand ):
        return [model] + [demand] + Inventory(demand, 1000, 5000, 340).get_data()


result_data = list(map(generate_output, data["product"], data["demand"]))
output = pd.DataFrame(result_data, columns=['model','demand','epq', 'total_cycle', 'production_cycle', 'depletion_cycle', 'runs', 'setup', 'holding', 'total' ])


#output.to_csv("EPQ.csv",index=False)
