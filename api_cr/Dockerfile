FROM python:3.8.10

# Copy application to the container
COPY . /api_cr/

# Update the system and install Python
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get clean

# Install pip    
RUN apt-get install -y python3-pip

# Upgrade pip
RUN pip3 install --upgrade pip

# Install requirements as root
RUN pip3 install -r /api_cr/requirements.txt

# Expose port
EXPOSE 5002

# Create a new user
RUN useradd -ms /bin/bash appuser

# Change ownership of the /maia directory to appuser
RUN chown -R appuser:appuser /api_cr

# Switch to the new user
USER appuser

# Set the working directory
WORKDIR /api_cr

#Initiate streamlit app
CMD ["uvicorn", "main:app", "--port", "5002", "--host", "0.0.0.0"]

