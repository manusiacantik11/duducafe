import streamlit as st
import pandas as pd

# Fungsi untuk admin dashboard
def admin_dashboard():
    st.sidebar.header('Dashboard')
    page = st.sidebar.selectbox(
        'Pilih Halaman',
        ['Input Transaksi', 'Jurnal Penjualan', 'Jurnal Pembelian', 'Jurnal Umum', 'Buku Besar', 'Laporan Keuangan']
    )
    
    if page == 'Input Transaksi':
        input_transaksi()
    elif page == 'Jurnal Penjualan':
        jurnal_penjualan()
    elif page == 'Jurnal Pembelian':
        jurnal_pembelian()
    elif page == 'Jurnal Umum':
        jurnal_umum()
    elif page == 'Buku Besar':
        buku_besar()
    elif page == 'Laporan Keuangan':
        laporan_keuangan()

def input_transaksi():
    st.header('Input Transaksi Harian')

    jenis_transaksi = st.radio("Jenis Transaksi", ('Penjualan', 'Pembelian'))

    if jenis_transaksi == 'Penjualan':
        akun_items = ['Kas', 'Piutang Dagang', 'Penjualan', 'Prive', 'Beban Lain-lain']
    else:  # Pembelian
        akun_items = ['Kas', 'Utang Dagang', 'Pembelian', 'Perlengkapan', 'Peralatan', 'Beban Lain-lain']

    if 'transaksi' not in st.session_state:
        st.session_state['transaksi'] = []

    with st.form(key='transaction_form'):
        if 'new_transaction' not in st.session_state:
            st.session_state['new_transaction'] = {}
        st.session_state['new_transaction']['tanggal'] = st.date_input('Tanggal', key='tanggal')
        nama_pelanggan_supplier = st.text_input('Nama Customer/Supplier', key='nama_pelanggan_supplier')
        keterangan = st.text_input('Keterangan', key='keterangan')
        
        # Pilih jenis akun
        st.session_state['new_transaction']['akun'] = st.selectbox('Akun', akun_items, key='akun')

        # Kolom pertama untuk transaksi pertama
        st.session_state['new_transaction']['debit'] = st.number_input('Debit', min_value=0, step=1, key='debit')

        # Kolom kedua untuk double entry
        st.session_state['new_transaction']['kredit'] = st.number_input('Kredit', min_value=0, step=1, key='kredit')

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.success('Transaksi berhasil ditambahkan:')
            # Menambahkan transaksi pertama
            st.session_state['transaksi'].append({
                'Tanggal': st.session_state['new_transaction']['tanggal'],
                'Nama Pelanggan/Supplier': nama_pelanggan_supplier,
                'Akun': st.session_state['new_transaction']['akun'],
                'Debit': st.session_state['new_transaction']['debit'],
                'Kredit': "-" if jenis_transaksi == 'Penjualan' else st.session_state['new_transaction']['kredit']
            })
            # Menambahkan transaksi double entry
            st.session_state['transaksi'].append({
                'Tanggal': st.session_state['new_transaction']['tanggal'],
                'Nama Pelanggan/Supplier': nama_pelanggan_supplier,
                'Akun': 'Penjualan' if jenis_transaksi == 'Penjualan' else 'Pembelian',
                'Debit': "-" if jenis_transaksi == 'Penjualan' else st.session_state['new_transaction']['kredit'],
                'Kredit': st.session_state['new_transaction']['kredit'] if jenis_transaksi == 'Penjualan' else "-"
            })

    st.subheader('Daftar Transaksi')
    if 'transaksi' in st.session_state:
        df_transaksi = pd.DataFrame(st.session_state['transaksi'])
        df_transaksi.insert(0, 'No', range(1, len(df_transaksi) + 1))

        # Tampilkan tabel
        st.write(df_transaksi)

        # Tambahkan tombol hapus di setiap baris
        for i, transaksi in df_transaksi.iterrows():
            if st.button(f"Hapus Transaksi {i+1}", key=f"hapus_{i}"):
                st.session_state['transaksi'].pop(i)
                st.experimental_rerun()


def jurnal_penjualan():
    st.header('Jurnal Penjualan')
    st.write('Daftar Jurnal Penjualan')

def jurnal_pembelian():
    st.header('Jurnal Pembelian')
    st.write('Daftar Jurnal Pembelian')

def jurnal_umum():
    st.header('Jurnal Umum')
    st.write('Daftar Jurnal Umum')

def buku_besar():
    st.header('Buku Besar')
    st.write('Daftar Buku Besar')

def laporan_keuangan():
    st.header('Laporan Keuangan')
    st.write('Laporan Keuangan')

if __name__ == '__main__':
    admin_dashboard()
