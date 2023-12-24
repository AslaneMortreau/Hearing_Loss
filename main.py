import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import librosa
import soundfile as sf
import wave



st.set_option('deprecation.showPyplotGlobalUse', False)

with st.sidebar : 
    p=st.slider("Hearing loss percentage",min_value=0,max_value=100,step=1)
    p*=0.01
    filename = "file.wav"
    f=open(filename,'rb')
    y,sr = librosa.load(filename)
    valider = st.button("Valider")


if valider:
    fft_signal = np.fft.fft(y)
    amp = np.abs(fft_signal)
    frequencies = np.fft.fftfreq(len(y), 1/sr)
    a=np.random.choice(len(fft_signal), size=int(len(fft_signal)*p), replace=False)
    fft_signal[a]=0
    amp2 = np.abs(fft_signal)
    y_filtered = np.fft.ifft(fft_signal).real
    plt.plot(fft_signal)
    plt.show()
    y_norm = librosa.util.normalize(y_filtered)
    sf.write('output_file.wav',y_norm, sr,'PCM_24')
    audio_file = open('output_file.wav','rb')
    st.write("Original file")
    st.audio(f)
    st.write("Transformed file")
    st.audio(audio_file)
    col1,col2=st.columns(2)
    with col1:
        st.header('Original audio')
        fig, ax = plt.subplots()
        ax.plot(frequencies,amp)
        st.pyplot(fig)
    with col2:
        st.header('Transformed audio')
        fig2, ax2 = plt.subplots()
        ax2.plot(frequencies,amp2)
        st.pyplot(fig2)