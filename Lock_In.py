# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:03:17 2023

@author: bipo12


This function allows you to receive the output signal from Lock_In amplifier for a given signal and parameters.
u_det - input signal
sample_rate - sample rate of digitizer 
f_ref - reference frequency
fc_lowpass - low pass filter cut-off frequency
num_har - number of harmonic that should be detected by Lock_In amplifier 

Example usage:
import Lock_In
import matplotlib.pyplot as plt
import numpy as np

sample_rate=1*10**6
num_samples=100*10**3
f_ref=200*10**3
f_mod=200*10**3
t=np.arange(0,(num_samples)/sample_rate,1/sample_rate)
u_det=1*np.sin(2*np.pi*f_mod*t)
plt.figure(1)
plt.clf()
plt.plot(u_det)
plt.title('Input signal')
plt.ylabel('Voltage')
plt.xlabel('Number of sample')
fc_lowpass=100
num_har=1

R=Lock_In.lock_in(u_det,sample_rate,num_samples,f_ref,fc_lowpass,num_har)
plt.figure(2)
plt.plot(R)
plt.title('Output signal')
plt.ylabel('Voltage')
plt.xlabel('Number of sample')
plt.ylim([0,1])

"""

import numpy as np

def lock_in(u_det,sample_rate,num_samples,f_ref,fc_lowpass,num_har):
    
    t=np.arange(0,(num_samples)/sample_rate,1/sample_rate)
    A_ref=1
    phase_ref=0
    if len(u_det)!=len(t):
        t=t[:t.shape[0]-(t.shape[0]%10)]
    
    X=np.multiply(u_det,A_ref*np.sin(2*np.pi*num_har*f_ref*t+phase_ref))
    Y=np.multiply(u_det,A_ref*np.cos(2*np.pi*num_har*f_ref*t+phase_ref))
    
    atten=60#desired attenuation in dB
    N=atten/(22*fc_lowpass/sample_rate)#number of taps
    print(f'Number of taps: {N}')
    x=np.arange(1,N)
    wc=fc_lowpass/(sample_rate/2)
    filter_lwpass=np.sin(wc*np.pi*(x-(N+1)/2))/(np.pi*(x-(N+1)/2))#the normalised function sinc (repspone of the ideal low pass filter)
    filter_lwpass[int((N)/2)]=wc#delete NAN value from the middle sample
    wbl=0.42-0.5*np.cos(2*np.pi*x/N)+0.08*np.cos(4*np.pi*x/N);# the Blackman window
    filter_lwpass=filter_lwpass*wbl;
    
    X=np.convolve(X,filter_lwpass,mode='valid')
    Y=np.convolve(Y,filter_lwpass,mode='valid')
    
    R=np.sqrt(np.power(X,2)+np.power(Y,2))
    R=R.tolist()
    
    return R
