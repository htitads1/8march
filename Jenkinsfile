pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'  // Virtual environment path
        APP_DIR = 'C:\\path\\to\\your\\app'  // Change to your actual app directory
        STREAMLIT_PORT = '8501'  // Change if needed
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/htitads1/8march.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat """
                cd %APP_DIR%
                if not exist %VENV_DIR% python -m venv %VENV_DIR%
                call %VENV_DIR%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Deploy Streamlit App') {
            steps {
                bat """
                for /f \"tokens=5\" %%a in ('netstat -ano ^| findstr :%STREAMLIT_PORT%') do taskkill /F /PID %%a || echo No process found
                start /B %VENV_DIR%\\Scripts\\python -m streamlit run app.py --server.port=%STREAMLIT_PORT% --server.headless=true
                """
            }
        }
    }
}
