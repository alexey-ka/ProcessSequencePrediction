import pandas as pd
from pathlib import Path
import os

root = Path(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/')
filename = str(root)+'/code/output_files/results/next_activity_and_time_helpdesk.csv'
print(filename)
file = (''+filename)
csv = pd.read_csv(filename)
groupd = csv.groupby(['Prefix length'])['MAE'].mean()
print(groupd/86400)
print(csv.mean()['MAE']/86400)
