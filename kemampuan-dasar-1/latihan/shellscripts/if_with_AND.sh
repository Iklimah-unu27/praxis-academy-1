echo "Enter username"
read username
echo "Enter password"
read password

if [[ ( $username == "ini_admin" && $password == "ini_password" ) ]]; then
echo "valid user"
else
echo "invalid user"
fi
