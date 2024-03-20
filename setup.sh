echo '[]' > i
echo '[]' > c

pip install requests flask

# check exit code
if [ $? -eq 0 ]; then
    echo "Success"
else
    # lets try with python3
    python -m ensurepip
    python -m pip install --upgrade pip
    python -m pip install requests flask

    # check exit code
    python3 -m ensurepip
    python3 -m pip install --upgrade pip
    python3 -m pip install requests flask
fi
