import ast
import os

PROJECT_ID = os.environ.get('PROJECT_ID')
TABLE_ID = os.environ.get('TABLE')
DATASET_ID = os.environ.get('DATASET')
LOCAL_RUN = ast.literal_eval(os.environ.get('LOCAL_RUN', 'True'))