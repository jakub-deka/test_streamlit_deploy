import streamlit as st

ss = st.session_state

if "first_run" not in ss:
    ss.first_run = False

    st.write("This is the first run")
else:
    st.write("This is not the first run")

if st.button("Go to chat"):
    ss.go_to_chat = True
    st.switch_page("./pages/chat.py")

if st.button("Rerun app"):
    ss.rerun_me = True
    st.rerun()

if st.button("Reset"):
    for key in ss.keys():
        del ss[key]

    st.rerun()


st.write(ss)
