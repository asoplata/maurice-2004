
# Some, but not all, of this is from https://neuron.yale.edu/neuron/docs/scripting-neuron-basics

import csv
import matplotlib.pyplot as plt

from neuron import h
from neuron.units import ms, mV

import numpy as np

# Define the soma
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
dend[0].connect(soma(0),0)
dend[1].connect(soma(1),0)

for ii in 0,1:
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
iosc.delay = 10 # [ms] delay until start of stim
iosc.f = 130 # [Hz] frequency of stim
iosc.amp = -0.05 # [nA] amplitude
# 200 cycles * 130 Hz = about 1.5 seconds of stim time
iosc.n = 200 # [cycles] number of cycles to run

# What data to save
v = h.Vector().record(soma(0.5)._ref_v)             # Membrane potential vector
t = h.Vector().record(h._ref_t)
stim = h.Vector().record(iosc._ref_i)

# Setup and actually run the simulation
h.finitialize(-55 * mV)
h.celsius = 22
h.load_file('stdrun.hoc')
h.continuerun(5000 * ms)
h.dt = 25*ms
h.steps_per_ms = 4

# Plotting
plt.figure()
plt.plot(t, v)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.show()

plt.figure()
plt.plot(t, stim)
plt.xlabel('t (ms)')
plt.ylabel('stim (nA)')
plt.show()


# Saving data
with open('data.csv', 'w') as f:
    csv.writer(f).writerows(zip(t, v))
