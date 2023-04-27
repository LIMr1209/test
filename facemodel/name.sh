grep "\"Model::$1" "$2" | awk '{print $3}' | sed 's/Model:://g' | awk 'BEGIN{print "{\"data\":["}''{print $1}''END{print "]}"}'
