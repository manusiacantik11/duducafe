import streamlit as st
import pandas as pd

def dashboard():
    st.header('Tentang Kami')

    # Display welcome message
    st.subheader('Selamat datang di Angkringan Dudu Cafe!')
    st.write("""
        Angkringan Dudu Cafe adalah sebuah UMKM yang berlokasi di depan kost Cemara,
        Jl. Marga Satwa No.24, Banaran, Kec. Gn. Pati, Kota Semarang, Jawa Tengah 50229, Indonesia.
        Cafe ini memiliki rating 4.9 dengan 37 ulasan. Angkringan Dudu Cafe menawarkan suasana santai dan
        nyaman untuk pengunjung, serta berbagai menu minuman dan makanan yang tersedia.
    """)

     # Example of displaying an image
    st.subheader('Monggo Pinarak!')
    st.subheader('Nikmati Kebersamaan di Angkringan Dudu Cafe')
    st.image("angkringan.jpg")
    st.image("angkringan 3.jpg")

   # Menu Makanan dan Minuman
    st.header('Menu Makanan dan Minuman')
    menu_items = [
        'Nasi ayam               Rp.  3000',
        'Nasi ati ampela         Rp.  3000',
        'Nasi usus               Rp.  3000',
        'Nasi teri               Rp.  3000',
        'Sate bakso              Rp.  3000',
        'Sate Usus               Rp.  3000',
        'Mie rebus               Rp.  6000',
        'Mie nyemek              Rp. 12000',
        'Mie gorgor              Rp. 12000',
        'Mie rebus + telur       Rp. 10000',
        'Gorengan                Rp.  1000',
        'Piscok                  Rp.  1000',
        'Keju Aroma              Rp.  1000',
        'Bakaran                 Rp.  3000',
        'Kopi Susu               Rp.  6000',
        'Es teh-anget            Rp.  3000',
        'Wedang seruk            Rp.  1000',
        'Wedang Jahe             Rp.  4000',
        'Susu Jahe               Rp.  5000',
        'Kopi susu jahe          Rp.  6000'
    ]
    
    for item in menu_items:
        st.write(item)

# Tautan Sosial Media
    st.header('Ikuti Kami di Sosial Media')
    st.write('[Instagram](https://www.instagram.com/angkringanduducafe)')
# Run the function to display the dashboard
dashboard()