COMMENT
icos.mod

Based on isin.mod, which is based on fsin.mod, which is derived from fzap.mod

Describes Icos, a point process class that delivers an oscillating current
i = amp * cos(2*PI*(t-delay)*f*(0.001))
which starts at t == delay and ends after n whole cycles
where
amp is peak amplitude in nA
t and delay are in ms
f is in Hz

User specifies amp, f, and n.

icos uses the event delivery system to ensure compatibility with adaptive integration.
ENDCOMMENT

NEURON {
  POINT_PROCESS Icos
  RANGE delay, f, amp, n, i
  ELECTRODE_CURRENT i
}

UNITS {
  PI = (pi) (1)
  (nA) = (nanoamp)
}

PARAMETER {
  delay (ms)
  f (1/s)  : frequency is in Hz
  amp (nA)
  n (1)
}

ASSIGNED {
  i (nA)
  on (1)
}

INITIAL {
  i = 0
  on = 0

  if (delay<0) { delay=0 }
  if (n<0) { n=0 }
  if (f<=0) { f=0 (1/s) }

  : do nothing if n or f == 0
  if ((n>0)&&(f>0)) {
    net_send(delay, 1)  : to turn it on
    net_send(delay+(n/f)*(1000), 1)  : to turn it off
  }
}

BREAKPOINT {
  if (on==0) {
    i = 0
  } else {
    i = amp * cos(2*PI*(t-delay)*f*(0.001))
  }
}

NET_RECEIVE (w) {
  : respond only to self-events with flag > 0
  if (flag == 1) {
    if (on==0) {
      on = 1  : turn it on
    } else {
      on = 0  : turn it off
    }
  }
}

COMMENT
for gcc 3.2.3
NET_RECEIVE (w) {
  : respond only to self-events with flag > 0
  if (flag != 0) {
VERBATIM
    on = (double)(on == 0.0);
ENDVERBATIM
  }
}
ENDCOMMENT
