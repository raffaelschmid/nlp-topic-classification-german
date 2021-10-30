# NLP Topic Classification (German)
## Development
The project structure follows this [convention](https://towardsdatascience.com/manage-your-data-science-project-structure-in-early-stage-95f91d4d0600).

### Google Cloud Notebook
Add the following line to ~/.ipython/profile_default/ipython_kernel_config.py:
```
c.InteractiveShellApp.exec_lines = [ 'import sys; sys.path.append("/home/jupyter/code/nlp-topic-classification-german")' ]
```

### Tasks

#### Setup
```
spacy download de_core_news_lg
```

#### Freeze
```
pip freeze > requirements.txt
```