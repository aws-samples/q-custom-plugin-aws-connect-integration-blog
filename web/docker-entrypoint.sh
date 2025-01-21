#!/bin/sh

# Replace environment variables in JavaScript files
envsubst < /usr/share/nginx/html/assets/env.template.js > /usr/share/nginx/html/assets/env.js

# Start Nginx
exec "$@"
