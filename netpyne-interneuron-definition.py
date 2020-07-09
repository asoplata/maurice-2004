from neuron import h


class InterneuronMaurice2004:
    """Definition of the (Maurice et al., 2004) interneuron cell.

    This is the definition for the interneuron cell from
    https://senselab.med.yale.edu/ModelDB/ShowModel?model=98005&file=/D2modulation/kv2_ch.mod#tabs-1
    but in the netpyne-compatible style of http://netpyne.org/advanced.html#import-mainen which is a Python
    implementation of http://senselab.med.yale.edu/ModelDB/showModel.cshtml?model=2488
    """

    def __init__(self):
        # self.synlist = []
        self._create_sections()
        self._define_geometry()
        self._connect_topology()
        self._define_biophysics()
        self._create_synapses()
        # self._create_netcon()
        # self.nclist = []

    def _create_sections(self):
        """Create the sections of the cell."""
        self.soma = h.Section(name='soma', cell=self)
        self.dend = [h.Section(name='dend[%d]' % i) for i in range(2)]
        pass

    def _connect_topology(self):
        pass

    def _define_geometry(self):
        pass

    def _define_biophysics(self):
        pass

    def _create_synapses(self):
        pass

    # def _create_synapses(self):
    #     """Add an exponentially decaying synapse """
    #     synsoma = h.ExpSyn(self.soma(0.5))
    #     synsoma.tau = 2
    #     synsoma.e = 0
    #     syndend = h.ExpSyn(self.dend(0.5))
    #     syndend.tau = 2
    #     syndend.e = 0
    #     self.synlist.append(synsoma) # synlist is defined in Cell
    #     self.synlist.append(syndend) # synlist is defined in Cell
    #
    # def _create_netcon(self, thresh=10):
    #     """ created netcon to record spikes """
    #     nc = h.NetCon(self.soma(0.5)._ref_v, None, sec=self.soma)
    #     nc.threshold = thresh
    #     return nc


soma = h.Section(name='soma')
soma.L = 20
soma.diam = 20
soma.Ra = 70

soma.insert('pas')
soma.insert('na_ch')
soma.insert('na2_ch')
soma.insert('kv2_ch')
soma.insert('kv4_ch')
soma.insert('kcnq_ch')
soma.insert('kir2_ch')
soma.insert('bk_ch')
soma.insert('sk_ch')
soma.insert('hcn12_ch')
soma.insert('hcn2_ch')
soma.insert('cal_ch')
soma.insert('cap_ch')
soma.insert('ca_ch')

for seg in soma:
    seg.pas.g = 0.001
    seg.pas.e = -55
    seg.na_ch.gbar = 0.4
    seg.na2_ch.gbar = 1
    seg.kv2_ch.gbar = 0.1
    seg.kv4_ch.gbar = 0.4
    seg.kcnq_ch.gbar = 0.002
    seg.kir2_ch.gbar = 0
    seg.bk_ch.gbar = 1
    seg.sk_ch.gbar = 0.003
    seg.hcn12_ch.gbar = 0
    seg.hcn2_ch.gbar = 0
    seg.cal_ch.gbar = 0.003
    seg.cap_ch.gbar = 5e-5

# Define the dendrites
dend = [h.Section(name='dend[%d]' % i) for i in range(2)]
dend[0].connect(soma(0), 0)
dend[1].connect(soma(1), 0)

for ii in 0, 1:
    dend[ii].L = 200
    dend[ii].diam = 2
    dend[ii].Ra = 70
    dend[ii].insert('pas')
    dend[ii].insert('na_ch')
    dend[ii].insert('na2_ch')
    dend[ii].insert('kv2_ch')
    dend[ii].insert('kv4_ch')
    dend[ii].insert('kcnq_ch')
    dend[ii].insert('kir2_ch')
    dend[ii].insert('bk_ch')
    dend[ii].insert('sk_ch')
    dend[ii].insert('hcn12_ch')
    dend[ii].insert('hcn2_ch')
    dend[ii].insert('cal_ch')
    dend[ii].insert('cap_ch')
    dend[ii].insert('ca_ch')

    for seg in dend[ii]:
        seg.pas.g = 0.001
        seg.pas.e = -55
        seg.na_ch.gbar = 0.1
        seg.na2_ch.gbar = 0.25
        seg.kv2_ch.gbar = 0.1
        seg.kv4_ch.gbar = 0.4
        seg.kcnq_ch.gbar = 0.0003
        seg.kir2_ch.gbar = 0
        seg.bk_ch.gbar = 1
        seg.sk_ch.gbar = 0.003
        seg.hcn12_ch.gbar = 0.01
        seg.hcn2_ch.gbar = 0.03
        seg.cal_ch.gbar = 0.003
        seg.cap_ch.gbar = 0

# Visualize the connectivity
h.topology()

# Define the stimulus
iosc = h.Icos(dend[0](0.5))
iosc.delay = 10  # [ms] delay until start of stim
iosc.f = 130  # [Hz] frequency of stim
iosc.amp = -0.05  # [nA] amplitude
# 200 cycles * 130 Hz = about 1.5 seconds of stim time
iosc.n = 200  # [cycles] number of cycles to run
#
# # What data to save
# v = h.Vector().record(soma(0.5)._ref_v)  # Membrane potential vector
# t = h.Vector().record(h._ref_t)
# stim = h.Vector().record(iosc._ref_i)
#
# # Setup and actually run the simulation
# h.finitialize(-55 * mV)
# h.celsius = 22
# h.load_file('stdrun.hoc')
# h.continuerun(5000 * ms)
# h.dt = 25 * ms
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
# # Saving data
# with open('data.csv', 'w') as f:
#     csv.writer(f).writerows(zip(t, v))
