import simpy

env = simpy.Environment()

print(env.run(until=10))