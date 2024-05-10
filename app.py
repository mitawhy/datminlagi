# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

color_scheme = px.colors.qualitative.Pastel

st.set_page_config(
    page_title="Prediksi Tingkat Adaptivitas Siswa dalam Pendidikan secara Online",
    page_icon="📊",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

# Baca dataset
dataset1 = 'students_adaptability_level_online_education.csv'
df = pd.read_csv(dataset1)

dataset = 'Data Cleaned_new.csv'
df1 = pd.read_csv(dataset)

# Sidebar untuk navigasi
with st.sidebar:
    st.header("Prediksi Tingkat Adaptivitas Siswa dalam Pendidikan secara Online")
    page_names = ['Pengenalan', 'Visualisasi Data', "Prediksi"]
    page = st.radio('Main Menu', page_names)

# Halaman Home
if page == "Pengenalan":
    st.title("Prediksi Tingkat Adaptivitas Siswa dalam Pendidikan secara Online")
    st.image('gambar.png', use_column_width=True)
    # st.write("Halo! Selamat Datang! :wave:")
    st.write("""
             Dashboard ini berisi tentang data-data siswa yang ada pada dataset terkait faktor-faktor yang sekiranya memengaruhi adaptivitas siswa pada pendidikan secara online. 
             Data tersebut kemudian diolah atau diproses untuk membuat prediksi tingkat adaptivitas siswa yang nantinya dapat digunakan oleh pihak-pihak tertentu untuk menyesuaikan pembelajaran yang sesuai untuk siswa agar pendidikan dapat terus maju.
             """)
    st.write("""Meskipun pendidikan online menawarkan fleksibilitas, para siswa harus menghadapi berbagai tantangan seperti kurangnya interaksi sosial dan kesulitan dalam mempertahankan fokus. 
             Di sinilah adaptivitas menjadi kunci utama kesuksesan. Dengan memprediksi tingkat adaptivitas siswa, kita dapat menyesuaikan pengalaman pembelajaran secara individual, 
             memastikan setiap siswa mendapatkan pendidikan yang sesuai dengan kebutuhannya. Oleh karena itu, pembuatan dashboard adaptivitas menjadi langkah yang penting dalam mendukung 
             kemajuan pendidikan di era digital ini.
             """)

    st.subheader("""
    Berikut adalah data terkait siswa yang ada:""")
    st.write(df)

    st.markdown("""
                Tabel di atas memiliki 14 kolom dan 1205 baris. Berikut adalah penjelasan untuk setiap kolom:
                1. **Gender**: Berisi jenis kelamin dari para siswa. Kolom ini memiliki nilai Boy dan Girl.
                2. **Age**: Berisi rentang usia para siswa.
                3. **Education Level**: Kolom ini berisikan tingkat institusi pendidikan siswa, seperti School, College, dan University.
                4. **Institution Type**: Berisi jenis institusi pendidikan siswa, yaitu Government (Pemerintah) atau Non Government (Bukan pemerintah).
                5. **IT Student**: Berisi pernyataan apakah siswa belajar sebagai siswa IT atau tidak (Yes or No).
                6. **Location**: Berisi pernyataan apakah lokasi siswa di kota (Yes or No).
                7. **Load-shedding**: Berisi level dari Load-shedding. Load shedding adalah keadaan dimana ketika permintaan listrik melebihi pasokan, kadang-kadang orang perlu terputus dari listrik untuk mencegah seluruh sistem runtuh. Nilai dari kolom ini ada Low dan High.
                8. **Financial Condition**: Berisi kondisi keuangan keluarga siswa. Kolom ini memiliki nilai Poor, Mid, dan Rich.
                9. **Internet Type**: Berisi jenis internet yang paling banyak digunakan dalam perangkat.
                10. **Network Type**: Berisi Jenis konektivitas jaringan, seperti 2G, 3G, dan 4G.
                11. **Class Duration**: Berisi rentang durasi kelas harian.
                12. **Self Lms**: Berisi ketersediaan LMS (Learning Management System) milik institusi.
                13. **Device**: Berisi jenis perangkat yang digunakan oleh sebagian besar siswa di kelas.
                14. **Adaptivity Level**: Berisi tingkat kemampuan beradaptasi siswa. Kolom ini merupakan kolom target.

                """)

# Halaman Visualisasi Data
elif page == "Visualisasi Data":
    selected_category = st.sidebar.selectbox("Halaman",
                                             ["Distribusi Data", "Analisis Perbandingan", "Analisis Hubungan", "Analisis Komposisi"])

    if selected_category == "Distribusi Data":
        st.subheader("Distribusi Usia Siswa Berdasarkan Gender")
        boy = df1[df1['Gender'] == 0]
        girl = df1[df1['Gender'] == 1]

        male_age_counts = boy['Age'].value_counts()
        female_age_counts = girl['Age'].value_counts()

        plt.figure(figsize=(10, 6))
        plt.hist(boy['Age'], bins=20, color='blue', alpha=0.5, label='Boy')
        plt.hist(girl['Age'], bins=20, color='pink', alpha=0.5, label='Girl')

        plt.title('Distribusi Usia Siswa Berdasarkan Gender')
        plt.xlabel('Kategori Usia')
        plt.ylabel('Jumlah Siswa')
        plt.legend()

        plt.grid(True)
        plt.show()
        st.pyplot()

        st.markdown("**1. Interpretasi**")
        st.markdown("""
                    - Grafik menunjukkan jumlah siswa dalam berbagai kategori usia, dengan fokus pada distribusi gender.
                    - Kategori 2 dan 4 memiliki jumlah anak laki-laki yang jauh lebih tinggi dibandingkan dengan anak perempuan, menunjukkan ketidakseimbangan gender dalam kelompok usia tersebut.
                    - Kategori 0, 1, dan 5 memiliki jumlah siswa yang relatif lebih rendah, dengan rasio gender yang bervariasi.
                    """)
        
        st.markdown("**2. Insight**")
        st.markdown("""
                    - Perlu untuk mengatasi ketidakseimbangan gender, terutama di kategori 2 dan 4, di mana jumlah anak laki-laki jauh lebih banyak daripada anak perempuan.
                    - Memahami alasan di balik disparitas gender dalam kelompok usia tertentu dapat membantu dalam menerapkan intervensi yang ditargetkan untuk mempromosikan kesetaraan gender.
                    """)
        
        st.markdown("**3. Actionable**")
        st.markdown("""
                   - Melakukan penelitian lebih lanjut untuk mengidentifikasi faktor-faktor yang menyebabkan ketidakseimbangan gender di kategori 2 dan 4.
                    - Mengimplementasikan inisiatif untuk mendorong dan mendukung partisipasi anak perempuan dalam pendidikan serta memastikan kesempatan yang sama bagi kedua gender.
                    - Mengembangkan program dan kebijakan yang mempromosikan inklusivitas dan keragaman dalam lingkungan pendidikan untuk menciptakan lingkungan belajar yang lebih seimbang dan adil.
                    """)
        #####

    elif selected_category == "Analisis Perbandingan":
        st.subheader("Perbandingan Jumlah Startup Berdasarkan Tahun Pendirian")
        durasi = ['Class Duration']
        plt.figure(figsize=(15,10))

        for i, col in enumerate(durasi):
            plt.subplot(3,3,i + 1)
            ax = sns.countplot(data = df, x = col, hue = "Adaptivity Level", palette = sns.color_palette("Set1"))
        st.pyplot()

        st.markdown("**1. Interpretasi**")
        st.markdown("""
                    - Jumlah startup yang paling banyak ada pada sekitar tahun 2011/2012 yaitu lebih dari 2000 startup.
                    - Jumlah startup terlihat mulai meningkat pada sekitar tahun 2000an.
                    - Jumlah startup terlihat mulai menurun sekitar tahun 2012/2013.
                    """)
        
        st.markdown("**2. Insight**")
        st.markdown("""
                    - Pasar startup di dunia mengalami pertumbuhan yang sangat pesat dalam beberapa tahun terakhir terutama pada tahun 2011/2012. 
                    Hal ini menunjukkan bahwa semakin banyak orang yang tertarik untuk memulai startup dan ekosistem startup di dunia semakin matang.
                    - Jumlah startup yang tiba-tiba melonjak tinggi dapat disebabkan oleh beberapa faktor, seperti berkambangnya teknologi digital,
                    meningkatnya minat investor terhadap startup, dan kebijakan pemerintah yang mendukung startup.
                    - Terjadinya tren penurunan jumlah startup juga dapat disebabkan oleh beberapa faktor.
                    """)
        
        st.markdown("**3. Actionable**")
        st.markdown("""
                    - Para pemangku kepentingan perlu melakukan analisis terhadap penyebab penurunan dan pertumbuhan startup. Identifikasi faktor-faktor yang menyebabkan hal tersebut. 
                    Dengan itu, dapat menghindarkan startup dari risiko-risiko yang ada dan membuat startup semakin sukses.
                    - Jika lonjakan jumlah startup pada tahun 2011/2012 disebabkan oleh berkembangnya ekosistem startup, maka perlu diperkuat lagi faktor-faktor yang mendukung pertumbuhan tersebut. 
                    Ini termasuk memperluas infrastruktur pendukung seperti ruang kerja bersama, akses pendanaan, mentorship, dan akses pasar.
                    - Dengan mengetahui bahwa jumlah startup bisa berfluktuasi secara signifikan, penting untuk membangun startup yang tahan terhadap perubahan pasar. 
                    Fokus pada pembangunan model bisnis yang berkelanjutan, diversifikasi portofolio produk atau layanan, dan membangun hubungan yang kuat dengan pelanggan dan mitra.
                    - Para pemangku kepentingan terkait dapat menggunakan wawasan dari analisis tren ini untuk membuat keputusan yang lebih baik dalam pengembangan dan manajemen startup. 
                    Berdasarkan pemahaman tentang faktor-faktor yang memengaruhi pertumbuhan dan penurunan, perhatikan tindakan yang dapat diambil untuk meminimalkan risiko dan memaksimalkan peluang kesuksesan startup di masa depan.
                    """)

        #####

    elif selected_category == "Analisis Hubungan":
        st.subheader("Hubungan Antara Funding Rounds dan Status Perusahaan")
        # Buat scatter plot
        plt.figure(figsize=(8, 6))
        plt.scatter(df['Age'], range(len(df)), c=pd.factorize(df['Gender'])[0], cmap='viridis')
        plt.xlabel('Age')
        plt.ylabel('Index')
        plt.title('Scatter Plot: Age vs Index colored by Gender')
        plt.colorbar(label='Gender')
        st.pyplot()

        #####

        fig = px.scatter(df1, x='Age', y='Adaptivity Level', size='Adaptivity Level', 
                 hover_name=df1.index, title='Bubble Plot: Age vs Adaptivity Level colored by Gender',
                 labels={'Age': 'Age', 'Adaptivity Level': 'Adaptivity Level'}, 
                 size_max=30)  # ukuran maksimum bubble

        # Menampilkan bubble plot di dashboard Streamlit
        st.plotly_chart(fig)

        #####

        sizes = df1['Adaptivity Level'] * 100  # Skala faktor untuk ukuran titik

        # Buat bubble plot
        plt.figure(figsize=(8, 6))
        plt.scatter(df1['Age'], df1['Adaptivity Level'], s=sizes, alpha=0.5)
        plt.xlabel('Age')
        plt.ylabel('Adaptivity Level')
        plt.title('Bubble Plot: Age vs Adaptivity Level')
        plt.grid(True)
        st.pyplot()

    else:
        # Dropdown untuk kolom "Adaptivity Level"
        Adaptivity_Level = st.selectbox('Pilih Jenis Adaptivity Level', [i for i in sorted(df['Adaptivity Level'].unique())])
        if Adaptivity_Level == "Low":

            st.subheader("Komposisi Status Startup dalam Pie Chart")
            low_adaptivity_counts = df[df['Adaptivity Level'] == 'Low']['Gender'].value_counts()
            
            # Membuat pie chart
            fig, ax = plt.subplots()
            ax.pie(low_adaptivity_counts, labels=low_adaptivity_counts.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Tambahkan judul
            plt.title('Distribusi Tingkat Adaptivitas Rendah Berdasarkan Gender')

            # Menampilkan pie chart di dashboard Streamlit
            st.pyplot(fig)

            st.markdown("**1. Interpretasi**")
            st.markdown("""
                        - Sebanyak 79.9% startup berstatus 'Operating'.
                        - Sebanyak 9.4% startup berstatus 'Closed'.
                        - Sebanyak 8.4% startup berstatus 'Acquired'.
                        - Sebanyak 2.3% startup berstatus 'IPO'.
                        """)
            
            st.markdown("**2. Insight**")
            st.markdown("""
                        - Mayoritas startup masih beroperasi (79.9%). Menunjukkaan bahwa masih banyak perusahaan yang masih dalam tahap awal pengembangan.
                        - Masih ada risiko kegagalan untuk startup walau tidak terlalu tinggi (9.4%) dengan tutupnya perusahaan.
                        - Cukup sedikit startup yang mencapai kesuksesan melalui akuisisi (8.4%).
                        - Hanya sedikit startup yang mencapai IPO (2.3%). Menunjukkan bahwa masih banyak startup yang membutuhkan waktu dan sumber daya yang lebih baik untuk mencapai tahap pertumbuhan yang matang.
                        """)
            
            st.markdown("**3. Actionable**")
            st.markdown("""
                        - Pemerintah ataupun pemangku kepentingan terkait perlu terus memberikan dukungan kepada startup yang sedang beroperasi agar dapat terus berkembang dan dapat mencapai kesuksesan.
                        Dukungan dapat diberikan dalam bentukk pendanaan ataupun yang lainnya.
                        - Melihat masih ada risiko kegagalan walau tidak terlalu tinggi, para pemangku kepentingan terkait perlu menyusun strategi, model bisnis, keuangan, atau hal-hal lain yang sekiranya diperlukan agar tidak meraih kegagalan nantinya.
                        - Melihat masih ada peluang untuk startup diakuisisi, para pemangku kepentingan terkait perlu memperluas jaringan dan hubungan dengan perusahaan yang mungkin tertarik untuk mengakuisisi startup yang dimiliki. 
                        Dan memastikan bahwa startup yang dimiliki memiliki nilai yang jelas dan menarik bagi calon pembeli.
                        """)

# Halaman Prediksi
else:
    st.subheader("Silakan Prediksi.")

    input_data = {}
    col1, col2 = st.columns(2)

    with col1:
            # Dropdown untuk kolom "Gender"
            Gender = st.selectbox('Pilih Gender', [i for i in sorted(df['Gender'].unique())])

            # Dropdown untuk kolom "Age"
            Age = st.selectbox('Pilih Range Umur (Tahun)', [i for i in sorted(df['Age'].unique())])

            # Dropdown untuk kolom "Age"
            Education_Level = st.selectbox('Pilih Tingkat Pendidikan', [i for i in sorted(df['Education Level'].unique())])

            # Dropdown untuk kolom "Institution Type"
            Institution_Type = st.selectbox('Pilh Tipe Institusi', [i for i in sorted(df['Institution Type'].unique())])

            # Dropdown untuk kolom "IT Student"
            IT_Student = st.selectbox('Apakah belajar di bidang IT?', [i for i in sorted(df['IT Student'].unique())])

            # Dropdown untuk kolom "Location"
            Location = st.selectbox('Apakah lokasi nya di Kota?', [i for i in sorted(df['Location'].unique())])

            # Dropdown untuk kolom "Load-shedding"
            Loadshedding = st.selectbox('Pilih Load-shedding', [i for i in sorted(df['Load-shedding'].unique())])

    with col2:
            # Dropdown untuk kolom "Financial Condition"
            Financial_Condition = st.selectbox('Pilih Kondisi Keuangan', [i for i in sorted(df['Financial Condition'].unique())])

            # Dropdown untuk kolom "Internet Type"
            Internet_Type = st.selectbox('Pilih Jenis Internet', [i for i in sorted(df['Internet Type'].unique())])

            # Dropdown untuk kolom "Network Type"
            Network_Type = st.selectbox('Pilih Jenis Jaringan', [i for i in sorted(df['Network Type'].unique())])

            # Dropdown untuk kolom "Class Duration"
            Class_Duration = st.selectbox('Pilih Range Durasi Kelas (Jam)', [i for i in sorted(df['Class Duration'].unique())])

            # Dropdown untuk kolom "Self Lms"
            Self_Lms = st.selectbox('Apakah institusi nya memiliki LMS sendiri?', [i for i in sorted(df['Self Lms'].unique())])

            # Dropdown untuk kolom "Device"
            Device = st.selectbox('Pilih Jenis Device', [i for i in sorted(df['Device'].unique())])

    data = pd.DataFrame({
        'Gender': [df[df['Gender'] == Gender].index[0]],
        'Age': [df[df['Age'] == Age].index[0]],
        'Education Level': [df[df['Education Level'] == Education_Level].index[0]],
        'Institution Type': [df[df['Institution Type'] == Institution_Type].index[0]],
        'IT Student': [df[df['IT Student'] == IT_Student].index[0]],
        'Location': [df[df['Location'] == Location].index[0]],
        'Load-shedding': [df[df['Load-shedding'] == Loadshedding].index[0]],
        'Financial Condition': [df[df['Financial Condition'] == Financial_Condition].index[0]],
        'Internet Type': [df[df['Internet Type'] == Internet_Type].index[0]],
        'Network Type': [df[df['Network Type'] == Network_Type].index[0]],
        'Class Duration': [df[df['Class Duration'] == Class_Duration].index[0]],
        'Self Lms': [df[df['Self Lms'] == Self_Lms].index[0]],
        'Device': [df[df['Device'] == Device].index[0]]
    })
    button = st.button('Prediksi')

    if button:
        filename='dtc.pkl'
        with open(filename,'rb') as file:
            loaded_model = pickle.load(file)

        predicted = loaded_model.predict(data)
        
        if predicted[0] == 0:
            # st.markdown('<p style="color:lightred;">Tingkat adaptasi nya adalah Low (Rendah)</p>', unsafe_allow_html=True)
            st.error("Tingkat adaptasi nya adalah Low (Rendah)")
        elif predicted[0] == 1:
            # st.markdown('<p style="color:orange;">Tingkat adaptasi nya adalah Moderate (Sedang)</p>', unsafe_allow_html=True)
            st.warning("Tingkat adaptasi nya adalah Moderate (Sedang)")
        elif predicted[0] == 2:
            # st.markdown('<p style="color:lightgreen;">Tingkat adaptasi nya adalah High (Tinggi)</p>', unsafe_allow_html=True)
            st.success("Tingkat adaptasi nya adalah High (Tinggi)")
        else:
            st.write('Not Defined')
