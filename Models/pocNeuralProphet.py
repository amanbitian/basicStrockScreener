import pandas as pd
from neuralprophet import NeuralProphet
import matplotlib.pyplot as plt
from data.MysqlConnection import MysqlConnection

mysqlconnection= MysqlConnection()
connection= mysqlconnection.get_mysql_connection()
query= f"""
        select Date, Close from HDFC_Bank_Ltd_data;"""

## Read data from sql db
columns, results= mysqlconnection.execute_query(connection,query,'fetch')
df= pd.DataFrame(results, columns=columns)
print(df.shape)

df.columns = ['ds', 'y']

## Commenting this graph to avoid hault
# plt.plot(df['ds'], df['y'], label = 'actual', c = 'g')
# plt.show()

## train model

model = NeuralProphet()
model.fit(df)

### Evaluate model

future = model.make_future_dataframe(df, periods = 300)

forecast = model.predict(future)
actual_prediction = model.predict(df)

plt.plot(actual_prediction['ds'], actual_prediction['yhat1'], label = "prediction_Actual", c = 'r')
plt.plot(forecast['ds'], forecast['yhat1'], label = 'future_prediction', c = 'b')
plt.plot(df['ds'], df['y'], label = 'actual', c = 'g')
plt.legend()
plt.title('HDFC')
plt.show()

# model.plot_components(forecast)
# plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 8))
axs[0].plot(forecast['ds'], forecast['trend'], label='Trend', color='blue')
axs[1].plot(forecast['ds'], forecast['season_yearly'], label='Yearly Seasonality', color='orange')
axs[2].plot(forecast['ds'], forecast['season_weekly'], label='Weekly Seasonality', color='green')

for ax in axs:
    ax.legend()

plt.show()