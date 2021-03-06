:Migliore file Modify by Maciej Lazarewicz (mailto:mlazarew@gmu.edu) May/16/2001

TITLE Borg-Graham type generic K-AHP channel

: SK for cholinergic interneuron

NEURON {
	SUFFIX sk_ch
	USEION k READ ek WRITE ik
        USEION ca READ cai
        RANGE  gbar,gkahp,ik
        GLOBAL inf,tau
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	celsius = 6.3	(degC)
	gbar	= .003 	(mho/cm2)
        n	= 4
        cai	= 50.e-6 (mM)
        a0	= 1.3e13 (/ms-mM-mM-mM-mM)	:b0/(1.4e-4^4)
        b0	= .5e-2  (/ms)			:0.5/(0.100e3)
        v       	 (mV)
        ek      	 (mV)
}

STATE {	w }

ASSIGNED {
	ik 		(mA/cm2)
        gkahp  		(mho/cm2)
        inf
        tau
}

BREAKPOINT {
	SOLVE state METHOD cnexp
	gkahp = gbar*w
	ik = gkahp*(v-ek)
}

INITIAL {
	rate(cai)
	w=inf
}

FUNCTION alp(cai (mM)) {
  alp = a0*cai^n
}

DERIVATIVE state {     : exact when v held constant; integrates over dt step
        rate(cai)
        w' = (inf - w)/tau
}

PROCEDURE rate(cai (mM)) { :callable from hoc
        LOCAL a
        a = alp(cai)
        tau = 1/(a + b0)
        inf = a*tau
}















