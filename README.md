First activate miniconda
```bash
module load miniconda
```
Then to install this software, please begin by setting up the conda environment first.
```bash
conda create --name bisection-environment python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate bisection-environment
```
Ensure that pip is using the most up to date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```
Create an editable install of the bisection method code (note: you must be in the correct directory):
```bash
pip install -e .
```
Test that the code is working with pytest:
```bash
pytest -v --cov=bisectionmethod --cov-report term-missing
```
