import streamlit as st
from pages import student_info, student_enrollment
from Pagess import Data as data_page

# Page configuration (centralized)
st.set_page_config(page_title='School Dashboard', page_icon='🏫', layout='wide')

if 'page' not in st.session_state:
	st.session_state['page'] = 'Home'

st.sidebar.title('Navigation')
choice = st.sidebar.radio('Go to', ['Home', 'Student Info', 'Student Enrollment', 'Data'])
st.session_state['page'] = choice

if st.session_state['page'] == 'Home':
	st.title('School Dashboard')
	st.write('Welcome to the School Dashboard')

	# Quick links from Home
	col1, col2, col3 = st.columns(3)
	if col1.button('Open Student Info'):
		st.session_state['page'] = 'Student Info'
	if col2.button('Open Student Enrollment'):
		st.session_state['page'] = 'Student Enrollment'
	if col3.button('Open Data Upload'):
		st.session_state['page'] = 'Data'

elif st.session_state['page'] == 'Student Info':
	student_info.app()

elif st.session_state['page'] == 'Student Enrollment':
	student_enrollment.app()

elif st.session_state['page'] == 'Data':
	data_page.app()
 
 