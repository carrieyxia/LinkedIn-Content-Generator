LinkedIn Content Creator
==============================



Project Organization
------------

    │
    ├── data/               <- The original, immutable data dump. 
    │
    ├── figures/            <- Figures saved by scripts or notebooks.
    │
    ├── notebooks/          <- Jupyter notebooks. Naming convention is a short `-` delimited 
    │                         description, a number (for ordering), and the creator's initials,
    │                        e.g. `initial-data-exploration-01-hg`.
    │
    ├── environment.yml     <- conda virtual environment definition file.
    │
    ├── LICENSE
    │
    ├── Makefile            <- Makefile with commands like `make environment`
    │
    ├── README.md           <- The top-level README for developers using this project.
    │
    └── tox.ini             <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</p>


Set up
------------

Install the virtual environment with conda and activate it:

```bash
$ conda env create -f environment.yml
$ conda activate example-project 
```

Install `linkedin_content_creator` in the virtual environment:

```bash
$ pip install --editable .
```
