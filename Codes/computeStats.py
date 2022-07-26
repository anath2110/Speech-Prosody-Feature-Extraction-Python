# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:57:36 2019

@author:Anindita Nath 
        3M|M*Modal
        Pittsburgh,PA   
Translated to Python and modified from the original in MATLAB, 
getFeaturesMeanStd.m by Gerardo Cervantes.

Reference:
Ward et al., "TURN-TAKING PREDICTIONS ACROSS LANGUAGES AND GENRES USING AN LSTM
RECURRENT NEURAL NETWORK", IEEE Workshop on Spoken Language Technology (SLT),2018
"""

"""
From a 3 dimensional array, find the mean and standard deviation of the
features.  Features should be in the third dimension.
"""
import numpy as np


def computeStats(trainFeatures):
    #print(trainFeatures.shape)
    samplemeans=np.mean(trainFeatures,axis=1)
    #print(samplemeans.shape)
    #samplesMeans = np.squeeze(means).shape
    #print(samplesMeans.shape)
    featuresMean = np.mean(samplemeans,axis=1)
    #print(featuresMean.shape)
    samplesStds = np.std(trainFeatures,axis=1)
    #print(samplesStds.shape)
    featuresStd = np.std(samplesStds,axis=1)
    #print(featuresStd.shape)
    return featuresMean,featuresStd