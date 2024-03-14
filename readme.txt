##Create a Python virtual environment (optional but recommended):
python -m venv .venv

##source .venv/bin/activate.csh  
#On Windows, 
use: .venv\Scripts\activate

##Install the required Python packages:
pip install -r requirements.txt

delete .git folder

git init
git add .
git commit -m 'Initial commit'
git push -u origin main

git remote add origin https://github.com/mxf20040518/AI-Medical-Coding.git
git remote set-url origin https://github.com/mxf20040518/AI-Medical-Coding.git
git branch -M main

##fix unrelated-histories issues
git pull origin main --allow-unrelated-histories

example: term= pulmonary infection llt: Lung infection
Column Names: ['term', 'llt_code', 'Cos_Sim', 'llt_name', 'pt_code', 'pt_name', 'hlt_name', 'hlgt_name', 'soc_name', 'hlt_code', 'hlgt_code', 'soc_code', 'soc_abbrev', 'pt_soc_code', 'aedesc', 'vernum']

Generate a requirements file and then install from it in another environment.
Windows:
env1\bin\python -m pip freeze > requirements.txt
env2\bin\python -m pip install -r requirements.txt