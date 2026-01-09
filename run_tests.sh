#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python3 -m pytest chat_gpt/tests -vv
