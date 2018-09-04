def outer():
    def inner():
        print('This is inner')

    print('This is outer, returning inner.')
    return inner


i = outer()  # 이건 i = inner 이므로 i() = inner()임.
print(i())