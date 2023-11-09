import db
import pandas as pd
import transforms
import joblib
from pmdarima.arima import auto_arima
from models import PredictRequest, Sale

def train_model_for_all():
    base_data = pd.DataFrame(db.get_all_sales())
    all_products = base_data['product_name'].unique()
    for product in all_products:
        train_model(product_name=product)

def train_model(product_name):
    got_product = pd.DataFrame(db.get_one_product_sales(product_name=product_name))
    series = transforms.complete_series(df=got_product, product_name=product_name)
    auto_model = auto_arima(series,trace=True,stepwise=False,seasonal=True,stationary=False,max_p=5,max_q=5,max_P=5,max_Q=5,start_p=0,start_P=0,start_Q=0,m=12)
    joblib.dump(auto_model, 'models/'+ product_name +'.joblib')
    print(auto_model)

def predict_future_values(predict_request : PredictRequest):
    model = joblib.load('models/'+ predict_request.product_name +'.joblib')
    forecasts = model.predict(n_periods=predict_request.days)
    full_forecast = round(forecasts.sum())
    return full_forecast

def add_sale(sale : Sale):
    print(sale)
    db.add_sale(sale)
