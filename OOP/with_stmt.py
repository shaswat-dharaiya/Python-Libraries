class TextWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name
        print("__init__, {}".format(self.file_name))

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        print("__enter__")
        return self.file

    def __exit__(self, *args, **kwargs):
        self.file.close()
        print("__exit__ {} - {}".format(args,kwargs))

# using with statement with TextWriter

print("Outside with statement")
with TextWriter('my_file.txt') as xfile:
    print("Inside with statement")
    xfile.write('hello world')
    print("End of with statement")

print("Outside post with statement")
