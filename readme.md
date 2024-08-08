# Azure Python WebJob: CSV Record Inserter

This repository contains a Sample Python WebJob script that is designed to manage a CSV file by appending new records with a timestamp and an incremented integer value.

## Overview

The WebJob script performs the following tasks:
1. **Read from a CSV File**: The script reads from a CSV file located at `/home/site/wwwroot/data.csv`.
2. **Increment Value**: The script determines the next integer value to insert, which increments by 1 with each execution.
3. **Append Record**: The script appends a new record with the current timestamp and the incremented integer value to the CSV file.
4. **Logging**: All operations and errors are logged to `/home/LogFiles/webjob.log`.

## Prerequisites

- Python 3.x
- Required Python packages: `pandas`
- Azure App Service 

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
