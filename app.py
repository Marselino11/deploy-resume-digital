# Import Library
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "doc" / "CV Imam Wahyudi_English.pdf"
profile_pic = current_dir / "doc" / "Foto Formal_Imam Wahyudi.JPG"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Imam W"
PAGE_ICON = ":wave:"
NAME = "Imam Wahyudi"
DESCRIPTION = """ 
Hi there! Let me introduce myself. My name is Imam Wahyudi, and I am
currently an active student in my eighth semester of the Faculty of
Science and Technology, majoring in Electrical Engineering at Al-Azhar
Indonesia University (UAI).

"""
EMAIL = "wahyudijr1@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/imam-wahyudi-6191021b4",
    "Instagram": "https://www.instagram.com/invites/contact/?i=1hvivyoqf8078&utm_content=1fq1apg",
}
PROJECTS = {
    "💼 Konferensi Seminar Nasional Pemberdayaan Masyarakat (SENDAMAS 2) - Universitas Al-Azhar Indonesia": "https://jurnal.uai.ac.id/index.php/PSN/article/view/1621",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Bagian pengaturan foto profile ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=260)
    st.write("Student | Electrical Engineering | Al-Azhar University")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Curicullum Vitae",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Internship Experience")
st.write(
    """
- ✔️ MSIB Batch 3 di PT Prasimax Inovasi Teknologi untuk 'Pengembangan Laptop Merah Putih', sebagai Hardware Engineer.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: C/C++, Arduino, Matlab
- 📚 Design     : HMI LCD Nextion and PCB Design Electrical Circuits
"""
)


# --- WORK HISTORY ---
#st.write('\n')
#st.subheader("Work Experience")
#st.write("---")

# --- JOB 1
#st.write("🚧", "**Senior Coach Artificial Intelligence | PT Orbit Future Academy**")
#st.write("2021 - Sekarang")

# --- JOB 2
#st.write('\n')
#st.write("🚧", "**Full-Stack Web Developer | PT Prima Armada Raya (PAR)**")
#st.write("2020 - 2021")
#st.write(
#    """
#- ► Menjaga dan memantau aplikasi yang ada.
#- ► Dukungan mengembangkan fitur baru untuk aplikasi yang ada.
#- ► Berkomunikasi dengan user mengenai masalah teknis.
#"""
#)

# --- JOB 3
#st.write('\n')
#st.write("🚧", "**IT Support Application | PT Datasynthesis**")
#st.write("2019 - 2020")
#st.write(
#    """
#- ► Menjaga dan memantau aplikasi yang ada.
#- ► Dukungan mengembangkan fitur baru untuk aplikasi yang ada.
#- ► Berkomunikasi dengan divisi lain mengenai masalah teknis.
#"""
#)

# --- JOB 4
#st.write('\n')
#st.write("🚧", "**Assistant Trainer | Yayasan Komunitas Open Source**")
#st.write("2019 - 2019")
#st.write(
#    """
#- ► Pelatihan dan Pengembangan SDM.
#"""
#)

# --- JOB 5
#st.write('\n')
#st.write("🚧", "**Staff Network Operations Center (NOC) | PT. Skyreach**")
#st.write("2018 - 2019")
#st.write(
#    """
#- ► Mengontrol dan Monitoring semua site.
#- ► Melakukan Troubelshoot dan Membuat report.
#"""
#)

# --- JOB 6
#st.write('\n')
#st.write("🚧", "**Supervisor Produksi Premik & Supply Chain | PT. Dapur Solo Sukses Sejati**")
#st.write("2009 - 2018")
#st.write(
#    """
#- ► Bertanggung jawab terhadap hal-hal yang berhubungan dengan jalanya oprasional.
#- ► Membuat laporan setiap bulan.
#- ► Mengontrol proses penimbangan bumbu premik.
#- ► Menjaga kualitas dan kuantitas bumbu premik.
#- ► Memastikan semua oprasional berjalan dengan baik dan sesuai SOP.
#"""
#)


# --- Projects & Pencapaian ---
st.write('\n')
st.subheader("Projects & Pencapaian")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
