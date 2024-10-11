import torch
import matplotlib.pyplot as plt

def plot_img(sample):
    x = sample['front_img']
    x = x.detach().cpu().permute(1,2,0).numpy()
    x = (x - x.min())/(x.max() - x.min())
    plt.imshow(x)

def plot_waypoint(sample):
    plt.scatter(sample['waypoints'][:,0],sample['waypoints'][:,1])
    plt.xlim([-10,10])