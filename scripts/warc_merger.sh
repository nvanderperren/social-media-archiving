#!/bin/bash

function show_usage () {
    printf "\nUsage: $0 [options [parameters]]\n"
    printf "\n"
    printf "Options: \n"
    printf " -i|--input [input folder], Path to folder with WARC files   REQUIRED!\n"
    printf " -o|--output [output name], Name of output WARC   REQUIRED!\n"
    printf " -h|--help, Print this help message\n\n"

    return 0
}

function merge_warcs () {
    python3 -m warcat --output "$OUTPUT.warc.gz" --force-read-gzip --gzip --progress concat $INPUT/*
}

if [[ $# != 4 ]] ; then
    show_usage
    exit 0
fi

while [ ! -z "$1" ] ; do
  if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
    show_usage
  elif [[ "$1" == "--input" ]] || [[ "$1" == "-i" ]]; then
    INPUT="$2"
    shift
  elif [[ "$1" == "--output" ]] || [[ "$1" == "-o" ]]; then
    OUTPUT="$2"
    shift
  else
    echo "Incorrect input provided"
    show_usage
  fi
  shift
done

merge_warcs