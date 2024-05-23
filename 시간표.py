import streamlit as st
import pandas as pd
import datetime

# 시간표 데이터 생성 (7교시까지 포함)
timetables = {
    '1학년': {
        '1반': {
            '교시': ['9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00', '12:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00'],
            'Monday': ['Math', 'English', 'Physics', 'Lunch', 'History', 'Biology', 'Art'],
            'Tuesday': ['Chemistry', 'Math', 'English', 'Lunch', 'Physics', 'PE', 'Music'],
            'Wednesday': ['History', 'Chemistry', 'Math', 'Lunch', 'English', 'Physics', 'Art'],
            'Thursday': ['PE', 'History', 'Chemistry', 'Lunch', 'Math', 'English', 'Music'],
            'Friday': ['Biology', 'PE', 'History', 'Lunch', 'Chemistry', 'Math', 'Art']
        },
        '2반': {
            'Time': ['9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00', '12:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00'],
            'Monday': ['English', 'Math', 'Physics', 'Lunch', 'PE', 'Biology', 'Music'],
            'Tuesday': ['Math', 'Chemistry', 'History', 'Lunch', 'Physics', 'English', 'Art'],
            'Wednesday': ['Biology', 'Math', 'English', 'Lunch', 'Chemistry', 'History', 'Music'],
            'Thursday': ['History', 'PE', 'Math', 'Lunch', 'English', 'Chemistry', 'Art'],
            'Friday': ['Physics', 'Biology', 'PE', 'Lunch', 'Math', 'History', 'Music']
        },
        # ... 더 많은 반 데이터 추가
    },
    '2학년': {
        '1반': {
            'Time': ['9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00', '12:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00'],
            'Monday': ['Chemistry', 'Math', 'Physics', 'Lunch', 'History', 'PE', 'Art'],
            'Tuesday': ['Biology', 'English', 'Math', 'Lunch', 'Physics', 'History', 'Music'],
            'Wednesday': ['English', 'Chemistry', 'Math', 'Lunch', 'Biology', 'PE', 'Art'],
            'Thursday': ['Physics', 'History', 'Chemistry', 'Lunch', 'Math', 'English', 'Music'],
            'Friday': ['Math', 'Biology', 'English', 'Lunch', 'History', 'Physics', 'Art']
        },
        '2반': {
            'Time': ['9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00', '12:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00'],
            'Monday': ['Math', 'History', 'Physics', 'Lunch', 'English', 'PE', 'Music'],
            'Tuesday': ['Chemistry', 'Math', 'Biology', 'Lunch', 'Physics', 'History', 'Art'],
            'Wednesday': ['English', 'Chemistry', 'History', 'Lunch', 'Biology', 'Math', 'Music'],
            'Thursday': ['PE', 'English', 'Chemistry', 'Lunch', 'Math', 'Physics', 'Art'],
            'Friday': ['Biology', 'PE', 'Math', 'Lunch', 'History', 'English', 'Music']
        },
        # ... 더 많은 반 데이터 추가
    },
    '3학년': {
        '1반': {
            'Time': ['9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00', '12:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00'],
            'Monday': ['History', 'Math', 'Physics', 'Lunch', 'Chemistry', 'Biology', 'Art'],
            'Tuesday': ['Math', 'English', 'PE', 'Lunch', 'Physics', 'History', 'Music'],
            'Wednesday': ['Biology', 'History', 'Math', 'Lunch', 'Chemistry', 'English', 'Art'],
            'Thursday': ['Physics', 'PE', 'English', 'Lunch', 'Math', 'Chemistry', 'Music'],
            'Friday': ['English', 'Biology', 'History', 'Lunch', 'Math', 'Physics', 'Art']
        },
        '2반': {
            'Time': ['9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00', '12:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00'],
            'Monday': ['PE', 'Math', 'Physics', 'Lunch', 'Chemistry', 'History', 'Music'],
            'Tuesday': ['Math', 'Biology', 'History', 'Lunch', 'Physics', 'English', 'Art'],
            'Wednesday': ['English', 'PE', 'Math', 'Lunch', 'Chemistry', 'Biology', 'Music'],
            'Thursday': ['Physics', 'History', 'Math', 'Lunch', 'English', 'Chemistry', 'Art'],
            'Friday': ['Biology', 'English', 'PE', 'Lunch', 'History', 'Math', 'Music']
        },
        # ... 더 많은 반 데이터 추가
    }
}

# Streamlit 앱 제목 설정
st.title("School Timetable")

# 학년과 반 선택 상자를 한 줄에 배치
col1, col2 = st.columns(2)
with col1:
    grade = st.selectbox("Select Grade", list(timetables.keys()))
with col2:
    classroom = st.selectbox("Select Class", list(timetables[grade].keys()))

# 선택된 학년과 반의 시간표 데이터프레임 생성
timetable = timetables[grade][classroom]
df = pd.DataFrame(timetable)
df.set_index('교시', inplace=True)

# 오늘 요일 감지
today = datetime.datetime.today().strftime('%A')

# 요일에 맞는 열 색상 적용 함수
def highlight_today(col):
    if col.name == today:
        return ['background-color: #ffeb3b'] * len(col)
    else:
        return [''] * len(col)

# HTML/CSS 스타일링 추가
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .dataframe table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
    }
    .dataframe th, .dataframe td {
        border: 1px solid #dddddd;
        text-align: center;
        padding: 8px;
        font-size: 18px;  /* 폰트 크기 조정 */
    }
    .dataframe th {
        background-color: #4CAF50;
        color: white;
    }
    .dataframe td {
        background-color: #ffffff;
    }
    .dataframe tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 시간표 출력
st.write(f"Timetable for {grade} {classroom}")
st.dataframe(df.style.apply(highlight_today, axis=0).set_properties(**{
    'border': '1px solid black',
    'color': 'black',
    'font-size': '18px'  # 폰트 크기 조정
}).set_table_styles([{
    'selector': 'th',
    'props': [('font-size', '20px')]  # 헤더 폰트 크기 조정
}]))