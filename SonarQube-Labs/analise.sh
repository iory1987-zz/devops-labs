#!/bin/bash

# Export do binario
export PATH=$PATH:./sonar-scanner/bin/

# Executar analise.
sonar-scanner \
-Dsonar.projectKey="Python" \
-Dsonar.projectName="Python" \
-Dsonar.sources=samples/python/ \
-Dsonar.host.url=http://localhost:9000

sonar-scanner \
-Dsonar.projectKey="PHP" \
-Dsonar.projectName="PHP" \
-Dsonar.sources=samples/php/ \
-Dsonar.host.url=http://localhost:9000
