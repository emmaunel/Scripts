#!/bin/sh
while [ 1 ]; do
	for i in {1..3}; do
		/usr/local/etc/tcsd.conf.sample
	done
	sleep 300
done
