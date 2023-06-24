#!/usr/bin/env bash

# SPDX-FileCopyrightText: 2023 Radovan Bast <radovan.bast@uit.no>
#
# SPDX-License-Identifier: MIT

set -euo pipefail

if [ ! -f venv.sif ]; then
  singularity pull https://github.com/bast/singularity-venv/releases/download/0.3.0/venv.sif
fi

for file in wing-comparison.py important-points.py moving-polar.py; do
    ./venv.sif python $file
done
