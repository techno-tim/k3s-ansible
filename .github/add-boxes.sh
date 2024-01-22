#!/bin/bash

# add-boxes.sh
# list add boxes on system and add
# already present on the system.

set -euo pipefail

PROVIDER=virtualbox

# Read the boxes that are currently present on the system (for the current provider)
present_boxes=$(
    (vagrant box list |
        grep "${PROVIDER}" | # Filter by boxes available for the current provider
        awk '{print $1;}' |  # The box name is the first word in each line
        sort |
        uniq) ||
        echo "" # In case any of these commands fails, just use an empty list
)

# Add all boxes
  echo "${present_boxes}" | while IFS= read -r box; do
      vagrant box add --provider "${PROVIDER}" "${box}"
  done
