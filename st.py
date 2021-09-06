import streamlit as st 
from pydub import AudioSegment
from main import play_sound as pls


st.title('モールス信号')
char = st.text_input('入力してください')
st.write('※半角小文字のみ、スペースもだめ')
was_clicked = st.button('再生する') 
if was_clicked is not None:
    pls = pls()
    ret = pls.input_char(char)
    audio = AudioSegment.from_wav('./sound-wave/.wav')
    for i in ret:
        name = "./sound-wave/" + i + ".wav"
        sound = AudioSegment.from_wav(name)
        audio = audio + sound
    audio.export('test.wav', format='wav')
    audio_bytes = open('test.wav', 'rb').read()
    st.audio(audio_bytes, format='audio/wav')