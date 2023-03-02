#!/usr/bin/env bash
sudo rsync -Praz \
-e 'ssh -p 33' \
--exclude=.git \
--exclude=.idea \
--exclude=__pycache__ \
--exclude=.gitignore \
--exclude=ENV \
--exclude=send_to_server.sh \
--exclude=postgres_data \
/home/andrey/my_proj/FOR_WORK_TEST/2 \
root@194.87.98.68:/root/projects/test_2/

# 7f6YuTaKf0

