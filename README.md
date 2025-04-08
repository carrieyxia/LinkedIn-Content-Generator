## 🚀 Automating LinkedIn Job Post Generation with GPT-3.5-Turbo
This project explores automating the creation of LinkedIn job posts for recruiters using large language models (LLMs). While our recruitment SaaS platform already automates job distribution across boards, recruiters still manually write LinkedIn posts to share roles with their personal networks — a time-consuming and repetitive task.

We aimed to solve this with AI by comparing two approaches:
- Prompt Engineering using LangChain + GPT-3.5-Turbo
- Fine-Tuned GPT-3.5-Turbo on custom recruiter-style job post data

🔧 Tech Stack
- Python
- LangChain
-OpenAI GPT-3.5-Turbo (via both prompt + fine-tuning)

## 🧠 My Contributions
- Collected and curated the training dataset
- Built and evaluated both prompt-engineered and fine-tuned workflows
- Analyzed output quality and cost efficiency

📈 Outcome
- The fine-tuned model produced consistent, structured posts and was significantly more cost-effective during inference — supporting its adoption as a scalable product feature.


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
