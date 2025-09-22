import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Streamlit 레이아웃 예제",
    page_icon=":heart_eyes:",
    layout="wide"  # 전체 페이지를 wide 모드로 설정
)

# 사이드바 메뉴 생성
with st.sidebar:
    st.title("게임")
    selected_menu = st.radio(
        "원하시는 게임을 선택하세요:",
        ["숫자맞추기", "가위바위보"]
    )

# 메인 컨텐츠 영역
import random
def show_game1():
    st.header("숫자맞추기")
    st.write("환영합니다! 이곳은 숫자맞추기 게임 페이지입니다.")

    if 'c_number' not in st.session_state:
        st.session_state.c_number = random.randint(1, 100)    
    c_num = st.session_state.c_number

    st.number_input("1에서 100 사이의 숫자를 입력하세요:", 0, 100, key='h_number')
    h_number = st.session_state.h_number
    # st.write(f"입력한 숫자: {h_number}")  
    if st.button('확인'): 
        if h_number != 0:        
            if h_number < c_num:
                st.warning("예측한 값이 낮습니다.")
            elif h_number > c_num:
                st.warning("예측한 값이 높습니다.")
            else:
                st.balloons()
                st.success(f"정답! {c_num}였습니다.")
                del st.session_state.c_number    



from PIL import Image
image = Image.open(r"C:\Users\choi\OneDrive - 한국외국어대학교\바탕 화면\가위바위보\가위.jpeg")
st.image(image)
def show_game2():
    st.header("가위바위보")
    st.write("환영합니다! 이곳은 가위바위보 게임 페이지입니다.")        
    
# 선택된 메뉴에 따라 해당하는 컨텐츠 표시
if selected_menu == "숫자맞추기":
    show_game1()
elif selected_menu == "가위바위보":
    show_game2()