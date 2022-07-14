conda create -n wine python=3.7 -y

conda activate wine

touch requirements.txt

touch README.md

touch template.py

pip install -r requirements.txt

python template.py

mkdir data_given

git init

dvc init

git add .

git commit -m "template created"

git remote add origin https://github.com/amit-15/wine_quality_MLOPS.git

git branch -M main

git push --force origin main

touch src/get_data.py  #start working on get_data.py