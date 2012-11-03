#!/bin/bash

subj=$1
vox=$2
tp=$3
cond=$4

echo | R --version > out.V

echo | which R > out.Loc 

echo | ls -lt /usr/bin/R > out.Link
