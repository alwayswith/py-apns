#!/bin/bash

openssl pkcs12 -in apns-dev-cert.p12 -out apns-dev-cert.pem -nodes -clcerts
chmod 400 apns-dev-cert.pem
