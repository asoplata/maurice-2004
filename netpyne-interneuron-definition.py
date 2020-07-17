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
        self.number_dendrites = 2
        self.dend = [h.Section(name='dend[%d]' % ii) for ii in range(self.number_dendrites)]

    def _connect_topology(self):
        self.dend[0].connect(self.soma(0), 0)
        self.dend[1].connect(self.soma(1), 0)

    def _define_geometry(self):
        """Set the 3D geometry of the cell."""
        self.soma.L = 20  # length of section, units: um
        self.soma.diam = 20  # diameter of section, units: um
        self.soma.Ra = 70  # axial resistivity, units: ohm * cm
        for ii in range(self.number_dendrites):
            self.dend[ii].L = 200  # length of section, units: um
            self.dend[ii].diam = 2  # diameter of section, units: um
            self.dend[ii].Ra = 70  # axial resistivity, units: ohm * cm

    def _define_biophysics(self):
        """Set the mechanisms and parameters of them in the cell."""
        self.soma.insert('pas')
        self.soma.insert('na_ch')
        self.soma.insert('na2_ch')
        self.soma.insert('kv2_ch')
        self.soma.insert('kv4_ch')
        self.soma.insert('kcnq_ch')
        self.soma.insert('kir2_ch')
        self.soma.insert('bk_ch')
        self.soma.insert('sk_ch')
        self.soma.insert('hcn12_ch')
        self.soma.insert('hcn2_ch')
        self.soma.insert('cal_ch')
        self.soma.insert('cap_ch')
        self.soma.insert('ca_ch')

        for seg in self.soma:
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

        for ii in range(self.number_dendrites):
            self.dend[ii].insert('pas')
            self.dend[ii].insert('na_ch')
            self.dend[ii].insert('na2_ch')
            self.dend[ii].insert('kv2_ch')
            self.dend[ii].insert('kv4_ch')
            self.dend[ii].insert('kcnq_ch')
            self.dend[ii].insert('kir2_ch')
            self.dend[ii].insert('bk_ch')
            self.dend[ii].insert('sk_ch')
            self.dend[ii].insert('hcn12_ch')
            self.dend[ii].insert('hcn2_ch')
            self.dend[ii].insert('cal_ch')
            self.dend[ii].insert('cap_ch')
            self.dend[ii].insert('ca_ch')

            for seg in self.dend[ii]:
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
