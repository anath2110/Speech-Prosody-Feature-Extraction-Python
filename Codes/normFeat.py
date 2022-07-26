# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:57:36 2019

@author:Anindita Nath 
        3M|M*Modal
        Pittsburgh,PA 
Translated to Python and modified from the original in MATLAB,
zNormalizeBothSpeakers.m by Gerardo Cervantes.
Reference:
Ward et al., "TURN-TAKING PREDICTIONS ACROSS LANGUAGES AND GENRES USING AN LSTM
RECURRENT NEURAL NETWORK", IEEE Workshop on Spoken Language Technology (SLT),2018
"""
"""
This script handles Z-normalizing 3D multidimensional arrays, where the
features are in the first dimension, axis 0.
"""

def normFeat(features, featsMean, featsStd, feature_index):    
    
    featuresAtIndex = features[feature_index,:, :]
    featuresAtIndex = featuresAtIndex - featsMean[feature_index]
    featuresAtIndex = featuresAtIndex/featsStd[feature_index]
    features[feature_index,:,:] = featuresAtIndex    
    normalizedFeats = features
    
    return normalizedFeats

    