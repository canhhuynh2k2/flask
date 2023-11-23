from flask import Flask, request
from keras.models import load_model
import numpy as np
app = Flask(__name__)
    

@app.route('/lotrinh/calotieuthu', methods=['GET'])
def calo_can_dot():
   if request.method == 'GET':
       return predict_calories(request.get_json(force=True))


# Hàm dự đoán calo dựa trên đầu vào người dùng
def predict_calories(input):
    gender = input['gender']
    age = input['age']
    height = input['height']
    weight = input['weight']
    target_weight = input['target_weight']
    weight_loss_duration = input['weight_loss_duration']
    input_data = np.array([[gender, age, height, weight, target_weight, weight_loss_duration]])
    loaded_model = load_model('calotieuthuv1.keras')
    calories_prediction = loaded_model.predict(input_data)
    res = [int(x) for x in calories_prediction.flatten().tolist()]
    print(res)
    result = dict({'listCalo' : res[:weight_loss_duration]})
    return result
