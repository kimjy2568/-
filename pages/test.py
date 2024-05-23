import streamlit as st
import pandas as pd
import datetime

# 시간표 데이터 생성 (7교시까지 포함)
timetables = {
    '1학년': {
        '1반': {
            '교시': ['1', '2', '3', '4', '5', '6', '7'],
            '월요일': ['국어', '기가', '정보', '음악', '과학', '수학', '영어'],
            '화요일': ['카혼', '과학', '실험', '진로', '수학', '체육', '사회'],
            '수요일': ['국어', '영어', '사회', '기가', '창동', '창동', ''],
            '목요일': ['영어', '수학', '과학', '애니', '국어', '사회', '음악'],
            '금요일': ['국어', '영어', '체육', '수학', '사회', '정보', '과학']
        },
        # 추가 반 데이터
    },
    '2학년': {
        '1반': {
            '교시': ['1', '2', '3', '4', '5', '6', '7'],
            '월요일': ['Chemistry', 'Math', 'Physics', 'Lunch', 'History', 'PE', 'Art'],
            '화요일': ['Biology', 'English', 'Math', 'Lunch', 'Physics', 'History', 'Music'],
            '수요일': ['English', 'Chemistry', 'Math', 'Lunch', 'Biology', 'PE', 'Art'],
            '목요일': ['Physics', 'History', 'Chemistry', 'Lunch', 'Math', 'English', 'Music'],
            '금요일': ['Math', 'Biology', 'English', 'Lunch', 'History', 'Physics', 'Art']
        },
        # 추가 반 데이터
    },
    '3학년': {
        '1반': {
            '교시': ['1', '2', '3', '4', '5', '6', '7'],
            '월요일': ['History', 'Math', 'Physics', 'Lunch', 'Chemistry', 'Biology', 'Art'],
            '화요일': ['Math', 'English', 'PE', 'Lunch', 'Physics', 'History', 'Music'],
            '수요일': ['Biology', 'History', 'Math', 'Lunch', 'Chemistry', 'English', 'Art'],
            '목요일': ['Physics', 'PE', 'English', 'Lunch', 'Math', 'Chemistry', 'Music'],
            '금요일': ['English', 'Biology', 'History', 'Lunch', 'Math', 'Physics', 'Art']
        },
        # 추가 반 데이터
    }
}

# Streamlit 앱 제목 설정
st.title("낙동고등학교 시간표")

# 학년과 반 선택 상자를 한 줄에 배치
col1, col2 = st.columns(2)
with col1:
    grade = st.selectbox("학년 선택", list(timetables.keys()))
with col2:
    classroom = st.selectbox("반 선택", list(timetables[grade].keys()))

# 선택된 학년과 반의 시간표 데이터프레임 생성
timetable = timetables[grade][classroom]
df = pd.DataFrame(timetable)
df.set_index('교시', inplace=True)

# 오늘 요일 감지
today = datetime.datetime.today().strftime('%A')
# 요일을 한국어로 변환
days_english_to_korean = {
    'Monday': '월요일',
    'Tuesday': '화요일',
    'Wednesday': '수요일',
    'Thursday': '목요일',
    'Friday': '금요일',
    'Saturday': '토요일',
    'Sunday': '일요일'
}
today_korean = days_english_to_korean[today]

# 요일에 맞는 열 색상 적용 함수
def highlight_today(col):
    if col.name == today_korean:
        return ['background-color: #ffeb3b; color: black'] * len(col)
    else:
        return [''] * len(col)

# HTML/CSS 스타일링 추가
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .dark-mode .reportview-container {
        background: #2e2e2e;
    }
    .dataframe table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        font-size: 20px; /* 폰트 크기 증가 */
    }
    .dataframe th, .dataframe td {
        border: 1px solid #dddddd;
        text-align: center;
        padding: 12px; /* 패딩 증가 */
    }
    .dataframe th {
        background-color: #4CAF50;
        color: white;
    }
    .dark-mode .dataframe th {
        background-color: #1a1a1a;
        color: #f0f0f0;
    }
    .dataframe td {
        background-color: #ffffff;
        color: black;
    }
    .dark-mode .dataframe td {
        background-color: #333333;
        color: #f0f0f0;
    }
    .dataframe tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    .dark-mode .dataframe tr:nth-child(even) {
        background-color: #2a2a2a;
    }
    </style>
    <script>
    const observer = new MutationObserver((mutations) => {
        const darkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (darkMode) {
            document.body.classList.add('dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
        }
    });
    observer.observe(document.body, { attributes: true, childList: true, subtree
    });
    </script>
    """,
    unsafe_allow_html=True
)

# 시간표 출력
st.write(f"{grade} {classroom}")
st.dataframe(df.style.apply(highlight_today, axis=0).set_properties(**{
    'border': '1px solid black',
    'font-size': '20px',  # 폰트 크기 증가
    'text-align': 'center'
}).set_table_styles([{
    'selector': 'th',
    'props': [('font-size', '22px')]  # 헤더 폰트 크기 증가
}]), width=1920)
