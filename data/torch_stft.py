import numpy as np
import torch 
import librosa

# creating sine wave
fs = 64
t=1
s = np.linspace(0,t, int(fs*t))
x = np.sin(2*np.pi*3*s, dtype=np.float32)

n_fft = 64

# Slicing audio into windows of 64 samples wide

S_lib = librosa.stft(x, n_fft=n_fft, center=False, window='ones')
S_torchSTFT = torch.stft(torch.tensor(x), n_fft, center=False, return_complex=True).to("cuda:0")
S_torchSTFT = torch.stft(torch.tensor(x), n_fft, center=False, return_complex=True).to("cuda:1")
S_torchSTFT = torch.stft(torch.tensor(x), n_fft, center=False, return_complex=True).to("cuda:2")
print(S_lib)
print(S_torchSTFT)