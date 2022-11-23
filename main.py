import streamlit as st
import pandas as pd
import sqlite3 as sl
# Security
# passlib,hashlib,bcrypt,scrypt
con = sl.connect('gymdata.db')
c = con.cursor()

# username TEXT,
# password TEXT,
# age INTEGER,
# workout TEXT

# DB  Functions


def create_users():
    c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT,age INTEGER,workout TEXT)')


def add_userdata(username, password, age):
    c.execute('INSERT INTO users(username,password,age) VALUES (?,?,?)',
              (username, password, age))
    con.commit()


def login_user(username, password):
    c.execute('SELECT * FROM users WHERE username =? AND password = ?',
              (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    return data

# SIDE BAR
# Using object notation
# add_selectbox = st.sidebar.selectbox("How",
# ("Email", "Home phone", "Mobile phone"))


menu = ["Home", "Login", "SignUp"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Home")

elif choice == "Login":
    st.subheader("Login With Your User Name")

username = st.sidebar.text_input("User Name")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    # if password == '12345':
    create_users()
    result = login_user(username, password)
if st.sidebar.button("Signup"):
    create_users()
    add_userdata(username, password)
    st.success("You have successfully created a valid Account")
    st.info("Go to Login Menu to login")
elif choice == "SignUp":
    st.subheader("Register Your User Name & Password")
    # username = st.sidebar.text_input("User Name")
    # password = st.sidebar.text_input("Password", type="password")

# FRONT PAGE
st.title('Gym Python :snake:')
st.header('Select your Exercise:')
# _italics_
# :blue[colors]

st.write('Only Two Exercise:')
option_s = st.checkbox('Arms')
option_u = st.checkbox('Chest')
option_v = st.checkbox('Shoulders')
option_a = st.checkbox('Back')
option_t = st.checkbox('Legs')
known_variables = option_s + option_u + option_v + option_a + option_t

if known_variables < 3:
    st.write('**You have to select minimum 3 variables.**')
elif known_variables == 3:
    st.write('')
elif known_variables > 3:
    st.write('You can select maximum 3 variables.')

st.markdown(
    f'<h1 style="color:#00d26a;font-size:28px;">{"Workout of the Day"}</h1>', unsafe_allow_html=True)

df = pd.DataFrame({
    'Series': [1, 2, 3, 4],
    'Repetitions': [10, 20, 30, 40],
    'Weight': [10, 20, 30, 40]
})
df
