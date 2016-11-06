#!/bin/bash
set -eo pipefail

sleep 5

curl web/v1/countries | grep -q 'Invalid request'
curl web/v1/countries?target=source | grep -q 'United Kingdom'
curl web/v1/countries?target=destination | grep -q 'Spain'

echo "Tests passed!"
exit 0
