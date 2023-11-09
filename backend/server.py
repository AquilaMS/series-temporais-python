from fastapi import FastAPI, BackgroundTasks, HTTPException
import services 
import models

app = FastAPI()

@app.get('/')
def read_root():
    print(services.predict_future_values(days=7,product_name='Sony Alpha a7 III Camera'))
    return {'message': 'Working!'}

@app.post('/train')
def train_model(background_tasks : BackgroundTasks, train_model: models.TrainModel):
    try:
        background_tasks.add_task(services.train_model, train_model.product_name)
        return {'message': 'Training Started. Product: ' + train_model.product_name}  
    except:
        raise HTTPException(status_code=207, detail='Error')
    
@app.post('/trainall')
def train_model(background_task : BackgroundTasks):
    try:
        background_task.add_task(services.train_model_for_all)
        return {'message': 'Training Started'} 
    except:
        raise HTTPException(status_code=207, detail='Error')
    
@app.get('/predict')
def predict_next_values(predict_request : models.PredictRequest):
    try:
        return {'value':services.predict_future_values(predict_request)}
    except:
        raise HTTPException(status_code=207, detail='Error')
    
@app.get('/sale/insert')
def add_sale(sale : models.Sale):
    try:
        services.add_sale(sale=sale)
        return {'sale_inserted':sale}
    except:
        raise HTTPException(status_code=207, detail='Error')