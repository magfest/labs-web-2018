#!/bin/bash

curl -s -k -d '{"method": "guest.list", "params": ["guest"]}' -H "X-Auth-Token: ${UBER_API_KEY}" -w "\n" https://labs2018.uber.magfest.org/uber/jsonrpc/ | sed '1s/^/{ "guests": /' | sed -e "\$a}" | jq '.guests.result[]|= {group, bio} | .guests.result[].group |= {name} | .guests.result[].bio |= {website, facebook, desc, twitter, pic_url}' > labs-2018/src/store/modules/guests.json
curl -s -k -d '{"method": "guest.list", "params": ["band"]}' -H "X-Auth-Token: ${UBER_API_KEY}" -w "\n" https://labs2018.uber.magfest.org/uber/jsonrpc/ | sed '1s/^/{ "bands": /' | sed -e "\$a}" | jq '.bands.result[]|= {group, bio} | .bands.result[].group |= {name} | .bands.result[].bio |= {website, facebook, desc, twitter, pic_url}' > labs-2018/src/store/modules/bands.json
