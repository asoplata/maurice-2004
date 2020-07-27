from netpyne import specs
from netpyne.batch import Batch


def batchInhWeight():
    # Create variable of type ordered dictionary (NetPyNE's customized version)
    params = specs.ODict()

    # Parameters and values to explore (corresponds to variable in simConfig)
    # params['synMechTau2'] = [3.0, 5.0, 7.0]
    # params['connWeight'] = [0.005, 0.01, 0.15]
    params['inhWeight'] = [0.01, 0.025, 0.05, 0.1]

    # create Batch object with paramaters to modify, and model files to use
    b = Batch(params=params,
              cfgFile='netpyne_cfg.py',
              netParamsFile='netpyne_netParams.py')

    # Set output folder, optimization method, and run configuration
    b.batchLabel = 'inhWeight_exploration'
    # Note: folder prefix must already exist
    save_folder_prefix = '/projectnb/crc-nak/asoplata/x7-scc-data/netpyne_batch_testing/'
    b.saveFolder = save_folder_prefix + 'netpyne_batch_output_data'
    code_folder_prefix = '/usr3/graduate/asoplata/rep/maurice-2004/netpyne-batch-running/'
    b.method = 'grid'
    # b.runCfg = {'type': 'mpi_bulletin',
    #             'script': 'netpyne_init.py',
    #             'skip': True}
    b.runCfg = {'type': 'hpc_torque',
                'script': code_folder_prefix + 'netpyne_init.py',
                'skip': True}

    # Run batch simulations
    b.run()


# Main code
if __name__ == '__main__':
    batchInhWeight()



