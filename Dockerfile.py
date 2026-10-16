# Build from a slim Debian/Linux image
FROM debian:stable-slim

RUN apt-get update && apt-get install -y python3

# Copy our code into the image
COPY main.py main.py

# Copy our data dependencies
COPY books/ books/

# Run our Python script
CMD ["python3", "main.py"]
