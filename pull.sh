#!/bit/bash
git pull origin main
source .venv/bit/activate
pip install -r requirements.txt
sudo systemctl restart tgbot
echo "Successfully pulled P35TgBot!"