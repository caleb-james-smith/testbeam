import matplotlib.pyplot as plt
import numpy as np
import imageio
import glob

def makeGif(name):
  gifname = name + '.gif'
  files = glob.glob(name + '/*.gif')
  #use duration or fps for timing
  #with imageio.get_writer(gifname, mode='I',duration=0.01) as writer:
  with imageio.get_writer(gifname, mode='I', duration=1) as writer:
    for filename in files:
      print filename
      image = imageio.imread(filename)
      writer.append_data(image)
  print "Created gif: {0}".format(gifname)

if __name__ == "__main__":
  makeGif("eta_scan_phi_5")
