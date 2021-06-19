#openapi-sdkgen.sh generate  -g ibm-java -i /my/apidefdir/apidef.json -c config.json -o /my/outputdir/java
#./openapi-sdkgen.sh generate  -g ibm-java -i ./apis-docs/platform-service/case-management/case-management.yaml -o ./java-out
#./openapi-sdkgen.sh generate  -g ibm-java -i ./apis-docs/dv-1.5.yaml -o ./java-out
#./openapi-sdkgen.sh generate  -g ibm-go -i ./apis-docs/dv-1.5.yaml -o ./go-out
#./openapi-sdkgen.sh generate  -g ibm-go -i ./apis-docs/dv-1.5-OAS-3.0.yaml -o ./go-out
#./openapi-sdkgen.sh generate  -g ibm-go -i ./apis-docs/dv-1.5.json -o ./go-out
#./openapi-sdkgen.sh generate  -g ibm-java -i ./apis-docs/dv-1.5.json -o ./java-out
./openapi-sdkgen.sh generate --genITs -g ibm-java -i ./apis-docs/dvaas.json -o ./java-out
./openapi-sdkgen.sh generate --genITs -g ibm-go -i ./apis-docs/dvaas.json -o ./go-out
./openapi-sdkgen.sh generate --genITs -g ibm-python -i ./apis-docs/dvaas.json -o ./python-out
./openapi-sdkgen.sh generate --genITs -g ibm-node -i ./apis-docs/dvaas.json -o ./node-out
#./openapi-sdkgen.sh generate  -g ibm-go -i ./apis-docs/platform-service/case-management/case-management.yaml -o ./go-out
#./openapi-sdkgen.sh generate  -g ibm-go -i ./apis-docs/mytest.json -o ./go-out
