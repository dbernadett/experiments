#!/usr/bin/env bash
NAME=$1
G++ "$NAME.cpp" -o "$NAME" && "./$NAME"
