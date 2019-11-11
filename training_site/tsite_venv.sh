#run this script with "source ./tsite_venv.sh" instead of the usual "./tsite_venv.sh"
echo "run 'deactivate' to exit venv"
virtualenv --no-site-packages --distribute tsite_venv && source tsite_venv/bin/activate && pip install -r requirements.txt
