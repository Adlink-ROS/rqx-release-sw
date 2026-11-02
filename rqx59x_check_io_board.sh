#!/bin/bash -e

# get pin numders and names from `sudo cat /sys/kernel/debug/gpio`
PIN_NAME1=PA.04
PIN_NAME2=PA.07
PIN_NAME3=PA.05
PIN_NAME4=PA.06
PIN_NUM1=352
PIN_NUM2=355
PIN_NUM3=353
PIN_NUM4=354

cleanup()
{
    echo "Cleaning up before exit..."    
    echo $PIN_NUM1 > /sys/class/gpio/unexport
    echo $PIN_NUM2 > /sys/class/gpio/unexport
    echo $PIN_NUM3 > /sys/class/gpio/unexport
    echo $PIN_NUM4 > /sys/class/gpio/unexport
}
trap cleanup EXIT

echo "Initial GPIO settings..."
echo $PIN_NUM1 > /sys/class/gpio/export
echo $PIN_NUM2 > /sys/class/gpio/export
echo $PIN_NUM3 > /sys/class/gpio/export
echo $PIN_NUM4 > /sys/class/gpio/export
sleep 0.1
echo "in" > /sys/class/gpio/$PIN_NAME1/direction
echo "in" > /sys/class/gpio/$PIN_NAME2/direction
echo "in" > /sys/class/gpio/$PIN_NAME3/direction
echo "in" > /sys/class/gpio/$PIN_NAME4/direction

sleep 0.1

# Get current values
ID0=$(cat /sys/class/gpio/$PIN_NAME1/value)
ID1=$(cat /sys/class/gpio/$PIN_NAME2/value)
ID2=$(cat /sys/class/gpio/$PIN_NAME3/value)
ID3=$(cat /sys/class/gpio/$PIN_NAME4/value)

echo "Get current ID:"
echo $ID0 $ID1 $ID2 $ID3

if [[ $ID0 == 0 && $ID1 == 1 && $ID2 == 0 && $ID3 == 1 ]]; then
	echo "ADLINK GMSL"
elif [[ $ID0 == 0 && $ID1 == 1 && $ID2 == 1 && $ID3 == 1 ]]; then
	echo "ADLINK FPDL"
else
	echo "LEOPARD"
fi
