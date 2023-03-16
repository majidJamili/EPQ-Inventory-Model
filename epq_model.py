import math
demand = 260  # yearly demand
num_time_unit = 1 # Number of Weeks
production_rate = 1000 #weekly prodcution rate
setup_cost = 5000 #cost per production run
hold_cost = 120 # unit holding 



demand_w = demand /num_time_unit

# Econpmic Prodcution Quanitiy: 

def epq(d, p,k,h):
    return (math.sqrt((2*d*k )/ (h*(1- (d/p)))))
epq_value = epq(demand_w,production_rate,setup_cost,hold_cost)

print('EPQ:', round(epq_value))

#Production Run Cycle Length (Tp):
def production_len(q,p):
    return (q/p)

print('Production Only Length',round(production_len(epq_value,production_rate)*365), 'days')


#Demand Period Length (Td):
def deman_len(q,p,d):
    return ((q/d) - (q/p))

print('Inventory Holding Length: ',round(deman_len(epq_value,production_rate, demand)*365), 'days')


#Total Production Cycle Length

def total_len(q,d):
    return (q/d) 

print('Production Cycle Length',round( total_len(epq_value,demand)*360), 'days')

#Total Number of Production Runs:
def production_run(d,q):
    return round(d/q)


np = production_run(demand, epq_value)
print('Number of Production Run(s)',np)

#Annual Production Cost:
def annual_cost(np, k):
    return np*k
print(' Annual Fixed Costs',round(annual_cost(np,setup_cost)))




#Annual Holding Cost
def annual_hold_cost(q,d,p,h):
    return (q/2)*(1-(d/p))*h

hc = annual_hold_cost(epq_value, demand, production_rate, hold_cost)
print(' Annual Hold Costs',hc)



def annual_total_cost(a,b):
    return a + b
print(' Total Annual Cost',round(annual_total_cost(hc,annual_cost(np,setup_cost) )))



def max_inventory_level(q,d,p):
    return round(q*(1-(d/p)))
print('MAX Inventory level',max_inventory_level(epq_value, demand, production_rate))





