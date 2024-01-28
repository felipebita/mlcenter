from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class InputData(BaseModel):
    type_CASH_OUT: int
    type_TRANSFER: int
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float

class Fraud():
    def __init__(self):
        self.model = joblib.load('model_rf_fraud.joblib')
        
    def data_preparation(self, data):
        df = pd.DataFrame(data, index=[0])
        return df

    def get_prediction(self,df):
        pred = self.model.predict(df)
        return pred

@app.post("/predict")
async def ipredict(input_data: InputData):
    data = input_data.dict()
    pipeline = Fraud()
    df_pred = pipeline.data_preparation(data)
    pred = pipeline.get_prediction(df_pred)
    return {"prediction" : 'Fraud' if pred == 1 else 'Not Fraud'}
  
