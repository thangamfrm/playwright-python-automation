# Playwright Python Automation

This Test Automation Framework and Test Suites ( WebUI and REST API ) are implemented using Python and Playwright Tool.

## Installation & Setup

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   ```
   
2. **Activate the virtual environment:**
   * **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```
   * **Windows (Command Prompt):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   * **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
     
3. **Install the project and dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Bring up the Applications

This projects does functional testing

1. Spring Pet Clinic REST API
```bash
git clone https://github.com/spring-petclinic/spring-petclinic-rest.git
cd spring-petclinic-rest
./mvnw spring-boot:run
```

2. AWS Secret Agent Shop
```bash
mkdir -p aws-secret-agent-shop
cd aws-secret-agent-shop/
wget https://github.com/aws-containers/retail-store-sample-app/releases/latest/download/docker-compose.yaml
DB_PASSWORD='my-pwd' docker compose --file docker-compose.yaml up
```

## Running Tests

This project uses `pytest`. Once your virtual environment is active and dependencies are installed, run the test suite with:

1. REST API (Spring Pet Clinic ): 
```bash
pytest tests/api/spring_petclinic/
```

2. WebUI (AWS Secret Agent Shop):
```bash
pytest tests/webui/aws_secretagentshop
```

