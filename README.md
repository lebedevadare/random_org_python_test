## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/YOUR_GITHUB_USERNAME/random_org_python_test.git
    cd random_org_python_test
    ```
   
2. Cоздайте виртуальное окружение:
    ```sh
    python -m venv venv
    ```
3. Активируйте виртуальное окружение:
    ```sh
    source venv/bin/activate
    ```
   
4. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    playwright install
    ```

## Запуск тестов

1. Запустите тесты c помощью pytest:
    ```sh
   pytest tests/test_random_org.py
   ```
   
2. Для генерации отчета Allure:
   ```sh
   pytest --alluredir=allure-results
   allure serve allure-results
   ```