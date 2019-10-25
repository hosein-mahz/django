# django

## Installation

### A) VirualEnv

    $ pip install virtualenv
    $ virtualenv --always-copy VENV


## Tips

### 1) Query in Many to Many

    Profile.objects.get(id=1).caffe_set.all()