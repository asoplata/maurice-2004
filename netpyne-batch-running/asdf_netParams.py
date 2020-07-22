from netpyne import specs, sim

# from netpyne_cfg import cfg

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

# Population parameters
netParams.popParams['Maurice_pop'] = {'cellType': 'IN', 'numCells': 1, 'cellModel': 'Maurice'}

# Cell property rules
# The label possibly doesn't matter, but the "conds" dict is important, and where you set how to identify the model
# for later use in "popParams"
cellRule = netParams.importCellParams(label='IN_Maurice_rule',
                                      conds={'cellType': 'IN', 'cellModel': 'Maurice'},
                                      fileName='netpyne_interneuron_definition.py',
                                      cellName='InterneuronMaurice2004')

netParams.defaultThreshold = -15  # [mV] spike detection threshold for rasters

# Synaptic mechanism parameters (used for stimulation, see below)
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
