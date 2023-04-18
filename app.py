import streamlit as st 


st.title('title of your application') 
st.markdown('for example here is a **bold text**') 
st.sidebar.title ('this is the title of the sidebar')
    # gives you a sidebar: st.sidebar 

# insert a check box with text 
agree = st.checkbox('I agree') 
if agree: 
        st.write("Great!") 
        st.write('this is *italic text*') 

# insert a check box in sidebar with text 
side_check = st.sidebar.checkbox("Click me") 
if side_check: 
    st.sidebar.write('Sidebar checkbox has been clicked') 

# use this to run in terminal: 
# python -m streamlit run app.py 



# USE THIS TO ADD TO GITHUB, RUN IN TERMINAL 
# git init 
# git add . (adds all files)
# git commit -m "initial commit" 
# git branch -M main 
# git remote add origin https://github.com/noorbenny/streamlit_app.git 
# git push -u origin main 
