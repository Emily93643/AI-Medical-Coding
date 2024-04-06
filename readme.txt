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

docker pull qdrant/qdrant
docker run -p 6333:6333 -v ./qdrant_storage:/qdrant/storage:z qdrant/qdrant

    <title>AI-Powered Medical Coding Aid</title>
    <link href="{{ url_for('static', filename= 'styles/style.css')}}" rel ="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/jquery/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/bootstrap-table@1.22.3/dist/bootstrap-table.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://unpkg.com/bootstrap-table@1.22.3/dist/bootstrap-table.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap-table@1.22.3/dist/extensions/auto-refresh/bootstrap-table-auto-refresh.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tableexport.jquery.plugin@1.28.0/tableExport.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap-table@1.22.3/dist/extensions/export/bootstrap-table-export.min.js"></script>
