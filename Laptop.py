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
        
        Processor = request.form.get('Processor')
        Memory2 = request.form.get('Memory2')
        Memory1 = request.form.get('Memory1')
        OpSys = request.form.get('OpSys')
        Gpu = request.form.get('Gpu')
        Ram = request.form.get('Ram')
        ScreenResolution = request.form.get('ScreenResolution')
        Inches = request.form.get('Inches')
        TypeName = request.form.get('TypeName')
        Company = request.form.get('Company')

        input=pd.DataFrame([[Processor,Memory1,Memory2,OpSys,Gpu,Ram,ScreenResolution,Inches,TypeName,Company]],
                columns=['Processor','Memory1','Memory2','OpSys','Gpu','Ram','ScreenResolution','Inches','TypeName','Company'])
        # prediction=model.predict(input)[0]
        print('fndsfffffffffff$$$$$$$$$$$$$$$$$$$$',input)
          
        # return str(prediction)
      
        prediction = model.predict([[Processor,Memory1,Memory2,OpSys,Gpu,Ram,ScreenResolution,Inches,TypeName,Company]])
        prediction = prediction[0]
        print('prediction=', prediction)
        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5002)


