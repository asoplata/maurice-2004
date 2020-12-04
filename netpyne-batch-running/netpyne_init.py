
# Much of this is from http://netpyne.org/tutorial.html

# import csv
# import matplotlib.pyplot as plt
# from neuron import h
# from neuron.units import ms, mV
# import numpy as np
from netpyne import sim

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='netpyne_cfg.py', netParamsDefault='netpyne_netParams.py')

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)
# sim.checkOutput('netpyne-init')

# # Saving data
# with open('data.csv', 'w') as f:
#     csv.writer(f).writerows(zip(t, v))

