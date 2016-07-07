echo "<fdo_objects>" >$2 
cat $1 | ~/TOMITA_PARSER/build/bin/tomita-parser config.proto >> $2
python process_xml.py $2 $1 $3



