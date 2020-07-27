from netpyne import specs
from netpyne.batch import Batch
import os


def batchInhWeight():
    # Create variable of type ordered dictionary (NetPyNE's customized version)
    params = specs.ODict()

    # Parameters and values to explore (corresponds to variable in simConfig)
    # params['synMechTau2'] = [3.0, 5.0, 7.0]
    # params['connWeight'] = [0.005, 0.01, 0.15]
    params['inhWeight'] = [0.01, 0.1, 0.5, 1.0, 1.5, 5.0, 10.0]
    params['inhRate'] = [10]

    # create Batch object with paramaters to modify, and model files to use
    b = Batch(params=params,
              cfgFile='netpyne_cfg.py',
              netParamsFile='netpyne_netParams.py')

    # Set output folder, optimization method, and run configuration
    b.batchLabel = 'inh_stim_exploration'
    # Note: folder prefix must already exist
    # save_folder_prefix = '/projectnb/crc-nak/asoplata/x7-scc-data/netpyne_batch_testing/'
    # b.saveFolder = save_folder_prefix + 'netpyne_batch_output_data'
    b.saveFolder = 'netpyne_batch_output_data'
    b.method = 'grid'
    # b.runCfg = {'type': 'mpi_bulletin',
    #             'script': 'netpyne_init.py',
    #             'skip': True}
    b.runCfg = {'type': 'hpc_torque',
                'script': 'netpyne_init.py',
                'skip': True,
                'custom': 'export PBS_O_WORKDIR=$SGE_O_WORKDIR'
                }


    # Run batch simulations
    b.run()


# Main code
if __name__ == '__main__':
    batchInhWeight()



