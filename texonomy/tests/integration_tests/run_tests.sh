#!/bin/bash

green="$(tput setaf 2)"
bold="$(tput bold)"
reset="$(tput sgr0)"

for file in *.py; do
    echo "${green}${bold}Running test: ${file%.py}...${reset}"
    python $file > /dev/null
    echo "Done."
    echo "==================="
done

mkdir pdf
mv ./*.pdf pdf

mkdir tex
mv ./*.tex tex
