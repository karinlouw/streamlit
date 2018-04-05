from keras.datasets import mnist
from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import np_utils
import keras
import math
import numpy as np
import pandas as pd
import sys

from streamlit import Report, Chart

training_data = Report.get('5a7a62c393ff002ab2dad2ff')
x_train = training_data.get('x_train')
x_test = training_data.get('x_test')

report = Report.fork('5a7a62c393ff002ab2dad2ff')
network = report.get('network')


with Report() as write:
    write('hello world')
