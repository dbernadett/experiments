fswatch -l 0.05 -o test.py | xargs -n1 -I{} bash run.sh
