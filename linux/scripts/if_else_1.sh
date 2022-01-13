#!/usr/bin/bash

for i in {1..10};
do
	if (($i % 2 == 0))
	then
		echo "$i : even";
	else
		echo "$i : odd";
	fi
	
done;