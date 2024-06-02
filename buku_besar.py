import streamlit as st
import pandas as pd

def buku_besar():
    st.header('Buku Besar')
    st.write("Isi Buku Besar di sini.")

    # Initialize the dataframe in session state if not already initialized
    if 'buku_besar_df' not in st.session_state:
        st.session_state.buku_besar_df = pd.DataFrame(columns=['Tanggal', 'Keterangan', 'Debit', 'Kredit'])

    # Display the current transactions in the Buku Besar
    st.subheader('Transaksi Buku Besar')
    st.dataframe(st.session_state.buku_besar_df)

    # Add a form to input new transactions
    st.subheader('Tambah Transaksi Baru')
    with st.form(key='buku_besar_form'):
        tanggal = st.date_input('Tanggal')
        keterangan = st.text_input('Keterangan')
        debit = st.number_input('Debit', min_value=0)
        kredit = st.number_input('Kredit', min_value=0)
        submit_button = st.form_submit_button(label='Tambah Transaksi')

        if submit_button:
            new_transaction = pd.DataFrame([{'Tanggal': tanggal, 'Keterangan': keterangan, 'Debit': debit, 'Kredit': kredit}])
            st.session_state.buku_besar_df = pd.concat([st.session_state.buku_besar_df, new_transaction], ignore_index=True)
            st.write('Transaksi berhasil ditambahkan')

    # Display the updated transactions
    st.subheader('Transaksi Buku Besar Terbaru')
    st.dataframe(st.session_state.buku_besar_df)
