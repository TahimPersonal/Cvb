# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (not needed for Koyeb, but useful for debugging)
EXPOSE 8080

# Run the bot
CMD ["python", "bot.py"]
