FROM python:3.8-slim

# Install production dependencies.
ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy local code to the container image.
WORKDIR /app
COPY . .

ENV PORT 80
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 0 main:app