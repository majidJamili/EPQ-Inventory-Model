import math
import pandas as pd
import numpy as np

df = pd.read_csv('models_demand_costs.csv')

data = pd.DataFrame(df, columns=['product', 'demand'])


class Inventory(): 
        def __init__(self, demand,production_rate, fixed_cost, hold_cost, model):
            self.demand = demand                         #Demand [Unit]
            self.p_rate = production_rate if production_rate is not None else 0             #Production Capacity [Unit/Year]
            self.f_cost = fixed_cost                          # Production Setup Costs
            self.h_cost = hold_cost                          #Unit Holding/Inventory Cost [Unit/Year]
                                                                        
            self.data = []                                           # In case, storing data needed 
            self.work_days = 365                             #number of days in a year
            self.model = str(model) 
        
        def optimum_quantity(self):
                match self.model:
                        case 'epq':
                                return round(math.sqrt((2*self.demand*self.f_cost )/ (self.h_cost*(1- (self.demand/self.p_rate)))))
                        case 'eoq':
                                return round(math.sqrt((2*self.demand*self.f_cost)/self.h_cost))
                

        def get_total_cycle(self):
                return round((self.optimum_quantity() / self.demand)*self.work_days)
        def get_production_cycle(self):
                return round((self.optimum_quantity() / self.p_rate)*self.work_days)
        def get_depletion_cycle(self):
                return round(((self.optimum_quantity()/self.demand) - (self.optimum_quantity()/self.p_rate))*self.work_days)    
        def num_prodcution_runs(self):
                return round(self.demand / self.optimum_quantity())
        def annual_setup_cost(self):
                return self.num_prodcution_runs() *self.f_cost
        def annual_holding_cost(self):
                match self.model:
                        case 'epq':
                                return (self.optimum_quantity()) * (1-(self.demand/self.p_rate))*self.h_cost
                        case 'eoq':
                                return (self.optimum_quantity()/2)*self.h_cost
        def total_cost(self):
                return  round(self.annual_holding_cost() + self.annual_setup_cost())
        
        def get_data(self):
                return [self.optimum_quantity(), self.get_total_cycle(), self.get_production_cycle(), 
                                self.get_depletion_cycle(),self.num_prodcution_runs(), self.annual_setup_cost(), 
                                self.annual_holding_cost(), self.total_cost()]
          

print(Inventory(260,1000,3000,250,'epq').get_data())
          



def generate_output(model, demand ):
        return [model] + [demand] + Inventory(demand, 1000, 5000, 340,'epq').get_data()


result_data = list(map(generate_output, data["product"], data["demand"]))
output = pd.DataFrame(result_data, columns=['model','demand','optimal_quantity', 'total_cycle', 'production_cycle', 'depletion_cycle', 'runs', 'setup', 'holding', 'total' ])


output.to_csv("optimized_inventory_model.csv",index=False)
