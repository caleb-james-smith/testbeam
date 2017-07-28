import matplotlib.pyplot as plt
import numpy as np
import imageio

def makeGif(name):
  directory = name
  name = name + '/' + name
  filenames = name + '.txt'
  gifname   = name + '.gif'
  print filenames
  with open(filenames,'r') as fn:
    #with imageio.get_writer(gifname, mode='I',duration=0.01) as writer:
    with imageio.get_writer(gifname, mode='I', fps=1000) as writer:
      for filename in fn:
        filename = filename.split('\n')[0]
        filename = directory + '/' + filename
        print filename
        image = imageio.imread(filename)
        writer.append_data(image)

if __name__ == "__main__":
  makeGif("eta_scan_phi_5")
