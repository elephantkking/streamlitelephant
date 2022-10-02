
# 스트림릿 라이브러리를 사용하기 위한 임포트
import streamlit as st

# 웹 대시보드 개발 라이브러리 스트림릿은,
# main 할수가 있어야 한다.



# def main() :  
#     st.title('안녕하세요 웹 대시보드 프로젝트')
#     st.title('헬로')
#     __name__ = '_sub_'



# def sub() :
#     st.title('안녕하세요 gpgpgpgp')
#     st.title('p')
    


# if __name__=='__main__' :
#     main()

# if __name__=='_sub_' : 
#     sub()

view = [100, 150, 30]
st.write('# Youtube View')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview