# pip install streamlit - 터미널에서 실행
import streamlit as st

st.title('타이틀')
st.header("헤더")
st.subheader('서브헤더')
st.write('the first app')

name = st.text_input('이름을 입력하세요: ')
st.write(f'안녕하세요 {name}님.')

st.button('버튼')
st.checkbox('체크박스')
st.radio('라디오박스', ('a','b','c'))
st.selectbox('셀렉트 박스', (1,2,3))
st.slider('슬라이더',0,100,50)
st.text_input('텍스트 상자')