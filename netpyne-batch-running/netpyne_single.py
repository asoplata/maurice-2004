
# Much of this is from http://netpyne.org/tutorial.html

import csv
import matplotlib.pyplot as plt

# from neuron import h

# from neuron.units import ms, mV

# import numpy as np

from netpyne import specs, sim


# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

# The label possibly doesn't matter, but the "conds" dict is important, and where you set how to identify the model
# for later use in "popParams"
cellRule = netParams.importCellParams(label='IN_Maurice_rule',
                                      conds={'cellType': 'IN', 'cellModel': 'Maurice'},
                                      fileName='netpyne_interneuron_definition.py',
                                      cellName='InterneuronMaurice2004')

netParams.popParams['Maurice_pop'] = {'cellType': 'IN', 'numCells': 5, 'cellModel': 'Maurice'}
netParams.defaultThreshold = -15  # [mV] spike detection threshold for rasters

# Stimulation parameters
# First, define the syn mech
# Simple GABA-A mechanism loosely adapted from Destexhe's via this thread
# https://www.neuron.yale.edu/phpBB/viewtopic.php?t=2049
netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.2, 'tau2': 5.0, 'e': -80}
# Then setup the stim to use this syn mech
# TODO check rate unit conversion!!! text claims a rate of "10" may be "100 Hz"!!
netParams.stimSourceParams['bkg'] = {'type': 'NetStim',
                                     'rate': 10,
                                     'noise': 0.5}
# TODO what are the units of the weight? absolute conductance?
netParams.stimTargetParams['bkg->IN'] = {'source': 'bkg',
                                         'conds': {'cellType': 'IN', 'cellModel': 'Maurice'},
                                         'weight': 0.5,
                                         'delay': 5,

                                         'synMech': 'inh'}

###############################################################################
# SIMULATION PARAMETERS
###############################################################################
simConfig = specs.SimConfig()

# Simulation parameters
simConfig.duration = 1 * 1e3  # Duration of the simulation, in ms
simConfig.dt = 0.025  # Internal integration timestep to use
# simConfig.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
simConfig.verbose = False  # show detailed messages
# simConfig.hParams = {'v_init': -75}

# Recording
simConfig.recordCells = ['all']  # which cells to record from
simConfig.recordTraces = {'Vsoma': {'sec': 'soma', 'loc': 0.5, 'var': 'v'}}
simConfig.recordStim = True  # record spikes of cell stims
simConfig.recordStep = 0.1  # Step size in ms to save data (eg. V traces, LFP, etc)

# Saving
simConfig.filename = 'netpyne-single-output'  # Set file output name
simConfig.saveFileStep = 1000  # step size in ms to save data to disk
simConfig.savePickle = False  # Whether or not to write spikes etc. to a .mat file

# Analysis and plotting
simConfig.analysis['plotRaster'] = {'saveData': 'temp.json', 'saveFig': True}  # True  # Plot raster
simConfig.analysis['plotTraces'] = {'include': [0], 'saveFig': True}  # Plot raster
simConfig.analysis['plot2Dnet'] = True  # Plot 2D net cells and connections

sim.createSimulateAnalyze(netParams, simConfig)
# sim.checkOutput('netpyne-init')


#
#
#
# # Visualize the connectivity
# h.topology()
#
# # Define the stimulus
# iosc = h.Icos(dend[0](0.5))
# iosc.delay = 10 # [ms] delay until start of stim
# iosc.f = 130 # [Hz] frequency of stim
# iosc.amp = -0.05 # [nA] amplitude
# # 200 cycles * 130 Hz = about 1.5 seconds of stim time
# iosc.n = 200 # [cycles] number of cycles to run
#
# # What data to save
# v = h.Vector().record(soma(0.5)._ref_v)             # Membrane potential vector
# t = h.Vector().record(h._ref_t)
# stim = h.Vector().record(iosc._ref_i)
#
# # Setup and actually run the simulation
# h.finitialize(-55 * mV)
# h.celsius = 22
# h.load_file('stdrun.hoc')
# h.continuerun(5000 * ms)
# h.dt = 25*ms
# h.steps_per_ms = 4
#
# # Plotting
# plt.figure()
# plt.plot(t, v)
# plt.xlabel('t (ms)')
# plt.ylabel('v (mV)')
# plt.show()
#
# plt.figure()
# plt.plot(t, stim)
# plt.xlabel('t (ms)')
# plt.ylabel('stim (nA)')
# plt.show()
#
#
# # Saving data
# with open('data.csv', 'w') as f:
#     csv.writer(f).writerows(zip(t, v))
