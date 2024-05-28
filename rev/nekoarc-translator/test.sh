#!/bin/bash

command_to_run="./nekoarc.exe < tmp.txt"

# Run the command in a loop
while IFS= read -r line; do
	if [[ "$line" == *like* ]]; then
		echo "$line"
		break
	fi
done < <(eval "$command_to_run")
