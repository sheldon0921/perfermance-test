#!/bin/bash
: <<!
@FileName           :CollectionApi.sh
@Copyright          :Copyright ©2014-2021 创业翼
@Author             :GourdBoy
@Date               :2021/10/12
!
function CollectionApi(){
newman_path='node_modules/newman/bin/newman.js'
# shellcheck disable=SC2045
# shellcheck disable=SC2006
  for file in ` ls "$1"`
    do
        if [[ -d $1"/"${file} ]]
          then
          CollectionApi "$1""/""${file}"
        else
            local path=$1"/"${file}
            local name=${file}
            if [[ ${name} == *json ]]
              then
              ${newman_path} run "${path}" -r cli,junit --reporter-junit-export report/result/postmanout.xml
            fi
        fi
    done
}
INIT_PATH="PostmanScene/HaveStoreVersion/"
CollectionApi ${INIT_PATH}