import simpy
env = simpy.Environment()

def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print('starting driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)


env.process(car(env))

env.run(until=15)
