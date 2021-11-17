# NLP Topic Classification (German)
## Development
The project structure follows this [convention](https://towardsdatascience.com/manage-your-data-science-project-structure-in-early-stage-95f91d4d0600).

### Google Cloud Notebook
###  Generate ssh key for checkout
```
ssh-keygen -t rsa -b 4096 -C "raffael.schmid@students.fhwn.ch"
```

Add the following line to ~/.ipython/profile_default/ipython_kernel_config.py:
```
c.InteractiveShellApp.exec_lines = [ 'import sys; sys.path.append("/home/jupyter/code/nlp-topic-classification-german")' ]
```

### Tasks
#### Freeze
```
pip freeze > requirements.txt
```