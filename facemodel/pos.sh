grep "\"Model::$1" -A 12 "$2" | grep "Lcl Translation" | awk -F ',' 'BEGIN{print "{\"data\":["}''{printf "{\"x\":%f,\"y\":%f,\"z\":%f},\n",$5,$6, $7} ''END{print "]}"}'
