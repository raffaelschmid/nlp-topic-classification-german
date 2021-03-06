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
| /data          | Storage location for data. Raw data is downloaded to raw, after processing stored to processed. Trained models are stored in model subdirectory.           |
| /docs          | Documentation that is not part of the code.                                                                                                                |
| /models        | Location for model definitions.                                                                                                                            |
| /notebooks     | Jupyter notebooks are stored in the eda (Exploratory Data Analysis), modeling (Modeling) and evaluation (Evaluation) directories.                          |
| /preprocessing | Extracted Python code that is used during data preprocessing.                                                                                              |
| /reporting     | Extracted Python code that is used during reporting.                                                                                                       |
| /tests         | Module tests                                                                                                                                               |

## Project
### Exploratory Data Analysis

The dataset consists of roughly 10000 news articles that were classified in "Sport", "Kultur", "Web", "Wirtschaft",
"Inland", "Etat", "International", "Panorama" and "Wissenschaft". The dataset was given to us in form of two datasets
for training and testing.

I did Exploratory Data Analysis by analyzing [detail data](./notebook/eda/01_example_data.ipynb),
[missing data](./notebook/eda/02_missing_data.ipynb), [categories](./notebook/eda/03_analyze_categories.ipynb),
[text length](./notebook/eda/04_analyze_text_length.ipynb), [language](./notebook/eda/05_analyze_language.ipynb) and
looking at [word clouds](./notebook/eda/06_word_cloud.ipynb).

### Modeling

The modeling phase was started with [join datasets](./notebook/modeling/00_join.ipynb) where the given datasets (
training, test) were joined into a single one. Based on the class distribution
I [augmented some small amount of data](./notebook/modeling/01_augmentation.ipynb) to tackle class inbalance.
Then [tokenization, stemming, lemmatization](./notebook/modeling/02_preprocessing.ipynb) was done followed by the
[stratified split](./notebook/modeling/03_split.ipynb) into training, test and validation data.

#### Base Model

We were told that a base Model based on TF-IDF is a proper standard. This notebook can be
found [here](./notebook/modeling/04_base_model.ipynb).

#### CNN

The [first model](./notebook/modeling/05_cnn.ipynb) was a Convolutional Neural Network using fasttext word embeddings
and a convolutional layer.

#### RNN

The [second model](./notebook/modeling/06a_rnn.ipynb) was a Recurrent Neural Network using fasttext word embeddings
and an LSTM layer. I tried to do some tuning
in [based on tensorflow utilities](./notebook/modeling/06b_rnn-tuning.ipynb).

#### Transformers (BERT)

In the end I [ended up](./notebook/modeling/07_bert.ipynb) using a transformer based BERT model
from [huggingface](https://huggingface.co/bert-base-german-cased).

### Evaluation

For every model I persisted a sample file (e.g. [BERT](./data/processed/report_data_bert.json)) that contained two
arrays of a) predictions and b) expectations. This allowed me to analyse and compare the different models later on
in [Evaluation](./notebook/evaluation/02_evaluation.ipynb) while also calculating different metrics based on that data.

### Conclusion

#### Project Structure

It was hard to refactor the notebooks into normal python files due to several reasons:

- Preprocessing (cleaning, tokenization, etc.) and training are highly coupled and its hard to find a good way to
  extract code while keeping the flexibility for training different models. E.g. TF-IDF needs much different
  preprocessing (lemmatization, stemming, etc.) than RNNs, CNNs (word vectors) or transformers (pretrained tokenizers).
- Reloading: Reloading code that is outside Jupyter notebooks often requires restarting of kernel which makes it even
  harder to refactor.

#### Version Control

It is a nice feature of Jupyter notebooks that cell outputs are stored within the files because it makes it easy to
share and review files. Those cells however can be very annoying when put under version control due to the fact that
upon almost every run changes are detected. An option would be to
use [Git smudge filters](https://nbsphinx.readthedocs.io/en/latest/usage.html#Using-Notebooks-with-Git), however this
would make our notebooks not reviewable anymore.

#### Libraries

During preprocessing and training I was using different libraries: sklearn (data split, base model), tensorflow (RNN,
CNN, Bert). It felt a bit awkward to train a model using tensorflow and evaluate it using sklearn libraries (sklearn
confusion_matrix), I was aiming for using either one or the other.

#### GCP Vertex

I was using a Vertex AI workbench on Google Cloud Platform to code and train. My laptop does not have a suitable GPU and
GCP provides GPU support for a decent amount of money. Additionally it lets you connect
with [Github](https://github.com) repositories and kind of lets you follow proper development and project standards.

While using Vertex workbenches I experienced different issues:

1. Stopping instances after work is a bad idea due to the fact that you might get into the problem of reallocating GPU
   resources.
2. Even when continuously running the Workbench I was running into an automatic instance update where my boot disk got
   lost.

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

c.InteractiveShellApp.exec_lines
= [ 'import sys; sys.path.append("/home/jupyter/code/nlp-topic-classification-german")' ]

```

#### Freeze Dependencies

The setup was done using pip, project requirements should be stored using requirements.txt. In case of adding dependency
use the following command:

```

# Attention: within fully equiped GCP template containers this might get big.

pip freeze > requirements.txt

```