from netpyne import specs

# Simulation options
cfg = specs.SimConfig()		# object of class SimConfig to store simulation configuration

cfg.duration = 1 * 1e3 	    # Duration of the simulation, in ms
cfg.dt = 0.025 				# Internal integration timestep to use
cfg.verbose = True  			# Show detailed messages
cfg.recordTraces = {'V_soma':{'sec': 'soma', 'loc':0.5, 'var': 'v'}}  # Dict with traces to record
# cfg.recordStim = True  # record spikes of cell stims
cfg.recordStep = 0.1 			# Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = 'netpyne_batch_output'  # Set folder output name
# cfg.saveFileStep = 1000  # step size in ms to save data to disk
cfg.saveJson = True
cfg.printPopAvgRates = True
cfg.analysis['plotRaster'] = {'saveFig': True} 			# Plot a raster
cfg.analysis['plotTraces'] = {'include': [0], 'saveFig': True} 			# Plot recorded traces for this list of cells

# # Variable parameters (used in netParams)
# cfg.synMechTau2 = 5
# cfg.connWeight = 0.01
cfg.inhWeight = 0.01
