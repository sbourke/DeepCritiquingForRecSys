#!/usr/bin/env bash
source ~/ENV/bin/activate
cd ~/DeepCritiquingForRecSys
python tune_parameters.py --data_dir data/beer/ --save_path beer/encf.csv --parameters config/beer/encf.yml
