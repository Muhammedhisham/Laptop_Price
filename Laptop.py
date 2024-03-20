from flask import Flask,render_template,request
import pickle
import pandas as pd

with open(r'C:\Users\hisha\Desktop\Python\Laptop\output.pkl', 'rb') as f:
    model = pickle.load(f)
data=pd.read_csv(r'C:\Users\hisha\Desktop\Python\Laptop\Cleaned.csv')

app = Flask(__name__)

@app.route('/')
def home():
    Company=sorted(data['Company'].unique())
    TypeName=sorted(data['TypeName'].unique())
    Inches=sorted(data['Inches'].unique())
    ScreenResolution=sorted(data['ScreenResolution'].unique())
    Ram=sorted(data['Ram'].unique())
    Gpu=sorted(data['Gpu'].unique())
    OpSys=sorted(data['OpSys'].unique())
    Memory1=sorted(data['Memory1'].unique())
    Memory2=sorted(data['Memory2'].unique())
    Processor=sorted(data['Processor'].unique())
    return render_template('index.html',Company=Company,TypeName=TypeName,Inches=Inches,ScreenResolution=ScreenResolution,Ram=Ram,Gpu=Gpu,OpSys=OpSys,Memory1=Memory1,Memory2=Memory2,Processor=Processor)

@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        
        Company = None
        Company = int(Company.replace(' ', '')) if isinstance(Company, str) else Company
        TypeName = None
        TypeName = int(TypeName.replace(' ', '')) if isinstance(TypeName, str) else TypeName
        Inches = None
        Inches = float(Inches.replace(' ', '')) if isinstance(Inches, str) else Inches
        ScreenResolution = None
        ScreenResolution = int(ScreenResolution.replace(' ', '')) if isinstance(ScreenResolution, str) else ScreenResolution
        
        Ram = None
        Ram = float(Ram.replace(' ', '')) if isinstance(Ram, str) else Ram
                
        Gpu = None
        Gpu = int(Gpu.replace(' ', '')) if isinstance(Gpu, str) else Gpu
        OpSys = None
        OpSys = int(OpSys.replace(' ', '')) if isinstance(OpSys, str) else OpSys   

        Memory1 = None
        Memory1 = int(Memory1.replace(' ', '')) if isinstance(Memory1, str) else Memory1
        
        Memory2 = None
        Memory2 = int(Memory2.replace(' ', '')) if isinstance(Memory2, str) else Memory2
        Processor = None
        Processor = int(Processor.replace(' ', '')) if isinstance(Processor, str) else Processor
                   
        
            #['Company', 'TypeName', 'Inches', 'ScreenResolution', 'Ram', 'Gpu',
    #    'OpSys', 'Memory1', 'Memory2', 'Processor']
    #([[0,4,14,15,8.0,61,5,12,6,13]])
#     Company           1273 non-null   int32  
#  1   TypeName          1273 non-null   int32  
#  2   Inches            1273 non-null   object 
#  3   ScreenResolution  1273 non-null   int32  
#  4   Ram               1273 non-null   float64
#  5   Gpu               1273 non-null   int32  
#  6   OpSys             1273 non-null   int32  
#  7   Memory1           1273 non-null   int32  
#  8   Memory2           1273 non-null   int32  
#  9   Processor         1273 non-null   int32  

        prediction = model.predict([[Company,TypeName,Inches,ScreenResolution,Ram,Gpu,OpSys,Memory1,Memory2,Processor]])
        prediction = prediction[0]
        print('prediction=', prediction)
        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5002)


