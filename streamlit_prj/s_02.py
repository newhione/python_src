import streamlit as st
import random

# 컴퓨터 숫자 선택
if 'c_num' not in st.session_state:
    st.session_state['c_num'] = random.randint(1,100)
# 숫자 입력 1~100 사이
h_num = st.number_input('숫자 입력',1,100)

if st.button('결과 확인'):
    if h_num > st.session_state['c_num']:
        st.write('down')
    elif h_num < st.session_state['c_num']:
        st.write('up')
    else:
        st.write('컴퓨터 숫자:', st.session_state['c_num'])
        st.write('정답')
        st.balloons
