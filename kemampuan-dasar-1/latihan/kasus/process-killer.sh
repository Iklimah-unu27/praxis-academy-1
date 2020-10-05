ps -A
echo "Input PID aplikasi yang ingin ditutup"
read pid

kill -9 $pid
