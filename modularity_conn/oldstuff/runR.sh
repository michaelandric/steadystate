#!/bin/bash

subj=$1
vox=$2
tp=$3
cond=$4

R CMD BATCH --vanilla "--args $subj $vox $tp $cond" 4.corr.R

