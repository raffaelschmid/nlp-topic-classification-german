# NLP Topic Classification (German)

The purpose of this project was to accomplish an assignment that was given during the
[Advanced NLP](https://www.fhnw.ch/de/weiterbildung/technik/advanced-nlp) course at
[FHNW](https://www.fhnw.ch). The description of the assignment can be found in German
[here](./docs/00_project_assignment.pdf): the main idea was to train an NLP model doing topic classification based on a
dataset of [German News Articles](https://tblock.github.io/10kGNAD/).

The **project structure** follows the directory convention that can
befound [here](https://towardsdatascience.com/manage-your-data-science-project-structure-in-early-stage-95f91d4d0600)
with a the exception that source files are not located in /src folder. The reason for this is to not have src in import
statements `import src.reporting` nor to deviate from Pip defaults.

| Folder         | Description                                                                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /data          | Storage location for data. Raw data is downloaded into /raw and after some processing stored into /processed.                                              |
| /docs          | Documentation that is not part of the code.                                                                                                                |
| /models        | Location for trained models stored in binary format.                                                                                                       |
| /notebooks     | Jupyter notebooks are stored in the eda (Exploratory Data Analysis), poc (Proof of concepts), modeling (Modeling) and evaluation (Evaluation) directories. |
| /preprocessing | Extracted Python code that is used during data preprocessing.                                                                                              |
| /reporting     | Extracted Python code that is used during reporting.                                                                                                       |
| /tests         | Module tests                                                                                                                                               |

## Procedure

### Exploratory Data Analysis

The dataset consists of roughly 10000 news articles that are classified in "Sport", "Kultur", "Web", "Wirtschaft", "
Inland", "Etat", "International", "Panorama" and "Wissenschaft". The dataset was given to us in form of two datasets for
training and testing.

I did Exploratory Data Analysis by [analyzing categories](./notebook/eda/01_analyze_categories.ipynb) and
ensure [language consistency](./notebook/eda/02_analyze_language.ipynb). More information can be found in the
correspondent notebooks.

## Modeling

The modeling phase was started with [data normalization](./notebook/modeling/01_normalization.ipynb) where the raw
dataset was processed and enriched by a tokenized, lemmatized and stemmed version. I decided to join the given training
and test dataset together in order to produce an additional validation set at a [later stage](./notebook/modeling/). I
decided for a 70% (training) / 20% (test) / 10% (validation) split.

### Base Model

We were told that a base Model based on TF-IDF is a proper industry standard. This notebook can be
found [here](./notebook/modeling/).

### CNN

### RNN

### Transformers (BERT)

## Learnings

### Refactoring

It was hard to refactor the notebooks into normal python files due to several reasons:

- Preprocessing (cleaning, tokenization, etc.) and training are highly coupled and its hard to find a good way to
  extract code while keeping the flexibility for training different models. E.g. TF-IDF needs much different
  preprocessing (lemmatization, stemming, etc.) than RNNs, CNNs or transformers where e.g. word vectors might be used.
- Jupyter Kernel does a bad job by default in reloading extracted modules.

## Development

### Setup

#### GCP Vertex Workbench

1. Generate ssh key for checkout

```
ssh-keygen -t rsa -b 4096 -C "raffael.schmid@students.fhwn.ch"
```

2. Clone Project

```
git clone git@github.com:raffaelschmid/nlp-topic-classification-german.git ~/code/nlp-topic-classification-german
```

3. Add the following line to ~/.ipython/profile_default/ipython_kernel_config.py:

```
c.InteractiveShellApp.exec_lines = [ 'import sys; sys.path.append("/home/jupyter/code/nlp-topic-classification-german")' ]
```

#### Freeze Dependencies

The setup was done using pip, project requirements should be stored using requirements.txt. In case of adding dependency
use the following command:

```
# Attention: within fully equiped GCP template containers this might get big. 
pip freeze > requirements.txt
```