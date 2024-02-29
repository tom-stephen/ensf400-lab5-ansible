FROM alpine:3.9

# Install nginx
RUN apk --no-cache add nginx

# Copy config files in
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose the port that nginx will listen on
EXPOSE 80

# Comand to start nginx
CMD ["nginx", "-g", "deamon off;"]