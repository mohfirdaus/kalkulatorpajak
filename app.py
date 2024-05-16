import streamlit as st

def hitung_gross_up(penghasilan_netto):
    TARIF_PAJAK = 0.05
    penghasilan_bruto_gross_up = penghasilan_netto / (1 - (0.5 * TARIF_PAJAK))
    dpp = penghasilan_bruto_gross_up * 0.5
    pajak = dpp * TARIF_PAJAK
    return round(penghasilan_bruto_gross_up), round(dpp), round(pajak)

def main():
    st.title('Kalkulator Pajak')
    penghasilan_netto = st.number_input('Masukkan Penghasilan Netto:', min_value=0.0, step=5000.0)
    if st.button('Hitung'):
        penghasilan_bruto_gross_up, dpp, pajak = hitung_gross_up(penghasilan_netto)
        st.write(f'Penghasilan Bruto Gross-Up: Rp{penghasilan_bruto_gross_up:,}')
        st.write(f'Dasar Pengenaan Pajak (DPP): Rp{dpp:,}')
        st.write(f'PPh 21: Rp{pajak:,}')
        st.write(f'Jumlah Transfer: Rp{penghasilan_netto:,}')

if __name__ == '__main__':
    main()
