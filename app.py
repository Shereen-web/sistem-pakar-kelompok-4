
import streamlit as st

st.set_page_config(
    page_title="Sistem Pakar Kelompok 4",
    page_icon="🩺",
    layout="centered"
)

# JUDUL APLIKASI
st.title("🩺 Sistem Pakar Identifikasi Penyakit")
st.subheader("Identifikasi Penyakit Umum Berdasarkan Gejala")

st.write(
    "Aplikasi ini membantu memberikan informasi awal "
    "berdasarkan gejala yang dipilih pengguna."
)

st.info(
    "Aplikasi bersifat edukatif dan tidak menggantikan "
    "diagnosis tenaga medis."
)

# DAFTAR GEJALA
gejala = [
    "Demam",
    "Batuk",
    "Pilek",
    "Sakit kepala",
    "Nyeri tenggorokan",
    "Mual",
    "Muntah",
    "Diare",
    "Nyeri perut",
    "Bersin"
]

# BASIS PENGETAHUAN
aturan = [
    {
        "nama": "Flu",
        "gejala": {"Demam", "Batuk", "Sakit kepala"},
        "saran": "Istirahat cukup dan pantau perkembangan gejala."
    },
    {
        "nama": "Demam",
        "gejala": {"Demam", "Sakit kepala"},
        "saran": "Pantau suhu tubuh dan cukupi kebutuhan cairan."
    },
    {
        "nama": "Batuk",
        "gejala": {"Batuk", "Nyeri tenggorokan"},
        "saran": "Istirahat dan pantau kondisi pernapasan."
    },
    {
        "nama": "Pilek",
        "gejala": {"Pilek", "Bersin", "Nyeri tenggorokan"},
        "saran": "Istirahat dan cukupi kebutuhan cairan."
    },
    {
        "nama": "Maag",
        "gejala": {"Mual", "Nyeri perut"},
        "saran": "Perhatikan pola makan dan konsultasikan jika keluhan berlanjut."
    },
    {
        "nama": "Diare",
        "gejala": {"Diare", "Mual"},
        "saran": "Jaga asupan cairan untuk mencegah dehidrasi."
    },
    {
        "nama": "Sakit Kepala",
        "gejala": {"Sakit kepala", "Mual"},
        "saran": "Istirahat dan perhatikan perkembangan keluhan."
    }
]

# ALGORITMA FORWARD CHAINING
def forward_chaining(fakta):
    hasil = []
    proses = []

    fakta = set(fakta)

    for rule in aturan:
        cocok = rule["gejala"].issubset(fakta)

        proses.append({
            "aturan": rule["nama"],
            "syarat": rule["gejala"],
            "cocok": cocok
        })

        if cocok:
            hasil.append(rule)

    return hasil, proses


# INPUT PENGGUNA
st.header("1. Pilih Gejala")

pilihan = []

for item in gejala:
    if st.checkbox(item, key=item):
        pilihan.append(item)

# TOMBOL IDENTIFIKASI
if st.button("Identifikasi Penyakit", type="primary"):

    if not pilihan:
        st.warning("Silakan pilih minimal satu gejala.")

    else:
        hasil, proses = forward_chaining(pilihan)

        st.divider()
        st.header("2. Gejala yang Dipilih")

        for item in pilihan:
            st.write(f"✓ {item}")

        st.divider()
        st.header("3. Hasil Identifikasi")

        if hasil:
            for nomor, rule in enumerate(hasil, start=1):
                st.success(
                    f"Kemungkinan pola gejala: {rule['nama']}"
                )
                st.write(f"Saran umum: {rule['saran']}")

        else:
            st.warning(
                "Belum ditemukan aturan yang sesuai. "
                "Silakan perhatikan perkembangan gejala."
            )

        st.divider()
        st.header("4. Proses Forward Chaining")

        st.write(
            "Sistem mencocokkan fakta berupa gejala yang dipilih "
            "dengan aturan pada basis pengetahuan."
        )

        for item in proses:
            status = "Cocok" if item["cocok"] else "Tidak cocok"

            with st.expander(f"Aturan {item['aturan']} - {status}"):
                st.write("Syarat aturan:")
                st.write(", ".join(sorted(item["syarat"])))
                st.write("Gejala yang dipilih:")
                st.write(", ".join(pilihan))

        st.caption(
            "Hasil aplikasi merupakan informasi edukatif berdasarkan "
            "aturan sederhana, bukan diagnosis medis. "
            "Konsultasikan keluhan kepada tenaga kesehatan."
        )
