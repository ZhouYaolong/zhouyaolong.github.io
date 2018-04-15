# -*- coding: utf-8 -*-
listDictKeys = ['date', 'stateMorning', 'stateNight', 'temperatureMorning',
                'temperatureNight', 'windForceMorning', 'windForceNight', 'windDirectionMorning', 'windDirectionNight']

mongodbSetting = {
    'host': "127.0.0.1",  # 主机IP
    'port': 27017,  # 端口号
    'db': "pm25",  # 库名
    'collect': "history"  # collection名
}
