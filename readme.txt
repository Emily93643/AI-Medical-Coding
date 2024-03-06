##Create a Python virtual environment (optional but recommended):
python -m venv venv

##source venv/bin/activate  
#On Windows, 
use: venv\Scripts\activate

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


