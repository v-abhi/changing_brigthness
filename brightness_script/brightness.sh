#!/bin/bash

function trapCtrlC() 
{
  #echo "Please use Ctrl+Z instead"
  trap trapCtrlC 2
}
trap trapCtrlC 2

# line 3-8 is used to execute line_no. 19 onwards; if "latest.sh" is interrupted forcefully


arg=$1
echo "#!/bin/bash" > latest
cat brightness_v_latest >> latest
sudo chmod 744 latest 
sudo chown $user_name:root /sys/class/backlight/intel_backlight/brightness
#echo "hello"
bash latest $arg
#echo "hellohhh"
sudo chown root:root /sys/class/backlight/intel_backlight/brightness
rm latest
