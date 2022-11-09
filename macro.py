# coding: utf-8

## inport文
import webiopi                      ##ライブラリをインポートする。
import RPi.GPIO as GPIO

##初期化
GPIO.setmode(GPIO.BCM)              ##GOIOのモードを「GPIO.BCM」に指定
MOTOR_A1 = 26;                      ##変数「MOTOR_A1」に26を代入
MOTOR_A2 = 19;                      ##変数「MOTOR_A2」に19を代入
MOTOR_B1 = 13;                      ##変数「MOTOR_B1」に13を代入
MOTOR_B2 = 12;                      ##変数「MOTOR_B2」に12を代入



def setup():
    GPIO.setup(MOTOR_A1, GPIO.OUT)  ##「MOTOR_A1」の値のGPIOを出力モードにする。
    GPIO.setup(MOTOR_A2, GPIO.OUT)  ##「MOTOR_A2」の値のGPIOを出力モードにする。
    GPIO.setup(MOTOR_B1, GPIO.OUT)  ##「MOTOR_B1」の値のGPIOを出力モードにする。
    GPIO.setup(MOTOR_B2, GPIO.OUT)  ##「MOTOR_B2」の値のGPIOを出力モードにする。



## 以下マクロ 前進
@webiopi.macro
def FW():
    GPIO.output(MOTOR_A1,GPIO.HIGH) ##変数「MOTOR_A1」の番号のピンの信号をHIGHにする。
    GPIO.output(MOTOR_A2,GPIO.LOW)  ##変数「MOTOR_A2」の番号のピンの信号をLOWにする。
    GPIO.output(MOTOR_B1,GPIO.HIGH) ##変数「MOTOR_B1」の番号のピンの信号をHIGHにする。
    GPIO.output(MOTOR_B2,GPIO.LOW)  ##変数「MOTOR_B2」の番号のピンの信号をLOWにする。

## 後退
@webiopi.macro
def BK():
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)

## 左旋回
@webiopi.macro
def LT():
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.HIGH)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    
## 右旋回
@webiopi.macro
def RT():
    GPIO.output(MOTOR_A1,GPIO.HIGH)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)

## 停止
@webiopi.macro
def ST():
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.LOW)