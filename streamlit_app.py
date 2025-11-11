import streamlit as st
import clips
import logging

# Setup working environment
logging.basicConfig(level=15,format='%(message)s')

env = clips.Environment()
router = clips.LoggingRouter()
env.add_router(router)

# input
name = st.test_input("Enter your name")

# knowledge base
env.build('(deftemplate result (slot name))')
# add facts to working memory
env.assert_string(f'(result (name "{name}"))')
#interface
