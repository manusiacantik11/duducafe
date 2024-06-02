import streamlit as st
from admin_dashboard import admin_dashboard
from user_dashboard import user_dashboard

# Fungsi untuk memverifikasi login
def verify_login(username, password, user_data):
    user = user_data.get(username)
    if user and user['password'] == password:
        return user['role']
    return None

# Data pengguna dan admin
user_data = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'user': {'password': 'userpass', 'role': 'user'}
}

# Fungsi utama untuk login dan pengaturan dashboard
def main():
    st.title('Angkringan Dudu Cafe')
    
    if 'role' not in st.session_state:
        st.session_state['role'] = None
    
    if st.session_state['role'] is None:
        st.header('Login')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            role = verify_login(username, password, user_data)
            if role:
                st.session_state['role'] = role
                st.session_state['username'] = username
                st.success(f'Login berhasil! Anda login sebagai {role}.')
            else:
                st.error('Username atau password salah.')
    else:
        if st.session_state['role'] == 'admin':
            admin_dashboard()
        elif st.session_state['role'] == 'user':
            user_dashboard()
        
        if st.button('Logout'):
            st.session_state['role'] = None
            st.session_state['username'] = None
            st.success('Logout berhasil.')

if __name__ == '__main__':
    main()
