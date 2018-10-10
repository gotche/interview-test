#!/bin/bash

mypy distance.py && flake8 . && pytest

