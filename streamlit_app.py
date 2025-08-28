
# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session

cnx=st.connection("snowflake")
session=cnx.session()
