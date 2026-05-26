#!/data/data/com.termux/files/usr/bin/bash

number="<nomor_telepon>"# Ganti dengan nomor telepon target
message="ANDRO"# Ganti dengan pesan yang ingin Anda kirim

for i in {1..100}; do
  curl -s -X POST https://api.chat-api.com/instance28435/ \
    -H 'Content-Type: application/json' \
    -d '{"phone": "'$number'", "message": "'$message'"}'
done
