def do_twice(function, argument):
    function(argument)
    function(argument)
def print_twice(text):
    print(text)
    print(text)
def do_four(function, a):
    function(a)
    function(a)
    function(a)
    function(a)
def do_four_short(function, a): #реализация функции do_four для меня была понятней и проще, но все же эта функция лучше, так как она компактнее и при ее создании используется способ разработки снизу-вверх, то есть для этой функции ранее была написана функция-подзадача. так код читается лучше, происходит меньше дублирования, его легче отлаживать и расширять
    do_twice(function, a)
    do_twice(function, a)
do_twice(print_twice, 'спам')
do_four(print, 4)
do_four_short(print, 7)
