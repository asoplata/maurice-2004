# maurice-2004-code
Copy of (Maurice et al., 2004) code for [NEURON](https://neuron.yale.edu/neuron/) and [NetPyNE](http://netpyne.org/index.html) beginners

This is a copy of the NEURON code available on ModelDB at
http://modeldb.yale.edu/98005
corresponding to part of the work in the following paper:

> Maurice N, Mercer J, Chan CS, Hernandez-Lopez S, Held J, Tkatch T, Surmeier DJ
> (2004) D2 dopamine receptor-mediated modulation of voltage-dependent Na+
> channels reduces autonomous activity in striatal cholinergic interneurons. J
> Neurosci 24:10289-301

`mosinit.hoc` is the original file used to perform the simulation in native
NEURON, `init.py` is a translation of the original simulation code for use with
the Python interface of NEURON, and either `netpyne_init.py` or
`netpyne_batch.py` in the folder `netpyne-batch-running` can be used to run
another translation of this code using the powerful NetPyNE interface to
NEURON. For the original Readme, see the file `readme.txt`. I am not one of the
original authors of this code, but it was published open source and unlicensed,
so let me know if there's a problem.

## Instructions

The easiest way to get started that works ANYWHERE is:

1. Install Anaconda from here: https://www.anaconda.com/products/individual and restart your computer afterwards.
2. Open up a Terminal/Command-line window.
3. Create a compatible "conda" environment with Python 3.7 using a command similar to

`conda create --name=neuro python=3.7`

4. From now on, you will have to enter or "activate" this environment when you want to use it via

`conda activate neuro`

Do this now. Afterwards, you should now see something like `(neuro)` to the left of your command prompt every time it appears.

5. If on Linux, install a necessary library by running `conda install gxx_linux-64`. If on Windows or Mac/OS X, try installing a similar library via `conda install clangxx`; I'm not sure whether or not the non-Linux solution will work.
6. Now, install the Python package for NEURON using

`pip install neuron`

7. Use the command `cd` to Change Directory into where you've downloaded this model.
8. Run the command `nrnivmodl`. It should spit out a bunch of text and create a bunch of compiled files in a folder called `x86_64`. This is it compiling the mechanisms, but not the sim code itself.
9. If you want to run the original model code, run `nrngui mosinit.hoc`, or if you want to run the native Python implementation, run `nrniv init.py`.

### SCC Cluster / NetPyNE

If you want to use NetPyNE's support of automatic batch job distribution on the [SCC cluster](https://www.bu.edu/tech/support/research/system-usage/scc-quickstart/), there's a couple extra steps:

1. First, let's get Anaconda working on the cluster, where it's already pre-installed, but must be configured (following https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/anaconda/ ). Create a folder called `conda_envs` in your personal `/projectnb` directory, i.e. at `/projectnb/<your_project_name>/<your_user_name>/conda_envs`.
2. Open either your `.bashrc`, `.bash_profile`, or `.profile` file, whichever you already have in your home directory (you may have to select View > Show Hidden Files to see these files), and add the following lines anywhere, filling in the location of the folder you just created:

```
module load miniconda/4.7.5
module load openmpi/3.1.4
export PATH=$PATH:/projectnb/<your_project_name>/<your_user_name>/conda_envs
```

3. Now open up a NEW Terminal window.
4. Follow steps 3-5 from the previous section (including installing the Linux library).
5. Instead of just installing NEURON with `pip install neuron`, instead run `pip install neuron netpyne` to also install NetPyNE.
6. `cd` to to `netpyne-batch-running` subfolder of this code.
7. Follow step 8 from the previous section.
8. Now you can run the batch job submission and simulation by running `python netpyne_batch.py`! After the jobs complete, you can run `python netpyne_analysis.py` to compare the different simulations!
