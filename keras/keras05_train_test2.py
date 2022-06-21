import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#1. 데이터
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,2,3,4,5,6,7,8,9,10])
# x_train = np.array ([1,2,3,4,5,6,7])
# x_test = np.array([8,9,10])
# y_train = np.array ([1,2,3,4,5,6,7])
# y_test = np.array([8,9,10])
x_train = x[:7]
x_test = x[7:]
y_train = y[:7]
y_test = y[7:]

print(x_train)
print(x_test)
print(y_train)
print(y_test)


#2. 모델구성
model = Sequential()
model.add(Dense(100, input_dim=1))
model.add(Dense(100))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=100, batch_size=1)

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)
result = model.predict([11])
print('11의 예측값 : ', result)

# loss :  3.031649096259942e-13
# 11의 예측값 :  [[11.000002]]
