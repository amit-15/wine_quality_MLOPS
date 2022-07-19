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

touch src/get_data.py   #start working on get_data.py
                        #get_data add pushing changes

touch src/load_data.py

    # add stage in dvc.yaml file 

touch src/split_data.py

touch src/train_and_evaluate.py

mkdir report

touch report/scores.json
touch params/scores.json

dvc metrics show

dvc metrics diff

touch tox.ini

mkdir tests

touch tests/conftest.py tests/test_config.py

touch setup.py
pip install -e .

python setup.py sdist bdist_wheel