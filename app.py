# Import library yang dibutuhkan
import numpy as np
import seaborn as sns
import pandas as pd
import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import datetime as dt
import calendar
import time
matplotlib.use('Agg')
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False) #Disable error bila error terjadi pada chart

#Design sidebar pada dashboard
st.sidebar.title("Ecommerse Churn Analysis")
st.sidebar.markdown("Dashboard Analisis Churn data milik perusahaan ECommerce")


def main():

    df = pd.read_csv("ECommerceDataset_clean.csv") #read data dari EcommerseDataset yang telah di proceed dan di clean

    menu = ['Explore your dataset','Visualisasi Dataset','EDA','Modeling Test'] #Menu Sidebar
    choice=st.sidebar.selectbox("Menu",menu)
    if choice=='Explore your dataset':
        st.image("analysis1.jpg",use_column_width=True)
        st.info("Dashboard ini dibuat sebagai halaman data explore, dimana data dapat ditampilkan sesuai dengan yg di inginkan, dapat juga melihat dataset summary, dan juga apakah terdapat data yang missing values.")
        st.header("Explore your dataset")
        #df=pd.read_csv(data) test23


        if st.checkbox("Show Dataset"): #checkbox untuk menampilkan dataset
            number=st.number_input("Number of Rows to view",5,15)
            st.dataframe(df.head(number))
            st.success("Data loaded successfully") 


            data_dim= st.radio("Shape of the dataset:", ("Number of Rows","Number of Columns")) #radio button widget
            if st.button("Show Dimension"):
                if data_dim== 'Number of Rows':
                    st.write(df.shape[0])
                elif data_dim== 'Number of Columns':
                    st.write(df.shape[1])
                else:
                    st.write(df.shape)

            Info =['Dataset Information','Display Multiple Columns','Display the dataset summary','Check for missing values in the dataset']
            options=st.selectbox("Pilihan - pilihan terhadap dataset",Info)


            if options==('Dataset Information'): #cemacem dataset
                st.markdown("**CustomerID**: Nomor identitas pengguna.")
                st.markdown("**Churn**: Identifikasi pengguna churn atau tidak (1 Churn, 0 Tidak Churn).")
                st.markdown("**Tenure**: Masa pengguna berlangganan pada produk ini.")
                st.markdown("**PreferredLoginDevice**: Perangkat yang sering digunakan untuk login.")
                st.markdown("**CityTier**: Klasifikasi kota berdasarkan tingkat kesejahteraan di kota tersebut.")
                st.markdown("**WarehouseToHome**: Jarak antara gudang dan rumah pengguna.")
                st.markdown("**PreferredPaymentMode**: Metode pembayaran yang sering digunakan untuk pengguna.")
                st.markdown("**Gender**: Jenis kelamin pengguna.")
                st.markdown("**HourSpendOnApp**: Jam yang dihabiskan untuk menggunakan aplikasi atau website.")
                st.markdown("**NumberOfDeviceRegistered**: Jumlah perangkat yang diregistrasikan terhadap satu pengguna/akun.")
                st.markdown("**PreferredOrderCat**: Kategori yang sering dipesan dalam satu bulan terakhir.")
                st.markdown("**SatisfactionScore**: Nilai kepuasan pelanggan terhadap pelayanan.")
                st.markdown("**MaritalStatus**: Status pernikahan pelanggan.")
                st.markdown("**NumberOfAddress margin percentage**: Jumlah alamat yang terdaftar dalam satu pengguna.")
                st.markdown("**Complain**: Keluhan yang diajukan dalam satu bulan terakhir.")
                st.markdown("**OrderAmountHikeFromLastYear**: Persentase peningkatan pesanan dalam satu tahun terakhir.")
                st.markdown("**CouponUsed**: Jumlah kupon yang digunakan dalam satu bulan terakhir.")
                st.markdown("**OrderCount**: Jumlah pesanan dalam satu bulan terakhir.")
                st.markdown("**DaySinceLastOrder**: Hari terakhir pemesanan yang dilakukan oleh pelanggan.")
                st.markdown("**CashbackAmount**:Rata-rata cashback dalam satu bulan terakhir.")

            if options=='Display Multiple Columns': #bila ingin menampilkan kolom tertentu
                 selected_columns=st.multiselect('Select Preferred Columns:',df.columns)
                 df1=df[selected_columns]
                 st.dataframe(df1)

            if options=='Check for missing values in the dataset': 
                 st.write(df.isnull().sum(axis=0)) #cekk null values
                 if st.button("Drop Null Values"):
                     df=df.dropna() #drop null values
                     st.success("Null values droped successfully")


            if options=='Display the dataset summary':
                 st.write(df.describe().T)
                 

    elif choice=='Visualisasi Dataset':
        st.image("visuals.jpeg",use_column_width=True)
        st.info("Dashboard ini dibuat sebagai halaman Visualisasi Data, dimana data dapat divisualisasikan sesuai dengan meassure, fact / labels, serta bar chart yg di inginkan")
        st.header("Visualisasikan dataset yang anda inginkan")
        # #df=pd.read_csv(data)
        #     #st.dataframe(df.head(50))
        # df['Churn']=pd.to_datetime(df['date_time'])

        # df['Month']=pd.DatetimeIndex(df['date_time']).month
        # #hadeuh
        # df['MonthName'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
        # df['date_time'] = pd.to_datetime(df['date_time'])
        # df['Hour'] = (df['date_time']).dt.hour


        if st.button("Show Dataset again"):
            st.dataframe(df.head(50)) #menampilkan kembali 50 dataset apabila diperlukan

        col1,col2,col3=st.columns(3)

        st.subheader("Bar Chart / Horizontal Bar Chart / Scatter Bar / Plot Bar")
        with col1:
            measure_selection = st.selectbox('Choose a Measure:', ['Churn','Tenure','WarehouseToHome','HourSpendOnApp','OrderAmountHikeFromlastYear','CouponUsed','OrderCount','DaySinceLastOrder'], key='1')
        with col2:
            fact_selection = st.selectbox('Choose a Fact:', ["PreferredLoginDevice", "CityTier", "PreferredPaymentMode", "Gender", "PreferedOrderCat", "MaritalStatus", "Complain"], key='1')
            ax=df.groupby([fact_selection])[measure_selection].aggregate('sum').reset_index().sort_values(measure_selection,ascending=True)
            dx=df.groupby([fact_selection])[measure_selection].aggregate('sum').reset_index().sort_values(fact_selection,ascending=True)
            #cust_data=ax xxx gatau mau diapain tar aj
        with col3:
            type_of_plot=st.selectbox("Select Type of Plot",["Bar Chart","Horizontal Bar", "Scatter Bar", "Plot Bar"])

        if type_of_plot=='Bar Chart':
            st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
            plt.xticks(rotation=45)
                #plt.subplots(figsize=(15, 7))
            plt.autoscale()
            plt.tight_layout(rect=(0, 0.25, 1, 1))
            plt.bar(ax[fact_selection], ax[measure_selection], align='center')
            plt.ylabel(fact_selection)
            st.pyplot()
    

        elif type_of_plot=='Horizontal Bar':
            st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
            plt.barh(ax[fact_selection], ax[measure_selection], align='center')
            #plt.barh(ax[measure_selection], ax[fact_selection])
            st.pyplot()
        
        
        elif type_of_plot=='Scatter Bar':
            st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
            plt.autoscale()
            plt.xticks(rotation=45)
            plt.xlabel(measure_selection)
            plt.tight_layout(rect=(0, 0.25, 1, 1))
            plt.scatter(ax[fact_selection], ax[measure_selection],color='green')
            plt.ylabel(fact_selection)
            plt.grid(True)
            st.pyplot()
            
            
        elif type_of_plot=='Plot Bar':
            st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
            plt.autoscale()
            plt.xticks(rotation=45)
            plt.xlabel(measure_selection)
            plt.tight_layout(rect=(0, 0.25, 1, 1))
            plt.plot(ax[fact_selection], ax[measure_selection],color='red')
            plt.ylabel(fact_selection)
            plt.grid(True)
            st.pyplot()        

        st.subheader("Donut Chart")
        #col5 = st.columns(1)
        #st.button('Donut Chart')
        st.success("Menampilkan Donut Chart untuk pengukuran {} terhadap {}".format(measure_selection,fact_selection))
        labels = dx[fact_selection].unique()
        #labels = ax[measure_selection].unique()
        #values =df.groupby([measure_selection])[fact_selection].sum()
        values =df.groupby([fact_selection])[measure_selection].sum()
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
        #fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
        st.plotly_chart(fig)
        
        
        
        # st.subheader("FF Chart")
        # st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
        # x1 = np.random.randn(200) - 2
        # x2 = np.random.randn(200)
        # x3 = np.random.randn(200) + 2
        # labels = [x1, x2, x3]
        # values =df.groupby([fact_selection])[measure_selection].sum()
        # fig = ff.create_distplot(
        #  labels, values, bin_size=[.1, .25, .5])
        # st.plotly_chart(fig, use_container_width=True)
        
        # st.subheader("Bubble Chart")
        # st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
        # labels = dx[fact_selection].unique()
        # values =df.groupby([fact_selection])[measure_selection].sum()
        # fig = go.Figure(go.Bar(labels, values, orientation='h'))
        # st.plotly_chart(fig)
        

    elif choice=='EDA':
        st.image("EDA.png",use_column_width=True)
        st.info("Dashboard ini dibuat sebagai halaman Exploratory data analysis")
        st.header("Data Distribution")
        st.image('D1.png',use_column_width=True)
        D1 = '''
Observations:

Dari data set, customer yang churn mendekati 20%, sedangkan yang tidak churn 
sekitar 80%.).'''
        st.code(D1, language='python')
        
        st.header("Data Korelasi")
        st.image('K1.png',use_column_width=True)
        K1 = '''
CouponUsed dan OrderCount berkorelasi kuat, make sense karena setiap pengguna
dengan lebih banyak kupon dapat memesan lebih banyak barang.<br>'''
        st.code(K1, language='python')
        
        st.header("Demogprahic Dari Variabel")
        st.image('G1.png',use_column_width=True)
        G1 = '''
Observations:

- Gender: ~60% pengguna ecommerce hijau paling banyak adalah Laki-laki, yang
memiliki ~20% pengguna lebih banyak dari Perempuan yaitu ~40%.'''
        st.code(G1, language='python')
        
        st.image('G2.png',use_column_width=True)

        st.image('G3.png',use_column_width=True)
        G3 = '''
Observations
- Dari dataset, distribusi Laki-laki lebih banyak dari Perempuan
- Dari 16,8% customer yang churn, 10.7%% nya adalah Laki-Laki dan 6.2% nya 
adalah Perempuan
- Namun, dari 83.2% customer yang bertahan, yang paling banyak adalah 
Laki-Laki yaitu sebesar 49.4% dari keseluruhan pengguna, sedangkan 
Perempuan 33.7%
- Presentase Churn diantara pengguna dalam setiap Gender juga memperlihatkan
presentase Churn Laki-Laki ~19% .
Sedangkan diantara perempuan presentase Churn nya ~17%. Dua-duanya berada 
di hampir level presentase yang sama..'''

        st.code(G3, language='python')
        
        st.image('G4.png',use_column_width=True)
        G4 = '''
Observations
- Pengguna ecommerce paling banyak adalah orang yang sudah menikah yaitu ~50%
- Pengguna yang Single memiliki presentase Churn paling banyak yaitu ~30%.
.'''
        st.code(G4, language='python')

        st.header("Rangkuman EDA")    
        st.markdown('Karena keterbatasan waktu, dan juga efisiensi webpage'
                    'Akan di rangkum EDA yang telah di analis sebagai berikut')
        Rangkuman = '''
Observations
1. Dari hasil observasi, customer yang churn sekitar 16%, sedangkan yang 
tidak churn sekitar 83%<br><br>

2. Variabel CouponUsed dan OrderCount berkorelasi kuat, make sense karena 
setiap pengguna dengan lebih banyak kupon dapat memesan lebih banyak barang. 
Namun, itu hanya 0,62 jadi sementara bisa dikeep datanya.<br><br>

3. Gender: Presentase Churn diantara pengguna dalam setiap Gender juga 
memperlihatkan presentase Churn Laki-Laki ~19%. Sedangkan diantara perempuan
presentase Churn nya ~17%. Dua-duanya berada di hampir level presentase yang sama.<br><br>

4. Marital Status: Pengguna yang Single memiliki presentase Churn paling 
banyak yaitu ~30%.<br><br>

5. Tenure: Semakin lama Tenur, maka kemungkinan untuk Churn berkurang. 
Pengguna baru memiliki kecenderungan untuk Churn lebih besar. Pengguna 
dengan Tenure 1 tahun memiliki kecenderungan Churn hampir 20% di banding 
pengguna di tahun ke 2 yang kurang dari 10%.<br><br>

6. Satisfaction Score: Tingkat kepuasan 5 adalah yang paling banyak Churn
pada tahun pertama. Tingkat kepuasan 5 memiliki kecenderungan Churn paling
banyak yaitu sekitar lebih dari 20%. Ternyata ~65% Pengguna yang memberikan
nilai Satisfaction Score 5, Churned pada Bulan ke 0, dan ~60% pada Bulan ke 1.
Meskipun memberikan Satisfaction Score 5, user dengan Cashback terendah 
USD 110 - 111 memiliki tingkat Churn 100%.<br><br>

7. Number of device registered: Pengguna yang mengakses Computer memiliki 
persentase Churn lebih tinggi di banding Mobile Phone (~20%)<br><br>

8. Hour Spend On App: Presentase Churn pengguna yang menggunakan aplikasi 
selama lebih dari 1 jam memiliki distribusi yang hampir sama ~18%<br><br>

9. Payment Mode: Presentase Churn yang paling tinggi adalah COD sekitar 
25%. Pengguna Credit Card memiliki presentase Churn paling rendah ~16%<br><br>

10. Complain: Pelanggan yang tidak memiliki complain, masih memiliki 
presentase Churn sebesar ~10%. Presentase Churn pelanggan complain 30%<br><br>

11. City Tier: Semakin tinggi City Tier, semakin tinggi pula presentase 
Churn. City Tier 2 & 3 memiliki presentase Churn yang hampir sama yaitu 
sekitar ~20%.<br><br>

12. Warehouse To Home: Tingkat presentase Churn pada jarak Warehouse ke 
rumah ada di sekitar 15% - 20%. Terjadi kenaikan signifikan pada jarak 
15km, 19km, dan juga 31km. Semakin jauh jarak rumah ke gudang, potensi 
churn semakin meningkat.<br><br>

13. Number of device registered: Semakin banyak jumlah device pengguna, 
semakin tinggi tingkat presentase Churn. 5 device ~21%, 1 device ~10%<br><br>

14. Preferred Order Category: Pengguna yang membeli pada kategori mobile 
phone memiliki presentase Churn paling tinggi yaitu ~30%, lebih tinggi 20%
dibandingkan pengguna yang membeli pada kategori Laptop & Accessory yaitu 10%. 
Paling rendah grocery ~5%<br><br>

15. Number of Address: Semakin banyak jumlah alamat yang terdaftar, 
maka tingkat Churn semakin tinggi. Customer dengan jumlah 12 alamat memiliki 
tingkat Churn paling tinggi sebesar 50%<br><br>

16. Order Amount Hike From Last Year: Tingkat presentase Churn memiliki siklus
Penurunan tiap 5 pesanan. 11-15 Pesanan dan 16-21 pesanan.  Peningkatan
Signifikan presentase Churn terjadi pada peningkatan jumlah pesanan 22-24. 
Tetapi, pada jumlah pesanan 25 terjadi penurunan kembali.<br><br>

17. Coupon Used: Distribusi tingkat presentase Churn hampir sama untuk
penggunaan jumlah kupon. Namun pengguna yang tidak pernah menggunakan kupon 
memiliki tingkat presentase Churn paling tinggi ~17.5%<br><br>

18. Order Count: Semakin banyak jumlah pesanan, maka semakin rendah 
presentase Churn. Presentase Churn Paling tinggi adalah order count 1 yaitu ~19%, 
Namun peningkatan Churn terjadi kembali pada Jumlah pesanan 6 yaitu ~17%<br><br>

19. Day Since Last Order: Semakin lama pengguna tidak melakukan pemesanan, 
maka tingkat Churn semakin rendah<br><br>

20. Cashback:Semakin tinggi cashback yang didapatkan, semakin rendah 
presentase Churn. Terdapat peningkatan Churn signifikan pada pelanggan 
yang mendapatkan Cashback 221-231 dollar.'''

        st.code(Rangkuman, language='python')

    elif choice=='Modeling Test':
        st.image("Kmeans.png",use_column_width=True)
        st.info("Dashboard ini dibuat sebagai halaman Modeling testing")    
        st.header("Model Testing")
        st.image('Sil3.png',use_column_width=True)
        Hipothesis = '''
Dapat dilihat plot di atas Yang terpilih adalah n_components 3 dengan skor 
silhouete 0,4 (Silhouter terbaik dari yg lain).'''
        st.code(Hipothesis, language='python')
        st.header('Aglomerative Clustering')
        st.image("Aglo.png",use_column_width=True)
        Aglo       = '''> Hasil dari aglomerative clustering dinilai cukup baik dengan jarak antar 
kelompok sudah terbentuk dengan jelas '''
        st.code(Aglo, language='python')
        
        st.header("Model Inference")
        st.markdown('Model Inference menggunakan KMeans dengan n_cluster =3')
        st.markdown('Kmeans Dipilih karena dinilai cukup baik dalam memvisualisasikan data dengan baik :')
        
        st.image('Model.png',use_column_width=10)
        klaster = '''
- Klaster 1 - 41.8% dari total sampel
- Klaster 0 - 34.9% dari total sampel
- Klaster 2 - 23.2% dari total sampel

 >1. Klaster 1 Menunjukan Jumlah dari orang-orang yang Churn karena alasan-alasan 
 dari yang sudah di paparkan pada EDA
 >2. Klaster 0 Menunjukan Jumlah dari orang-orang yang setia menggunakan applikasi
 >3. Klaster 2 Menunjukan Jumlah dari orang-orang yang berpotensi akan Churn
'''
        st.code(klaster, language='python')
        
        st.subheader('''SHAP
Untuk mendapatkan gambaran tentang fitur mana yang paling penting untuk sebuah model, lalu dapat 
memplot nilai SHAP dari setiap fitur untuk setiap sampel
Plot di bawah ini mengurutkan fitur berdasarkan jumlah besaran nilai SHAP pada semua sampel, 
dan menggunakan nilai SHAP untuk menunjukkan dampak distribusi yang dimiliki setiap fitur 
pada output model. Warna mewakili nilai fitur (merah High, biru Low)''')
       
        st.image("Shap.png",use_column_width=True)
        st.markdown('''
1. Tenure
  - Semakin singkat berlangganan potensi churn semakin meningkat
2. Complain
  - Semakin banyak complain potensi churn semakin meningkat
3. NumberOfAddress
  - Semakin banyak jumlah alamat yang terdaftar potensi churn semakin meningkat
4. CashbackAmount
  - Semakin sedikit jumlah Cashback yang didapat potensi churn semakin meningkat
5. DaySinceLastOrder
  - Semakin singkat interval pemesanan, potensi churn semakin meningkat
6. SatisfactionScore
  - Semakin tinggi nilai kepuasan, potensi churn semakin meningkat
7. NumberOfDeviceRegistered
  - Semakin banyak jumlah device yang terdaftar, potensi churn semakin meningkat
8. WarehouseToHome
 - Semakin jauh jarak dari gudang ke rumah, , potensi churn semakin meningkat''')
        
        
        st.header("Rekomendasi")
        Rekomendasi = '''
1. Untuk pengguna dengan masa tenure 0-1 bulan, diberikan insentif 
(bisa berupa package promo cashback), untuk mencegah potensi churn terhadap 
Pengguna baru.
2. Diperlukan perbaikan secara fungsi(aplikasi) maupun feedback pelayanan
(service) yang lebih responsif terhadap komplain dari user, untuk mencegah
pengguna akan churn.
3. Memberikan notifikasi pengingat (reminder) yang bisa digabungkan dengan
program insentif untuk pengguna yang telah melakukan pemesanan agar akun pengguna
kembali aktif dan tidak churn.
4. Memberikan insentif berupa pengurangan biaya ongkos kirim kepada pelanggan
yang memiliki jarak yang jauh terhadap gudang, bisa dengan melakukan kerja sama
dengan pihak jasa pengantar (kurir) untuk meringankan cost dari perusahaan.
5. Pengguna baru yang memberikan nilai Satisfaction Score 5 diberikan notifikasi
email untuk aktif kembali dengan isi email berupa visual grafis marketing ajakan
untuk kembali aktif menggunakan aplikasi.
'''
        st.code(Rekomendasi, language='python')
        #df=pd.read_csv(data)
     
if __name__ == '__main__':
    main()
