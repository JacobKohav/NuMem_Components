#run this script with "source ./tsite_venv.sh" or instead of the usual "./tsite_venv.sh"
echo "run 'deactivate' to exit venv"
virtualenv venv && source venv/bin/activate && pip install -r requirements.txt
