# Install

Complete all these steps in the same terminal or command line window.

1.  Download and install a Python virtual environment manager.  I use [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) but any equivalent tool will work.
2.  Open a command line/terminal and create a new virtual environment (venv).  For Miniconda I run this command:
```shell
conda create --name zombie-diplo python=3.11
```
3.  Activate the environment in your current terminal: `conda activate zombie-diplo`.  You must always have the venv activated whenever building the map or installing additional Python packages.
4.  Install [RichChk](https://github.com/sethmachine/richchk):
    * Clone or download its repo: `git clone https://github.com/sethmachine/richchk.git`
    * Enter the cloned repo folder on command line, e.g. `cd richchk/`
    * Install via `pip install src/ --upgrade`

# Build

To build the map, run `scripts/build_map.py`.  This script will take an input .SCX/.SCM map file and output a new .SCX/.SCM map file that combines the terrain with the triggers, unit settings, etc.  Use the output map as the playable version and for testing.

1.  Install the `zombie_diplo` package if running from the terminal, e.g. `pip install src/ --upgrade`, or wherever `src/zombie_diplo` folder is located.
2.  If you are using an IDE like IntelliJ, just make sure the `zombie_diplo` package is on the Python path.
3.  To change where the output map is located, change `OUTFILE` to where you want it to go.  Same with `MAPFILE`
4.  Run the script: `python scripts/build_map.py`

# How to update

* Create new triggers in `zombie_diplo/systems`


