# maurice-2004-code
Copy of (Maurice et al., 2004) code for NEURON beginners

This is a copy of the NEURON code available on ModelDB at
http://modeldb.yale.edu/98005
corresponding to part of the work in the following paper:

> Maurice N, Mercer J, Chan CS, Hernandez-Lopez S, Held J, Tkatch T, Surmeier DJ
> (2004) D2 dopamine receptor-mediated modulation of voltage-dependent Na+
> channels reduces autonomous activity in striatal cholinergic interneurons. J
> Neurosci 24:10289-301

The code has been only slightly modified to add an oscillatory current stimulus
and to make things easier for NEURON beginners to understand and use the model.
For the original Readme, see the file `readme.txt`. I am not one of the
original authors of this code, but it was published open source and unlicensed,
so let me know if there's a problem.

## Instructions

1. Install NEURON from here: https://neuron.yale.edu/neuron/download/ . As it says on the website, for Mac, you may also be required to install something like Xcode command line tools, in addition to a program called XQuartz.
2. Open up a NEW Terminal and use the command `cd` to Change Directory into where you've downloaded this model.
3. In the Terminal, run the command `nrnivmodl`. It should spit out a bunch of txt and create a bunch of compiled files in a folder called `x86_64`. This is it compiling the mechanisms, but not the sim code itself. If this doesn't work, then contact me and we'll have to debug it.
4. If you got this far, you should be able to run the original model using classic NEURON by running the command `nrngui mostinit.hoc` however I couldn't figure out how to save actually simulated data this way.
5. To try to use my Python script that does actually run the simulation and save your data (`init.py`), first test that you can access the NEURON python code. To do this, simply type `python` into the Terminal, which should give you a live python interpreter. Then, type `import neuron` and hit enter to see if it can access NEURON's Python code. If it gives an error, type `exit()` to exit the python prompt, then try a Python version 3 console by typing `python3` into the Terminal, and then repeating the `import neuron` command. If neither of those work, then contact me.
6. If either `python` or `python3` have the NEURON code, then use whichever version does and type in `python (or python3) init.py` and the simulation should run, spit out a plot that you will have to close, and after closing the last plot should save the voltage trace data into `data.csv`.
