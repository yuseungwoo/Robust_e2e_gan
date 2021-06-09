noise_wav_list=[]
clean_wav_list=[]
with open('clean_wav.scp', 'r', encoding='utf-8') as fid:
    for line in fid:
        line = line.strip().replace('\n','')
        uttid, wav_path = line.split()
        clean_wav_list.append((uttid, wav_path)) 
print('clean_wav_list', clean_wav_list) 
    
with open('noise.scp', 'r', encoding='utf-8') as fid:
    for line in fid:
        line = line.strip().replace('\n','')
        wav_path = line.split()
        noise_wav_list.append(wav_path) 
print('noise_wav_list', noise_wav_list) 

def load_audio(path):
    sound, _ = torchaudio.load_wav(path)
    sound = sound.numpy().astype('float16')
    return sound[0]
