import pandas as pd
import numpy as np
import networkx as nx
def read_file(file_name, method='Excel'):
    """
    Reads a file and returns a list
    """
    if method == 'Excel':
        source_file = file_name
        source_data = pd.read_excel(source_file , header=None)
        target_data = source_data.values.tolist()
        return target_data
    elif method == 'CSV':
        source_file = file_name
        source_data = pd.read_csv(source_file , header=None)
        target_data = source_data.values.tolist()
        return target_data

enter = []
leave = []
press = []
move  = []



network = nx.Graph()