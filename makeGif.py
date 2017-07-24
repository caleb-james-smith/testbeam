import matplotlib.pyplot as plt
import numpy as np
import imageio

def makeGif(name):
  filenames = name + '.txt'
  gifname = name + '.gif'
  with open(filenames,'r') as fn:
    with imageio.get_writer(gifname, mode='I',duration=1) as writer:
      for filename in fn:
        filename = filename.split('\n')[0]
        print filename
        image = imageio.imread(filename)
        writer.append_data(image)

if __name__ == "__main__":
  makeGif("eta_scan_phi_5")
