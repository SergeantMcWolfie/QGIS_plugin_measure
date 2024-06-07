<html>
<body>
<h3>WYMAGANIA SYSTEMOWE:</h3> <br>

<ul>
<li>system Windows 11 
<li>program QGIS w wersji minimum 3.34
<li>python 3.11
<li>biblioteka qgis.PyQt
<li>biblioteka qgis.core
<li>biblioteka qgis.utils
<li>biblioteka numpy
<li>biblioteka os
</ul> <br>

<h3>FUNKCJE WTYCZKI:</h3><br>

<h4><b> 1. Liczenie różnic wysokości pomiędzy dwoma punktami </h4></b>

<p> Aby policzyć różnicę wysokości między punktami należy z grupy punktów znajdujących się na tej samej warstwie wybrać <b>dokładnie dwa</b>. Program pobierze wtedy wartości z tabeli atrybutów w programie QGIS z kolumny o nazwie <b>'wysokosc'</b>, w której znajdują się wysokości tych punktów. Wtyczka odejmuje wysokość punktu początkowego (pierwszy zaznaczony) od wysokości punktu końcowego (drugi zaznaczony), co da wynik o znaku dodatnim bądź ujemnym - zależnie od tego w jakiej kolejności podamy nasze punkty. Na podstawie znaku uzyskanego przewyższenia będzie można zatem stwierdzić, czy na wybranym odcinku nastąpił wzrost czy spadek terenu. <br><br>

Aby wtyczka poprawnie obliczyła różnicę wysokości pomiędzy punktami, zaznaczone punkty muszą znajdować się na warstwie o nazwie <b>'agencje_zatrudnienia'</b> lub takiej, która w tabeli artybutów posiada kolumnę z wysokościami o nazwie <b>'wysokosc'</b>.<br><br>

Podany wynik wyrażony jest w metrach, z dokładnością do 0,1 metra. </p> 

<h4><b> 2. Liczenie pola powierzchni pomiędzy zaznaczonymi punktami: </h4></b>

<p> Do obliczenia pola powierzchni między punktami należy z jednej warstwy wybrać <b> przynajmniej trzy punkty </b>. Następnie na podstawie współrzędych tych punktów, program policzy pole powierzchni zawarte między nimi - przy użyciu metody Gaussa. <br><br>

Podany wynik wyrażany jest w m<sup>2</sup>, z dokładnością do 0,1 m<sup>2</sup>.
</p>

<h3> SPOSÓB UŻYCIA WTYCZKI: </h3>

<p> Na samym początku należy pobrać wtyczkę (folder o nazwie 'measure_dharea') i umieścić ją w folderze z wtyczkami (prawdopodobna ścieżka z wtyczkami Twojego urządzenia: <b>"C:\Users\XXX\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins" ----> NALEŻY ZMIENIĆ "XXX" NA TWOJĄ NAZWĘ UŻYTKOWNIKA)</b> a następnie załadować wtyczkę w programie QGIS. <br><br>

Następnie wczytać trzeba mapę zawierającą potrzebne, wymienione wyżej artybuty oraz elementy geometrii i uruchomić warstwę o nazwie <b>'agencje_zatrudnienia'</b>.  <br><br>

Po wczytaniu mapy należy zaznaczyć na mapie odpowiednią liczbę punktów narzędziem o nazwie <b>'Zaznacz obiekty prostokątem lub kliknięciem'</b>. <br><br>

Po kliknięciu <b>'Oblicz przewyższenie'</b> lub <b>'Oblicz pole powierzchni'</b>, powinien pojawić się wynik w dolnej części okienka wtyczki. Jeśli użytkownik nie wybierze wymaganej do wykonania wybranej operacji liczby punktów, program wyświetli komunikat o powstałym błędzie i wymaganej ilości punktów do policzenia wybranej funkcji.<br> 
Dodatkowo informacja o uzyskanym wyniku wyświetli się w panelu Komunikatów (dymek czatu w prawym dolnym rogu programu QGIS), w zakładce 'Ogólne'. Komunikat będzie zawierać również informację o wybranych do policzenia żądanej wartości numerach punktów.
</p>

<h3> PRAWDOPODOBNE BŁĘDY PRZY UŻYCIU WTYCZKI I ZAPOBIEGANIE: </h3>

<h4><b> 1. Program nie liczy przewyższenia przy zaznaczeniu obiektów prostokątem </h4></b>

<p> Wynika to z faktu, że niektóre punkty znajdują się na tych samych współrzędnych, ale na innej wysokości. Użytkownik zaznaczając punkty kwadratem może przypadkiem zaznaczyć punkt znajdujący się pod spodem, przez co program wyświetli błąd o nieprawidłowej ilości punktów. W tym wypadku najlepiej zaznaczać punkty kliknięciem, a te niewidoczne za pomocą Tabeli atrybutów. </p>

<h4><b> 2. Program może policzyć pole powierzchni pomiędzy dwoma punktami </h4></b>

<p> Wynika to z problemu wymienionego wyżej. Zaznaczenie prostokątem spowoduje zaznaczenie więcej niż jednego punktu i wartość pola wynosić będzie 0m<sup>2</sup>. Nie ma to jednak wpływu na pole powierzchni między oddalonymi od siebie punktami, które mają inne punkty pod sobą - wtyczka liczy pole na podstawie współrzędnych płaskich. </p> 


</body>
</html>
