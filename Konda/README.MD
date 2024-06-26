# Konda

> This directory will have all your testing of making env with conda. Conda seems to be presinstalled with this code spaces

## Commands 

All commands here are referenced from the main docs [`Conda Official Docs`](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#viewing-a-list-of-your-environments)

Create a new env 
```sh 
conda create --name m1
```

List all envs 
```sh 
conda env list 
```

Initialize env - This is important before using conda. You can initialize for specific shells 
```sh
conda init fish
```


Activate Env 
```sh 
conda activate m1
```

List all installed packages in conda 
```sh 
# List all pkg
conda list

# If you want to see total lines 
conda list | wc -l 
```

Remove conda env 
```sh
conda remove --name m1 --all
```
- This will wip all panties