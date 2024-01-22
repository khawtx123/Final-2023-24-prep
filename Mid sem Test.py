# pass is used as a placeholder in a loop
# Indicate an empty block of statements

search = 'Mini'
product = ' Apple iPad Mini 6 2021'

if search in product:
    print('Product Found !')
else:
    print('not found')

check = product.find(search)
if check != -1:
    print("Product Found")
else:
    print("Product not found")

temp_sensor_dict = {}
TemperatureSensorReading = "Sensor1/Lounge/2021.11.26 15:30/28.3"
sensor_data = TemperatureSensorReading.split('/')

temp_sensor_dict['SENSORID'] = sensor_data[0]
temp_sensor_dict['LOCATION'] = sensor_data[1]
temp_sensor_dict['DATETIME'] = sensor_data[2]
temp_sensor_dict['TEMPERATURE'] = sensor_data[3]

print(temp_sensor_dict)

TemperatureSensorReadingList = [
"Sensor1/Lounge/2021.11.26 15:30/28.3"
"Sensor2/Porch/2021.11.26 15:30/32.0"
"Sensor3/Porch/2021.11.26 16:30/32.6"
]

temperature_list = []
for temp in TemperatureSensorReadingList:
    sensor_data1 = temp.split('/')
    temperature_list.append(sensor_data1[-1])
temp_highest = max(temperature_list)
print(temp_highest)

sensor_highest_temp = []
for temp in TemperatureSensorReadingList:
    if temp_highest in temp:
        sensor_highest_temp = temp.split('/')
        break
print(sensor_highest_temp)
temp_sensor_max = {}