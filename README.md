# cdv_python_zaliczenie
Testy automatyczne wybranej aplikacji z użyciem pythona i selenium webdriver.
Aplikacja: http://automationpractice.com/index.php

PUSZCZANIE TESTÓW

Wszystkie testy:
Komenda 'pytest' będąc w folderze 'cdv_python_zaliczenie'

Wybrany test:
Komenda 'pytest wybrany_test.py' będąc w folderze 'page_object_pattern/tests'


RAPORTY: Allure

1. Instalacja allure-pytest
2. Instalacja Allure Framework z https://docs.qameta.io/allure/#_installing_a_commandline
3. Jeśli zachodzi taka potrzeba, usuwamy pliki z folderu 'report'.
4. Będąc w folderze 'cdv_python_zaliczenie' wykonujemy komendę: pytest --alluredir=ścieżka/do/folderu 'report'
   Zapisze to raporty z testów we wskazanym folderze.
5. Będąc w folderze 'cdv_python_zaliczenie' wykonujemy komendę: allure serve ścieżka/do/folderu 'report'.
   Uruchomi to server i otworzy przeglądarkę (lub nową kartę) z wygenerowanym raportem z testów. Można również użyć wygenerowanego w termianlu linku.
   Za pomocą ctrl+c wyłączamy serwer.