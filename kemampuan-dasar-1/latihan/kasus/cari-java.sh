
hitung_extension=`ls -1 *.java 2>/dev/null | wc -l`
if [ $hitung_extension != 0 ]
then 
	echo Ada file Java pada direktori $(pwd) 

fi 
