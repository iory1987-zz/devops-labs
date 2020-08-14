FROM sonarqube

ENV SONAR_SCANNER_VERSION=2.5.1 \
    SONAE_URL=https://binaries.sonarsource.com/Distribution \
    SONARQUBE_HOME=/opt/sonarqube \
    SONAR_RUNNER_HOME=/opt/sonar-scanner \
    PATH=$PATH:/opt/sonar-scanner/bin 

# Http port
EXPOSE 9000
EXPOSE 9092

RUN set -x \
    && echo "---> Installing Sonar Scanner" \
    && wget -O sonarscanner.zip --no-verbose $SONAE_URL/sonar-scanner-cli/sonar-scanner-$SONAR_SCANNER_VERSION.zip \
    && unzip sonarscanner.zip \
    && mv sonar-scanner-$SONAR_SCANNER_VERSION sonar-scanner \
    && rm sonarscanner.zip \
    && echo "---> Installing Slack Plugin" \
    && wget --no-verbose https://github.com/kogitant/sonar-slack-notifier-plugin/releases/download/2.1.2/cks-slack-notifier-2.1.2.jar \
    && mv cks-slack-notifier-2.1.2.jar $SONARQUBE_HOME/extensions/plugins/ 

VOLUME "$SONARQUBE_HOME/data"

WORKDIR $SONARQUBE_HOME