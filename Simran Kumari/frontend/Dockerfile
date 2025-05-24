# Use the official Nginx image as the base image
FROM nginx:alpine

# Copy the frontend files to the Nginx html directory
COPY . /usr/share/nginx/html

# Expose the port Nginx will run on
EXPOSE 80

# Nginx starts automatically, no CMD needed