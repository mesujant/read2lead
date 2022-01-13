#!/usr/bin/bash

FILENAME="test_output.html";	
curl --max-time 2 https://onlineedlreg.dotm.gov.np/ > $FILENAME;
FILESIZE=$(stat -c%s "$FILENAME");

if [$FILESIZE > 0];
then
	echo "found";
else
	echo "Not found";
fi;
