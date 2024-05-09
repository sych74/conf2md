#!/bin/bash
SPACE="VHS90AG"
INPUT_DIR="/home/builder/test/${SPACE}"
OUTPUT_DIR="/home/builder/test/content/${SPACE}"

IS_LOOP=true

rm -rf ${OUTPUT_DIR}
mkdir -p ${OUTPUT_DIR}

attachmentLinksFix(){
  local index_file="$1"
  local index_dir=$(dirname $index_file)
  local full_attach_list=$(sed -n '/^## Attachments:/,${p}' "${index_file}" | sed '1d')

  for full_attach in $(echo "$full_attach_list" | grep -oP 'attachments/\K[^)]+' | sed '/^$/d'); do
    attachment=$(basename "$full_attach")
    rsync -a ${INPUT_DIR}/attachments/${full_attach} ${index_dir}
    sed -i "s|attachments/${full_attach}|${attachment}|g" $index_file
  done
}

indexLinksFix(){
  IS_LOOP=false
  local index_file="$1"
  while IFS= read -r line; do
    if [[ $line =~ ^-\ +\[[^\]]+\]\([^\)]+\)$ ]]; then
      if [[ $line =~ \[([^\]]+)\]\(([^\)]+)\) ]]; then

	echo "========= $link"
        link="${BASH_REMATCH[2]}"
        new_link=$(echo "$link" | tr '[:upper:]' '[:lower:]' | tr '_' '-')

        if [[ ${new_link:0:1} == "." ]]; then
          new_link="${new_link:1}"
        fi
      
        if [ -n "$(find ${OUTPUT_DIR} -type d -name "${new_link}")" ]; then
          index_dir=$(dirname $index_file)
          link_dir=$(find ${OUTPUT_DIR} -type d -name "${new_link}")
          if [ ! -n "$(find ${index_dir} -type d -name "${new_link}")" ]; then
            mv "${link_dir}" ${index_dir}
            IS_LOOP=true
          fi
          sed -i "s/${link}/${new_link}/g" "${index_file}"
        fi
      fi
    fi
  done < $index_file
}

for file in  ${INPUT_DIR}/.*v7.1Beta.md; do
  name=$(basename "$file" .md)
#  name=$(echo "$name" | sed 's/_v7\.1Beta//')
  directory=$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr '_' '-')

  if [[ ${directory:0:1} == "." ]]; then
    directory="${directory:1}"
  fi

  mkdir "${OUTPUT_DIR}/$directory"
  cp "$file" "${OUTPUT_DIR}/$directory/index.md"

  title=$(grep -m 1 "^#" "$file" | sed 's/^# *//')
  title_new=$title
  if [[ ${title:0:1} == "." ]]; then
    title_new="${title:1}"
  fi

  sed -i "s/${title}/${title_new}/g" "${OUTPUT_DIR}/$directory/index.md"


  echo '---
draft: false
title: "'"$title_new"'"
aliases: "/'$directory'/"
seoindex: "index, follow"
seotitle: "'"$title_new"'"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "'"$title_new"'"
        url: "/'$directory'/"
        weight: 10
        parent: "get-started"
        identifier: "'$directory'.md"
---' | cat - "${OUTPUT_DIR}/$directory/index.md" > temp && mv temp "${OUTPUT_DIR}/$directory/index.md"

done


indexFiles=$(find ${OUTPUT_DIR} -type f -name "index.md")
IFS=$'\n'
  
for index in $indexFiles; do
      echo "Attachments processing: $index"
      attachmentLinksFix $index;
done

count=0
while [ $count -lt 5 ]; do

#while [ "$IS_LOOP" = true ]; do

indexFiles=$(find ${OUTPUT_DIR} -type f -name "index.md")
IFS=$'\n'
  
  for index in $indexFiles; do
    if [ -f "$index" ]; then
      echo "Index processing: $index"
      indexLinksFix $index;
    fi
  done

((count++))

done
