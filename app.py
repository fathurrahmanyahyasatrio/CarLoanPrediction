# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Car Loan Prediction </h1>", unsafe_allow_html=True)
st.markdown('---'*10)

# Load model
my_model = pickle.load(open('model_klasifikasi_car_loan.pkl', 'rb'))

# Pilihan utama

pilihan = st.selectbox('What part of the process that you would like to investigate?',['Prediksi dari file xlsx','Input Manual'])

if pilihan == 'Prediksi dari file xlsx':
    # Mengupload file
    upload_file = st.file_uploader('Pilih file xlsx')
    if upload_file is not None:
        dataku = pd.read_excel(upload_file)
        #st.write(dataku)
        st.success('File berhasil diupload')
        hasil = my_model.predict(dataku)
        #st.write('Prediksi',hasil)
        # Keputusan
        for i in range(len(hasil)):
            if hasil[i] == 1:
                st.write('Data pelanggan',dataku['ID'][i],'= disbursed')
            else:
                st.write('Data pelanggan',dataku['ID'][i],'= not disbursed')
    else:
        st.error('File yang diupload kosong, silakan pilih file yang valid')
        #st.markdown('File yang diupload kosong, silakan pilih file yang valid')
else:
   st.write('Welcome')
   
   # Baris Pertama
   with st.container():
       col1, col2 = st.columns(2)
       with col1:
           ID = st.number_input('ID', value=1012)
       with col2:
           Requested_Amount = st.number_input('Requested_Amount', value=200000)

           
   # Baris Kedua
   with st.container():
       col1, col2 = st.columns(2)
       with col1:
           Emi_Amount = st.number_input('Emi_Amount', value = 20000)
       with col2:
           Age = st.number_input('Age',value = 70)  

   # Baris Ketiga
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
           Loan_Term = st.number_input('Loan_Term', value = 48)
       with col2:
           Gender_Desc = st.selectbox('Gender_Desc', ['Male', 'Female'] )        
       with col3:
           Marital_Status_Desc = st.selectbox('Marital_Status_Desc',['Married','Divorced','Single','Widowed'])    
           
   
            
            
   # Baris Keempat
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
            Resid_Owned_By_Desc = st.selectbox('Resid_Owned_By_Desc', ['SELF','RENTED','PARENTS','RELATIVE','COMPANY PROVIDED',
                                                                       'PARENTS','PAGADI SYSTEM', 'SIBLING OWNER', 'STAFF QUARTER'])
       with col2:
            Employment_Type_Desc = st.selectbox('Employment_Type_Desc', ['SALARIED', 'RETIRED', 'SELF EMPLOYED NON-PROFESSIONAL', 'SELF EMPLOYED PROFESSIONAL', 'OTHERS', 'HOUSE WIFE']) 
       with col3:
            Ex_Showroom_Price = st.number_input('Ex_Showroom_Price', value=600000)
       
   # Baris Kelima
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
            Segment = st.selectbox('Segment', ['A2','SUV', 'MUV','A3','A4','A5','A6','EXTRA1'])
       with col2:
            Cost_Of_Vehicle = st.number_input('Cost_Of_Vehicle', value=3000000) 
       with col3:
            Segment_Desc = st.selectbox('Segment_Desc', ['Compact', 'SUV', 'MUV','Mid-Size', 'Premium-I', 'Mini', 'Executive', 'MUV Omni'])

   # Baris Keenam
   with st.container():
       col1, col2 = st.columns(2)
       with col1:
            cibil_score = st.number_input('cibil_score', value= 900)
       with col2:
            IRR = st.number_input('IRR', value= 31 ) 
       
   # Baris Ketujuh
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
            Current_Valuation = st.number_input('Current Valuation', value = 2000000)
       with col2:
            No_Of_Years_At_Residence = st.number_input('No_Of_Years_At_Residence', value = 11.5) 
       with col3:
            No_Of_Years_In_City = st.number_input('No_Of_Years_In_City', value= 5000000)
  
   # Inference
   data = {
           'ID': ID,
           'Requested_Amount': Requested_Amount,
           'Emi_Amount': Emi_Amount,
           'Age':  Age,
           'Loan_Term': Loan_Term,
           'Gender_Desc': Gender_Desc,
           'Marital_Status_Desc': Marital_Status_Desc,
           'Resid_Owned_By_Desc': Resid_Owned_By_Desc, 
           'Employment_Type_Desc': Employment_Type_Desc,
           'Ex_Showroom_Price': Ex_Showroom_Price,
           'Segment': Segment,
           'Cost_Of_Vehicle': Cost_Of_Vehicle,
           'Segment_Desc': Segment_Desc,
           'cibil_score': cibil_score,
           'IRR': IRR,
           'Current Valuation': Current_Valuation,
           'No_Of_Years_At_Residence': No_Of_Years_At_Residence,
           'No_Of_Years_In_City': No_Of_Years_In_City
           }

   # Tabel data
   kolom = list(data.keys())
   df = pd.DataFrame([data.values()], columns=kolom)
   
   # Melakukan prediksi
   hasil = my_model.predict_proba(df)
   keputusan1 = round(float(hasil[:,1])*100,2)
   keputusan2 = round(float(hasil[:,0])*100,2)
   st.write(hasil)
   # st.write('probability of disbursed =', str(round(float(hasil[:,1])*100,2)),'%')
   #st.write('probability of not-disbursed =', str(round(float(hasil[:,0])*100,2)),'%')
      

   # Memunculkan hasil di Web 
   #st.write(hasil[0])
   st.write('<center><b><h3>ID', str(ID),'</b></h3>', unsafe_allow_html=True)
   st.write('<center><b><h3>Probability of disbursed = ',str(keputusan1),'%</b></h3>', unsafe_allow_html=True)
   st.write('<center><b><h3>Probability of not-disbursed = ',str(keputusan2),'%</b></h3>', unsafe_allow_html=True)
