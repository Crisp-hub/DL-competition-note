import torch
from torch.utils.data import Dataset,DataLoader
import torch.nn as nn
import torch.optim as optim

class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.label = labels
    def __len__(self):
        return len(self.data)
    def __getitem__(self,index):
        sample = self.data[index]
        label = self.labels[index]
        return sample,label

        
                 
        
        
        
        
        