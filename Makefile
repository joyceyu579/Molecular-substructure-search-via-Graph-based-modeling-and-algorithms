lint:
	black .
	flake8 .

environment:
	conda create -n chem274A_final "python=3.11" --yes
	conda install -c conda-forge jupyterlab matplotlib networkx pytest argparse --name chem274A_final --yes

substructure_search:
	python UsingArgparse.py egcg.sdf benzene.sdf --help
	python UsingArgparse.py egcg.sdf benzene.sdf

testing:
	python -m pytest testcases.py -v

remove-env:
	conda remove --name chem274A_final --all --yes

.PHONY: lint environment remove-env