FROM python:3.8.10

# Copy application to the container
COPY . /api_fd/

# Update the system and install Python
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get clean

# Install pip    
RUN apt-get install -y python3-pip

# Upgrade pip
RUN pip3 install --upgrade pip

# Install requirements as root
RUN pip3 install -r /api_fd/requirements.txt

# Expose port
EXPOSE 5001

# Create a new user
RUN useradd -ms /bin/bash appuser

# Change ownership of the /maia directory to appuser
RUN chown -R appuser:appuser /api_fd

# Switch to the new user
USER appuser

# Set the working directory
WORKDIR /api_fd

#Initiate streamlit app
CMD ["uvicorn", "main:app", "--port", "5001", "--host", "0.0.0.0"]

