from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class InputData(BaseModel):
    personage: int
    personincome: float
    personhomeownershipOWN: int
    personhomeownershipMORTGAGE: int
    personhomeownershipRENT: int 
    personhomeownershipOTHER: int 
    personemplength: int
    loanintentEDUCATION: int
    loanintentMEDICAL: int
    loanintentVENTURE: int
    loanintentPERSONAL: int
    loanintentHOMEIMPROVEMENT: int
    loanintentDEBTCONSOLIDATION: int
    loangrade: int
    loanamnt: float
    loanintrate: float
    loanpercentincome: float
    cbpersondefaultonfileN: int
    cbpersondefaultonfileY: int
    cbpersoncredhistlength: int

class Fraud():
    def __init__(self):
        self.model = joblib.load('model_xgb_credit.joblib')
        
    def data_preparation(self, data):
        df = pd.DataFrame(data, index=[0])
        return df

    def get_prediction(self,df):
        #pred = self.model.predict(df)
        pred_proba = self.model.predict_proba(df)[:, 1]
        return pred_proba

@app.post("/predict")
async def ipredict(input_data: InputData):
    data = input_data.dict()
    pipeline = Fraud()
    df_pred = pipeline.data_preparation(data)
    pred_proba = pipeline.get_prediction(df_pred)
    return {"Credit Risk" : float(pred_proba)}