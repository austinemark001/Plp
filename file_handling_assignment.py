my_file = open('my_file.txt', 'w')

my_file.write('hello Im Austine\n I love progamming more so python\n my number 1')

my_file.close()

try: 
    my_file = open('my_file.txt', 'r')
    print(my_file.readlines())
    my_file.close()
    my_file = open('my_file.txt', 'a')
    my_file.write('this is the first new line\n I want to know programming \n to help the world in the future')
    my_file.close()
except:
    raise FileNotFoundError
finally:
    print('thanks for running the code')
