fswatch -o test_orm.py | xargs -n1 -I{} bash run-test.sh
