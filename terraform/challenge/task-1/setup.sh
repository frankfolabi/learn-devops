#!/bin/bash
# Run terraform plan in all subdirectories with .tf files

find . -type f -name "*.tf" -exec dirname {} \; | sort -u | while read -r dir; do
  echo "🔍 Running terraform plan in: $dir"
  (cd "$dir" && terraform fmt && terraform init && terraform apply --auto-approve)
  if [ $? -ne 0 ]; then
    echo "❌ Error running terraform in $dir"
    exit 1
  fi
  echo "✅ Successfully ran terraform in $dir"
  echo "----------------------------------------"
done

